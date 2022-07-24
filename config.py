import os
from datetime import timedelta

class Config(object):
    DEBUG = True
     # MQTT Brocker Configuration 
    MQTT_BROKER_URL = 'broker.emqx.io'
    MQTT_BROKER_PORT=1883
    MQTT_USERNAME=""
    MQTT_PASSWORD=""
    MQTT_KEEPALIVE=5
    MQTT_TLS_ENABLED=False
