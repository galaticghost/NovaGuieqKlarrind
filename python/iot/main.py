import time

import paho.mqtt.client as paho
from paho import mqtt

client = paho.Client(client_id="1", userdata=None, protocol=paho.MQTTv5)
topic = "python/mqtt"

client.username_pw_set("admin", "hivemq")

client.connect("localhost", 1883, 60)

while True:

    client.publish("test_topic", "WORK WORKIO WORKI RKOKIW !!!!!!", 0,retain=True)
    client.publish("encyclopedia/temperature", payload="hot", qos=1)

    client.loop_forever()