import socket

arp_table = {
    "192.168.1.1": "AA:BB:CC:DD:EE:01",
    "192.168.1.2": "AA:BB:CC:DD:EE:02",
    "192.168.1.3": "AA:BB:CC:DD:EE:03",
    "192.168.1.4": "AA:BB:CC:DD:EE:04",
    "192.168.1.5": "AA:BB:CC:DD:EE:05"
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9000))
server.listen(1)

print("ARP Server running on port 9000")
print("Waiting for client...")

client, addr = server.accept()
print("Client connected from:", addr)

while True:
    ip = client.recv(1024).decode()
    
    if not ip:
        break
    
    print("Requested IP:", ip)
    
    if ip in arp_table:
        mac = arp_table[ip]
        print("MAC found:", mac)
    else:
        mac = "IP not found in ARP table"
        print("MAC not found")
    
    client.send(mac.encode())

client.close()
server.close()