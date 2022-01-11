import socket

serverName = '127.0.0.1'
serverPort = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((serverName,serverPort))
sentence = input("Enter file name: ")

client_socket.send(sentence.encode())
filecontents = client_socket.recv(1024).decode()
print ('From Server:\n', filecontents)
client_socket.close()