import argparse, socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Instead of explicitly binding the socket to a given port and IP as we did
# previously, we can let the OS take care of it. Remember ephemeral ports?
# Yes, the OS will bind the socket to a port dynamically.

host = '127.0.0.1'
while True:
    s.connect((host, port))
    message = input('Input message to send to server:' )
    data = message.encode('ascii')
    s.send(data)
    data = s.recv(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    print('The server replied with {!r}'.format(text))
