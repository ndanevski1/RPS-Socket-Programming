#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys
import time
from netifaces import AF_INET, AF_INET6, AF_LINK
import netifaces as ni


# decides the choice from the server's perspective

def decide_result(server_choice, client_choice):
    if client_choice == 'rock' and server_choice == 'scissors' \
        or client_choice == 'scissors' and server_choice == 'paper' \
        or client_choice == 'paper' and server_choice == 'rock':
        return -1
    elif client_choice == 'scissors' and server_choice == 'rock' \
        or client_choice == 'paper' and server_choice == 'scissors' \
        or client_choice == 'rock' and server_choice == 'paper':

        return 1
    else:
        return 0


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

def reverse_result(result):
    if result == 1:
        return -1
    elif result == -1:
        return 1
    elif result == 0:
        return 0


def server(player, port):
    print("Server running!")
    print("Waiting for a client...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(socket.gethostname())
    server_address = (ip, port)
    sock.bind(server_address)
    print("Server address & port = ", ip, ":", port)
    sock.listen(1)
    (connection, client_address) = sock.accept()
    message = \
        'Hi! You are connected to the server. You are playing against ' \
        + player + '!'
    connection.send(message.encode())
    message_from_client = connection.recv(256)
    print(message_from_client.decode())
    server_choice = input("Please choose rock/paper/scissors: ")
    client_choice = connection.recv(16)
    client_choice = client_choice.decode()
    result = decide_result(server_choice,client_choice)
    connection.send(str(reverse_result(result)).encode())
    countdown_output()
    print_result(result)
    connection.close()
