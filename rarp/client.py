import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9001))

print("Connected to RARP Server")

mac = input("Enter MAC address: ")

client.send(mac.encode())

ip = client.recv(1024).decode()
print("IP Address:", ip)

client.close()