from opcua import Client
from opcua import ua
import time

url = "opc.tcp://localhost:4041"
client = Client(url)
client.connect()
while True:
    Temp = client.get_node("ns=2;i=2")
    Temperature = Temp.get_value()
    print(Temperature)

    Press = client.get_node("ns=2;i=3")
    Pressure = Press.get_value()
    print(Pressure)

    hum = client.get_node("ns=2;i=4")
    Humidity = hum.get_value()
    print(Humidity)
    print("")
    time.sleep(1)

