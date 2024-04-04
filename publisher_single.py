import paho.mqtt.publish as publish

publish.single("test/topic", "Hello, MQTT!", hostname="localhost")
