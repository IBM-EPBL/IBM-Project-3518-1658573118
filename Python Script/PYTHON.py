import wiotp.sdk.device
import time
import os
import datetime
import random
myConfig = {
    "identity": {
        "orgId": "hj5fmy",
        "typeId": "Device1",
        "deviceId": "67890"
    },
    "auth": {
        "token": "87654321"
    }
}
client = wiotp.sdk.device.DeviceClient(config=myconfig, logHandlers=None)
client.connect()


def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %S" % cmd.data['command'])
    m=cmd.data['command']
    if(m=="motoron"):
        print("Motor is switched on")
    elif(m=="motoroff"):
            print("Motor is switched OFF")
    print(" ")
while True:
        soil=random.randint(0,100)
        temp=random.randint(-20,125)
        hum=random.randint(0,100)
        myData={'soil_moisture': soikl, 'temperature':temp, 'humidity':hum}
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        time.sleep(2)
        client.commandCallback = myCommandCallback
client.disconnect()
