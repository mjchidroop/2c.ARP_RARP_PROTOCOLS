import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9000))

print("Connected to ARP Server")

ip = input("Enter IP address: ")

client.send(ip.encode())

mac = client.recv(1024).decode()
print("MAC Address:", mac)

client.close()