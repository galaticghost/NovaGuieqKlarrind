import paho.mqtt.client as mqtt
from random import randint
from time import sleep

def start():
    client = connect("localhost",1883,60)
    client.loop_start()
    x = randint(0,3) # Usado para o clima
    while True:
        try:
            soil_moisture = get_soil_moisture()
            client.publish("drone/soil_moisture",soil_moisture)
            
            # O clima é escolhido no inicio porque seria estranho ter chuva
            # e depois sol e depois nublado e etc.
            weather = get_weather(x)
            client.publish("drone/weather",weather)

            #Imagine que Images.png sejam imagens e não um texto
            client.publish("drone/images","Images.png")

            sleep(2)
        # Crtl + C para desconectar
        except KeyboardInterrupt:
            print("\nDesconectando")
            client.loop_stop()
            client.disconnect()
            break

def connect(host,port,timeout):
    client = mqtt.Client()
    client.connect(host,port,timeout)
    return client

def get_soil_moisture():
    return randint(0,100)

def get_weather(x):
    if x == 0:
        return "Limpo"
    elif x == 1:
        return "Nublado"
    elif x == 2:
        return "Chuva"
    else:
        return "Tempestadade"
    
start()