import time
from bicho import Bicho
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.loop_start()

bicho = Bicho("Jonas")

try:
    while True:
        client.publish("fome", bicho.fome)
        print(f"Enviada: {bicho.fome}")
        client.publish("feliz", bicho.feliz)
        print(f"Enviada: {bicho.feliz}")
        client.publish("cansado", bicho.cansado)
        print(f"Enviada: {bicho.cansado}")
        time.sleep(3)
        bicho.status()
except KeyboardInterrupt:
    pass
finally:
    print("\nohno")
    client.loop_stop()
    client.disconnect()
