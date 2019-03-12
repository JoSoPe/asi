from socket import *

serverPort=12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print "The server is ready to receive"
while 1:
    messageLowerCase, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = messageLowerCase.upper()
    serverSocket.sendto(modifiedMessage,clientAddress)
