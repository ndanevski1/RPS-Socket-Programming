Collaboration:
Team Members: Nikola Danevski and Muhammad Usama Ijaz
Class: CSC 257
Project 1

Instructions to run the code:
Compile and execute server: python3 rps.py [Player Name] server [Port Number]
Compile and execute client: python3 rps.py [Player Name] client [Address shown when server is ran]:[Port Number]

Example Input/Output for server:
[mijaz@cycle1 RPS-Socket-Programming]$ python3 rps.py Usama server 5005
Server running!
Waiting for a client...
Server address & port =  128.151.69.85 : 5005
Hi! You're playing against Nikola
Please choose rock/paper/scissors: rock
The outcome of the game is ...
3
2
1
Sorry! You lost the game! :(

Example Input/Output for client: python3 rps.py Nikola client 128.151.69.85:5005
Hi Nikola ! Trying to connect to 128.151.69.85 : 5005
Hi! You are connected to the server. You are playing against Usama!
Please choose rock/paper/scissors: paper
The outcome of the game is ...
3
2
1
Congratulations! You won the game!

We used TCP protocol for this project. This can be seen in the following line of our code:
"sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)" 
since we use socket.SOCK_STREAM instead of socket.SOCK_DGRAM (which is used for UDP protocol). 

Furthermore, we performed the handshake when the client recieves the name of the server player, and vice versa and the following is displayed the user console:

Server handshake confirmation:
"Hi! You're playing against Nikola"

Client handshake confirmation:
"Hi! You are connected to the server. You are playing against Usama!"

Client sends the name of the player in the connection request and the server responds with the player name of its side and these messages are then printed out.
