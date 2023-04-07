import paho.mqtt.client as mqtt
import json as json
import base64

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    resultat_complet = json.loads(msg.payload.decode())
    print(resultat_complet)
    payload = resultat_complet['uplink_message']['frm_payload']
    date = resultat_complet
    print("Information reçu :",base64.b64decode(payload).decode(), "\nà la date : ",resultat_complet['received_at'])

client = mqtt.Client()
client.username_pw_set("toilettes-seches1@ttn","NNSXS.VMJP7SBDLP4LPJV5KA25OROU37IEIAIC43KN42I.AE5MZ64KDCB2SZAIFJEHZU6JQLHRQHYVYB3FI5OI7Z35WB3SVYEA")

client.on_connect = on_connect
client.on_message = on_message

client.connect("eu1.cloud.thethings.network", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()