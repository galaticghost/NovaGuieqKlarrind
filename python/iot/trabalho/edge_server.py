import paho.mqtt.client as mqtt

def main():
    client = connect("localhost",1883,60)
    client.on_message = on_message
    client.loop_forever()


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
        print("Conectado ao broker MQTT")
        # Esse # é um caracter coringa para se inscrever em todos os tópicos de drone/
        client.subscribe("drone/#")
    else:
        print(f"Falha na conexão. Código: {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    
    if msg.topic == "drone/soil_moisture":
        payload = int(payload)
        if payload > 50: # Tenho que ser mais criativo com isso daqui TODO
            print("Solo úmido")
        else:
            print("Solo não úmido")
        userdata["soil_count"] += 1
        userdata["moisture"] += payload
        if userdata["soil_count"] == 10:
            moisture = userdata["moisture"] / 10
            client.publish(f"edge_server/{msg.topic}",moisture)
            userdata["soil_count"] = userdata["moisture"] = 0

    elif msg.topic == "drone/weather":
        print(f"Clima: {payload}")
        userdata["weather_count"] += 1
        if userdata["weather_count"] == 10:
            client.publish(f"edge_server/{msg.topic}",payload)
            userdata["weather_count"] = 0
    
    elif msg.topic == "drone/images":
        print("imagem: *Imagem imaginaria*")
        userdata["all_images"] += payload
        userdata["images_count"] += 1
        if userdata["images_count"] == 10:
            imageszip = userdata["all_images"]
            client.publish(f"edge_server/{msg.topic}",imageszip)
            userdata["images_count"] = 0
            userdata["all_images"] = ""

main()