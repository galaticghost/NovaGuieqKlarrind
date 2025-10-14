import paho.mqtt.client as mqtt
from random import randint
import csv
import asyncio

async def cloud():
    def connect(host,port,timeout):
        client = mqtt.Client(userdata={})
        client.on_connect = on_connect
        client.connect(host,port,timeout)
        return client

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("[Cloud] Conectado ao broker MQTT")
            # Esse # é um caracter coringa para se inscrever em todos os tópicos de drone/
            client.subscribe("edge_server/#")
        else:
            print(f"[Cloud] Falha na conexão. Código: {rc}")

    def on_message(client, userdata, msg):
        required = ["edge_server/drone/soil_moisture",
                    "edge_server/drone/weather",
                    "edge_server/drone/images"]

        userdata[msg.topic] = msg.payload.decode()

        if all(data in userdata for data in required):
            for k,v in userdata.items():
                print(f"[Cloud] Mensagem recebida: {k} -> {v}")
            with open("database.csv","a",newline='') as file:
                fieldnames = required
                writer = csv.DictWriter(file,fieldnames=fieldnames)
                writer.writerow(userdata)
            userdata.clear()

    def generate_csv():
        with open("database.csv","w+",newline='') as file:
            writer = csv.DictWriter(file,["SoilMoisture","Weather","Images"])
            writer.writeheader()

    generate_csv()
    client = connect("localhost",1883,60)
    client.on_message = on_message
    client.loop_start()

    while True:
        await asyncio.sleep(1)

async def edge_server():
    def connect(host,port,timeout):
            client = mqtt.Client(userdata={
                "soil_count":0,
                "moisture":0,
                "weather_count":0,
                "images_count":0,
                "all_images":""
                })
            client.on_connect = on_connect
            client.connect(host,port,timeout)
            return client


    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("[Edge Server] Conectado ao broker MQTT")
            # Esse # é um caracter coringa para se inscrever em todos os tópicos de drone/
            client.subscribe("drone/#")
        else:
            print(f"[Edge Server] Falha na conexão. Código: {rc}")

    def on_message(client, userdata, msg):
        payload = msg.payload.decode()
        
        if msg.topic == "drone/soil_moisture":
            payload = int(payload)
            if payload > 50: # Tenho que ser mais criativo com isso daqui TODO
                print("[Edge Server] Solo úmido")
            else:
                print("[Edge Server] Solo não úmido")
            userdata["soil_count"] += 1
            userdata["moisture"] += payload
            if userdata["soil_count"] == 10:
                moisture = userdata["moisture"] / 10
                client.publish(f"edge_server/{msg.topic}",moisture)
                userdata["soil_count"] = userdata["moisture"] = 0

        elif msg.topic == "drone/weather":
            print(f"[Edge Server] Clima: {payload}")
            userdata["weather_count"] += 1
            if userdata["weather_count"] == 10:
                client.publish(f"edge_server/{msg.topic}",payload)
                userdata["weather_count"] = 0
        
        elif msg.topic == "drone/images":
            print("[Edge Server] Imagem: *Imagem imaginaria*")
            userdata["all_images"] += payload
            userdata["images_count"] += 1
            if userdata["images_count"] == 10:
                imageszip = userdata["all_images"]
                client.publish(f"edge_server/{msg.topic}",imageszip)
                userdata["images_count"] = 0
                userdata["all_images"] = ""

    client = connect("localhost",1883,60)
    client.on_message = on_message
    client.loop_start()

    while True:
        await asyncio.sleep(1)

async def drone():
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
        
    client = connect("localhost",1883,60)
    client.loop_start()
    x = randint(0,3) # Usado para o clima
    while True:
        soil_moisture = get_soil_moisture()
        client.publish("drone/soil_moisture",soil_moisture)
        
        # O clima é escolhido no inicio porque seria estranho ter chuva
        # e depois sol e depois nublado e etc.
        weather = get_weather(x)
        client.publish("drone/weather",weather)
        #Imagine que Images.png sejam imagens e não um texto
        client.publish("drone/images","Images.png")

        await asyncio.sleep(2)

async def main():
    await asyncio.gather(
        drone(),
        edge_server(),
        cloud()
    )

if __name__ == "__main__":
    asyncio.run(main())