from flask import Blueprint, request, jsonify,current_app
#from run import mqtt_client
import os
from flask_mqtt import Mqtt
from apps.factory import mqtt as mqtt_client
from apps.factory import device_id


# setting up blueprint
mqtt_broker= Blueprint('dummy_module',__name__,url_prefix='/dummy_module')

# Setting up topic as device id
topic = device_id


@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully',flush=True)
        mqtt_client.subscribe(topic) # subscribe topic
    else:
        print('Bad connection. Code:', rc)


@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )

    print('Received message on topic: {topic} with payload: {payload}'.format(**data),flush=True)

@mqtt_client.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)

@mqtt_broker.route('/publish', methods=['POST'])
def publish_message():
    request_data = request.get_json()
    publish_result = mqtt_client.publish(request_data['topic'], request_data['msg'])
    return jsonify({'code': publish_result[0]})


@mqtt_broker.route('/print', methods=['GET'])
def print_message():
    print("MESSAGE RECEIVED",flush=True)
    return jsonify({})
