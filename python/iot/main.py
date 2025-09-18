import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.loop_start()

try:
    while True:
        msg = input("Escreva sua mensagem: ")
        client.publish("test_topic", msg)
        print(f"Enviada: {msg}")
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    print("\nohno")
    client.loop_stop()
    client.disconnect()
