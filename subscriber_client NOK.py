# not functional
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost")
client.subscribe("test/topic")
client.loop_forever()
