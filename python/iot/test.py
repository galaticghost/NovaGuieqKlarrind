import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT")
        client.subscribe("test_topic")
        print("Assinatura do tópico 'test_topic' realizada")
    else:
        print(f"Falha na conexão. Código: {rc}")

def on_message(client, userdata, msg):
    print(f"Mensagem recebida: {msg.topic} -> {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
