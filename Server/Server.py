import random
import sys
import time
from socket import *

from Utills import Utills


class Server:
	#constructor for inputs
	def __init__(self, address, port, drop_rate, buffer_size):
		self.buffer_size = buffer_size
		self.drop_rate = drop_rate
		self.address = address
		self.port = port
#start the server
	def start(self):
		self.serverSocket = socket(AF_INET, SOCK_DGRAM)
		self.serverSocket.bind((self.address,self.port))
		print('UDP Server is ready in '+ str(self.address)+':'+ str(self.port))
#wait for request
		while True:
			#take meesage and address
			message, address = self.serverSocket.recvfrom(self.buffer_size)
			current_time=Utills.current_time_ms()
			print('Message received at ' + str(current_time) + ': [' + message.decode()+']')
#make a random distrubuted number between 0 to 100
			random_number = random.randint(0, 100)
			print("random Number is : "+str(random_number))
			#if this number is smaller than the drop rate dont send response
			if random_number < self.drop_rate:
				continue
			#else make message uppercase and send it
			message = message.decode('utf-8').upper()
			self.serverSocket.sendto(message.encode('utf-8'), address)
			print('Message sent at ' + str(current_time) + ': [' + message+']')
		self.serverSocket.close()
