import socket
import sys
import time


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
			choice = input("Please choose rock/paper/scissors: ")
			sock.sendall(choice.lower().encode())
			result = sock.recv(128)
			countdown_output()
			print_result(int(result.decode()))

		finally:
			terminate = True
		    # print >>sys.stderr, 'closing socket'
	sock.close()

def countdown_output():
    print("The outcome of the game is ...")
    countdown = 3
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)

def print_result(result):
    if result == 1:
        print("Congratulations! You won the game! :)")
    elif result == -1:
        print("Sorry! You lost the game! :(")
    elif result == 0:
        print("It's a draw! :|")
