# @file    
# @author  Jiaming ZHANG
# @date    09/04/2024
# @brief   This file provides an exemple of MQTT multi publisher application with paho lib

from paho.mqtt.enums import MQTTProtocolVersion
import paho.mqtt.publish as publish

msgs = [{'topic':"test/topic", 'payload':"first message from multi pub"},
    ("test/topic", "seconde message from multi pub", 0, False)]
publish.multiple(msgs, hostname="localhost", protocol=MQTTProtocolVersion.MQTTv5