# @file    
# @author  Jiaming ZHANG
# @date    09/04/2024
# @brief   This file provides an exemple of MQTT subscriber application with paho lib

import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("test/topic", hostname="localhost")
print("%s %s" % (msg.topic, msg.payload))