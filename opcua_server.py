from opcua import Server
from random import randint
import datetime
import time

server = Server()

url = "opc.tcp://localhost:4041"
server.set_endpoint(url)

name = "OPC_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace,"Parameters")

Temp = Param.add_variable(addspace,"emperature",0)
Press = Param.add_variable(addspace,"Pressure",0)
hum = Param.add_variable(addspace,"Humidity",0)
hum1 = Param.add_variable(addspace,"air",0)
hum2 = Param.add_variable(addspace,"people",0)
hum3 = Param.add_variable(addspace,"house",0)
#Time = Param.add_variable(addspace,"Time",0)

Temp.set_writable()
Press.set_writable()
hum.set_writable()
hum1.set_writable()
hum2.set_writable()
hum3.set_writable()
#Time.set_writable()

server.start()
print("server started at {}".format(url))

while True:
	Temperature = str(randint(10,50))
	Pressure = str(randint(200,999))+"asd"
	Humidity = str(randint(1000,1999))
	Humidity1 = str(randint(500,1999))
	Humidity2 = str(randint(300,1999))+"q"
	Humidity3 = str(randint(10,1999))
	#Time = datetime.datetime.now()

	print("Temp :",Temperature,"  Press :",Pressure,"Hum :",Humidity)

	Temp.set_value(Temperature)
	Press.set_value(Pressure)
	hum.set_value(Humidity)
	hum1.set_value(Humidity1)
	hum2.set_value(Humidity2)
	hum3.set_value(Humidity3)
	#Time.set_value(Time)

	time.sleep(10)
