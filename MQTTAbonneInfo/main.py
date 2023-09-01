# This is a sample Python script.
import time

import paho.mqtt.client as mqtt

# Fonction callback pour la connexion au serveur MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connecté au serveur MQTT")
        client.subscribe(MQTT_TOPIC)  # S'abonne au sujet "topic/version"
        print("subribe"+MQTT_TOPIC)
    else:
        print(f"Échec de la connexion au serveur MQTT avec le code d'erreur: {rc}")

# Fonction callback pour la réception des messages MQTT
def on_message(client, userdata, msg):
    print(f"Message reçu sur le sujet '{msg.topic}': {msg.payload.decode()}")

# Créez un client MQTT
MQTT_BROKER = "10.4.1.42"
MQTT_TOPIC = "jacob/temperature/sensor"
client = mqtt.Client()

# Définir les fonctions de callback
client.on_connect = on_connect
client.on_message = on_message

# Connexion au serveur MQTT à l'adresse 10.9.1.42
client.connect(MQTT_BROKER, 1883, 60)

# Boucle principale pour maintenir la connexion et traiter les messages
time.sleep(2)
client.loop_forever()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
