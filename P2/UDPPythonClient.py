from socket import *

serverName='172.20.2.1'
serverPort=12000
clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
message = raw_input("Input lowercase sentence: ")
messageLowerCase = message.lower()
clientSocket.sendto(messageLowerCase,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage)
clientSocket.close()
