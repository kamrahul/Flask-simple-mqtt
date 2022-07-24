import logging
import os
import sys

#from celery import Celery
from flask import Flask
from flask_mqtt import Mqtt
from celery import Celery

mqtt = Mqtt()

# Setting up Device id 
device_id = os.getenv('DEVICE_NAME','123')

#initializing celery
celery = Celery(__name__, include=["apps.mqtt_module.task"])

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

    # Celery configuration for service to support celery task
    celery.conf.update(app.config)

    #Register blueprint
    from apps.mqtt_module.controller import mqtt_broker
    app.register_blueprint(mqtt_broker)

    return app

def create_celery():
    
    # Create flask app object
    app = Flask(__name__)

    # Setting configuration for the project 
    app.config.from_object('config.Config')

    # Adding log level
    app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    app.logger.setLevel(logging.DEBUG)

    # Initialize mqtt app
    mqtt.init_app(app)

    # Celery configuration for service to support celery task
    celery.conf.update(app.config)

    #Register blueprint
    from apps.mqtt_module.controller import mqtt_broker
    app.register_blueprint(mqtt_broker)

    return app

    

