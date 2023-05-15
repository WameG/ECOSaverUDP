from socket import *
import requests
import json

serverPort = 3520
serverSocket = socket(AF_INET, SOCK_DGRAM)

api_url = "https://ecosaver20230509124002.azurewebsites.net/api/Weather"
headers = {'Content-type': 'application/json'}

serverAddress = ('', serverPort)

serverSocket.bind(serverAddress)

print("Serveren er klar til at modtage temperatur og fugtighed data")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)

    response = requests.post(api_url, data=message.decode(), headers=headers)

    print(message.decode())
    print(response)