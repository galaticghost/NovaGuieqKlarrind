import paho.mqtt.client as mqtt
import csv

def main():
    generate_csv()
    client = connect("localhost",1883,60)
    client.on_message = on_message
    client.loop_forever()

def connect(host,port,timeout):
    client = mqtt.Client(userdata={})
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
    required = ["edge_server/drone/soil_moisture",
                "edge_server/drone/weather",
                "edge_server/drone/images"]

    userdata[msg.topic] = msg.payload.decode()

    if all(data in userdata for data in required):
        for k,v in userdata.items():
            print(f"Mensagem recebida: {k} -> {v}")
        with open("database.csv","a",newline='') as file:
            fieldnames = required
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writerow(userdata)
        userdata.clear()

def generate_csv():
    with open("database.csv","w+",newline='') as file:
        writer = csv.DictWriter(file,["SoilMoisture","Weather","Images"])
        writer.writeheader()

main()