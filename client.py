import socket
import sys

# Create a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ("172.17.0.1", 5005)
sock.connect(server_address)

try:
    
    # Send data
    message = "Usama panchod"
    # sys.stderr, 'sending "%s"' % message
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        # sys.stderr, 'received "%s"' % data

finally:
    # print >>sys.stderr, 'closing socket'
    sock.close()