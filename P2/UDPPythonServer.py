import socket

localIP = "172.20.2.1"
serverPort = 50007
bufferSize = 1024

messageFromServer = "Hola Client"
bytesToSend = str.encode(messageFromServer)

#Creem el datagrama del socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind a la IP i al port
UDPServerSocket.bind((localIP,serverPort))

print "Server UDP apunt i escoltant"

#Escoltat els datagrames que entrin

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    print clientMsg
    print clientIP
    
    # Enviant replica al client
    UDPServerSocket.sendto(bytesToSend, address)
