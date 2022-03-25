from Client.Client import Client
from Server.Server import Server

localIP = "127.0.0.1"

localPort = 20003

bufferSize = 1024
dropRate = 30
timeOut=2

client = Client(localIP, localPort, bufferSize,2)
client.start()
client.ping(10)

