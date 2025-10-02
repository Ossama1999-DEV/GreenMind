"""
client.py : communication MQTT entre Raspberry Pi et ESP32
"""

import paho.mqtt.client as mqtt

BROKER = "localhost"  # ou IP du Raspberry/ESP32
TOPIC = "greenmind/capteurs"


def on_connect(client, userdata, flags, rc):
    print("✅ Connecté au broker MQTT")
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    print(f"📩 Message reçu : {msg.topic} -> {msg.payload.decode()}")


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, 1883, 60)
    print("🔌 Connexion au broker MQTT...")

    client.loop_forever()


if __name__ == "__main__":
    main()
