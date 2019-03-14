# Echo client program
import socket
import sys

print ("C: IP")
HOST = raw_input('C: ')    # The remote host "172.20.2.1"
PORT = 50007              # The same port as used by the server
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print 'could not open socket'
    sys.exit(1)
connected = True
while connected:
    MSG = raw_input('M: ')
    s.sendall(MSG)
    data = s.recv(1024)
    if data == 'D':
        connected = False
        print repr(data) , 'Properly disconected '
        break
    print 'M->', repr(data)
    
s.close()


