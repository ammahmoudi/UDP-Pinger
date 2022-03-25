from Server.Server import Server

localIP = "127.0.0.1"

localPort = 20003

bufferSize = 1024
dropRate = 30

server = Server(localIP, localPort, dropRate, bufferSize)
server.start()

