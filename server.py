import socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

# create new socket object s
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#  socket.socket(family, type, proto, fileno)
port = 3000
hostname = '127.0.0.1' # The hostname is the IP address that your server will listen on
s.bind((hostname, port)) # Binding the socket to a port and IP address
print('Listening at {}'.format(s.getsockname())) # Printing the IP address and port of socket

while True:
    data, address = s.recvfrom(MAX_SIZE_BYTES) # Receive at most 65535 bytes at once
    message = data.decode('ascii')
    upperCaseMessage = message.upper()
    print('The client at {} says {!r}'.format(clientAddress, message))
    data = upperCaseMessage.encode('ascii')
    s.sendto(data, clientAddress)    
