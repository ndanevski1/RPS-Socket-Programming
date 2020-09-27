import socket
import sys


def client(player, address, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (address, port)
	print("Hi", player,"!", "Trying to connect to", address,":",port)
	sock.connect(server_address)
	try:
		data = sock.recv(256)
		print(data.decode())
		message = "Hi! You're playing against " + player
		sock.sendall(message.encode())
		terminate = False
	except:
		print("There was an unexpected error!")
	while terminate!=True:
		try:
		    # Send data
		    choice = input("Please choose rock/paper/scissors: ")
		    # sys.stderr, 'sending "%s"' % message
		    sock.sendall(choice.lower().encode())
		    result = sock.recv(128)
		    printResult(int(result.decode()))

		finally:
			terminate = True
		    # print >>sys.stderr, 'closing socket'
	sock.close()

def printResult(result):
	if result == 1:
		print("Congratulations! You won the game.")
	elif result == -1:
		print("Sorry! You lost the game :(")
	elif result == 0:
		print("It's a draw!")

client("Usama", "10.5.35.107", 5005)