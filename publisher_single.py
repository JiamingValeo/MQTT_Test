# @file    
# @author  Jiaming ZHANG
# @date    09/04/2024
# @brief   This file provides an exemple of MQTT single publisher application with paho lib

import paho.mqtt.publish as publish

publish.single("test/topic", "Hello, MQTT from single pub", hostname="localhost")
