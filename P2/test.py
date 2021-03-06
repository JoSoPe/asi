#https://steelkiwi.com/blog/working-tcp-sockets/
# Echo server program
import socket
import sys

HOST = None               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = None
print 'Waiting Client'
def E0():
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                                  socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.bind(sa)
            s.listen(1)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        print 'could not open socket'
        sys.exit(1)
        E0()
    else:
        E1(s)

def E1(s):
    conn, addr = s.accept()
    print 'Connected by', addr
    received = True
    while received:
        data = conn.recv(1024)
        print data
        if data == 'D':
            received=False
            conn.send('D')
            print 'Client ',addr,' disconnect'
            break
        missatge=raw_input('m: ')
        conn.send(missatge)
    conn.close()
    E1(s)    
E0()
