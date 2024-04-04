import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("test/topic", hostname="localhost")
print("%s %s" % (msg.topic, msg.payload))