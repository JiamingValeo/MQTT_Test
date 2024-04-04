from paho.mqtt.enums import MQTTProtocolVersion
import paho.mqtt.publish as publish

msgs = [{'topic':"test/topic", 'payload':"first message"},
    ("test/topic", "seconde message", 0, False)]
publish.multiple(msgs, hostname="localhost", protocol=MQTTProtocolVersion.MQTTv5