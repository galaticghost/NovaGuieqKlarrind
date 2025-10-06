import paho.mqtt.client as mqtt
import csv

def main():
    client = connect("localhost",1883,60)
    client.on_message = on_message
    client.loop_forever()


def connect(host,port,timeout):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host,port,timeout)
    return client


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT")
        # Esse # é um caracter coringa para se inscrever em todos os tópicos de drone/
        client.subscribe("edge_server/#")
    else:
        print(f"Falha na conexão. Código: {rc}")

def on_message(client, userdata, msg):
    print(f"Mensagem recebida: {msg.topic} -> {msg.payload.decode()}")

main()