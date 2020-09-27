from client import client
from server import server

import sys

# print(sys.argv[0])

def main():
	if(sys.argv[2] == "client"):
		parse = sys.argv[3].split(":")
		client(sys.argv[1], parse[0], int(parse[1]))
	elif (sys.argv[2] == "server"):
		server(sys.argv[1], "localhost", int(sys.argv[3]))
	else:
		print("Improper input!")
main()