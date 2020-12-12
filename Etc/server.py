import argparse, socket

MAX_SIZE_BYTES = 65535 # receive at most these bytes of data at once

port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# create a socket object
# syntax: socket.socket(family, type, proto, fileno) AF_INET: This family is used with IPV4 addresses.
# SOCK_DGRAM : for UDP, SOCK_STREAM: For TCP
hostname = '127.0.0.1'
s.bind((hostname, port)) # bind socket with hostname and port
# The hostname is the IP address that your server will listen on.
print('Listening at {}'.format(s.getsockname()))
while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    print('The client at {} says {!r}'.format(clientAddress, message))
    msg_to_send = input('Input message to send to client:' )
    data = msg_to_send.encode('ascii') # decode from byte stream to ASCII
    s.sendto(data, clientAddress)
