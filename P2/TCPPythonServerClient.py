#https://steelkiwi.com/blog/working-tcp-sockets/
# Echo server program
import socket
import sys


PORT = 50007              # Arbitrary non-privileged port
s = None
def E0():
    print 'State 0 opening socket'
    HOST = None               # Symbolic name meaning all available interfaces
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
    print 'State 1 socket opened, waiting a client'
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

def E2():
    print 'State2 client mode opening socket'
    HOST = raw_input('C: ')    # The remote host "172.20.2.1"
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
        E2()
    connected = True
    E3(s,connected)

def E3(s,connected):
    print 'state3 soket opened properly, waiting message to send'
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
    E0()
E2()
