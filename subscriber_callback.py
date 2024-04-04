import paho.mqtt.subscribe as subscribe
# to do, not tested
def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    userdata["message_count"] += 1
    if userdata["message_count"] >= 5:
        # it's possible to stop the program by disconnecting
        client.disconnect()

subscribe.callback(on_message_print, "paho/test/topic", hostname="mqtt.eclipseprojects.io", userdata={"message_count": 0})