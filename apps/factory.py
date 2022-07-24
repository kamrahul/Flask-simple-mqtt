import logging
import os
import sys

#from celery import Celery
from flask import Flask
from flask_mqtt import Mqtt

mqtt = Mqtt()

# Setting up Device id 
device_id = os.getenv('DEVICE_NAME','123')

def create_app():
    
    # Create flask app object
    app = Flask(__name__)

    # Setting configuration for the project 
    app.config.from_object('config.Config')

    # Adding log level
    app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    app.logger.setLevel(logging.DEBUG)

    # Initialize mqtt app
    mqtt.init_app(app)

    #Register blueprint
    from apps.mqtt_module.controller import mqtt_broker
    app.register_blueprint(mqtt_broker)

    return app

    

