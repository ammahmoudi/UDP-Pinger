import time
import sys
from socket import *
from Utills import Utills

class Client:
    #constructor for inputs
    def __init__(self,address,port,buffer_size,time_out):
        self.port = port
        self.time_out = time_out
        self.address=address
        self.buffer_size=buffer_size


#make the socket and set the time out
    def start(self):
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)
        self.clientSocket.settimeout(self.time_out)
        #function that takes repeat_time and send pings to server
    def ping(self,repaet_time):
        for i in range(repaet_time):
            #sleep before sending ping
            time.sleep(1)
            #take the sent time
            sent_time = Utills.current_time_ms()
            #make the message
            message = 'Ping ' + str(i + 1) + " " + str(time.time())
            #send the message
            self.clientSocket.sendto(message.encode('utf-8'), (self.address, self.port))
            #log
            print('Message '+str(i)+' sent at ' + str(sent_time) + ': [' + message+']')
            try:
                #take the response
                response, server = self.clientSocket.recvfrom(self.buffer_size)
                #calculate the received time
                receivedTime = Utills.current_time_ms()
                #log
                print('response ' + str(i) + ' received at ' + str(receivedTime) + ':[ ' + response.decode('utf-8')+']')


            #if time out print it
            except timeout:
                print('Request '+str(i)+' TIMED OUT.')
