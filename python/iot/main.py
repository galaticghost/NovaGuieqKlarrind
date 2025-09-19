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
        print(f"Status fome: {bicho.fome}")
        client.publish("feliz", bicho.feliz)
        print(f"Status feliz: {bicho.feliz}")
        client.publish("cansado", bicho.cansado)
        print(f"Status cansado: {bicho.cansado}")
        time.sleep(3)
        bicho.status()
except KeyboardInterrupt:
    pass
finally:
    print("\nDesconectando")
    client.loop_stop()
    client.disconnect()
