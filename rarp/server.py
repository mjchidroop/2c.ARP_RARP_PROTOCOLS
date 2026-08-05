import socket

rarp_table = {
    "AA:BB:CC:DD:EE:01": "192.168.1.1",
    "AA:BB:CC:DD:EE:02": "192.168.1.2",
    "AA:BB:CC:DD:EE:03": "192.168.1.3",
    "AA:BB:CC:DD:EE:04": "192.168.1.4",
    "AA:BB:CC:DD:EE:05": "192.168.1.5"
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9001))
server.listen(1)

print("RARP Server running on port 9001")
print("Waiting for client...")

client, addr = server.accept()
print("Client connected from:", addr)

while True:
    mac = client.recv(1024).decode()
    
    if not mac:
        break
    
    print("Requested MAC:", mac)
    
    if mac in rarp_table:
        ip = rarp_table[mac]
        print("IP found:", ip)
    else:
        ip = "MAC not found in RARP table"
        print("IP not found")
    
    client.send(ip.encode())

client.close()
server.close()