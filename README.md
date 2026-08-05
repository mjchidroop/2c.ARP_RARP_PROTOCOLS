# 2c.SIMULATING ARP /RARP PROTOCOLS
## AIM
To write a python program for simulating ARP protocols using TCP.
## ALGORITHM:
## Client:
1. Start the program
2. Using socket connection is established between client and server.
3. Get the IP address to be converted into MAC address.
4. Send this IP address to server.
5. Server returns the MAC address to client.
## Server:
1. Start the program
2. Accept the socket which is created by the client.
3. Server maintains the table in which IP and corresponding MAC addresses are
stored.
4. Read the IP address which is send by the client.
5. Map the IP address with its MAC address and return the MAC address to client.
P
## PROGRAM - ARP
## ARP (Address Resolution Protocol) Implementation

| **ARP Client (client.py)** | **ARP Server (server.py)** |
|----------------------------|----------------------------|
| `import socket` <br><br> `client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` <br> `client.connect(("localhost", 9000))` <br><br> `print("Connected to ARP Server")` <br><br> `ip = input("Enter IP address: ")` <br><br> `client.send(ip.encode())` <br><br> `mac = client.recv(1024).decode()` <br> `print("MAC Address:", mac)` <br><br> `client.close()` | `import socket` <br><br> `arp_table = {` <br> `    "192.168.1.1": "AA:BB:CC:DD:EE:01",` <br> `    "192.168.1.2": "AA:BB:CC:DD:EE:02",` <br> `    "192.168.1.3": "AA:BB:CC:DD:EE:03",` <br> `    "192.168.1.4": "AA:BB:CC:DD:EE:04",` <br> `    "192.168.1.5": "AA:BB:CC:DD:EE:05"` <br> `}` <br><br> `server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` <br> `server.bind(("localhost", 9000))` <br> `server.listen(1)` <br><br> `print("ARP Server running on port 9000")` <br> `print("Waiting for client...")` <br><br> `client, addr = server.accept()` <br> `print("Client connected from:", addr)` <br><br> `while True:` <br> `    ip = client.recv(1024).decode()` <br> `    if not ip:` <br> `        break` <br> `    print("Requested IP:", ip)` <br> `    if ip in arp_table:` <br> `        mac = arp_table[ip]` <br> `        print("MAC found:", mac)` <br> `    else:` <br> `        mac = "IP not found in ARP table"` <br> `        print("MAC not found")` <br> `    client.send(mac.encode())` <br><br> `client.close()` <br> `server.close()` |

---

### ARP Table

| **IP Address** | **MAC Address** |
|----------------|-----------------|
| 192.168.1.1 | AA:BB:CC:DD:EE:01 |
| 192.168.1.2 | AA:BB:CC:DD:EE:02 |
| 192.168.1.3 | AA:BB:CC:DD:EE:03 |
| 192.168.1.4 | AA:BB:CC:DD:EE:04 |
| 192.168.1.5 | AA:BB:CC:DD:EE:05 |
## OUTPUT - ARP
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/a42bc314-f644-4dad-a1a1-8abb5eb2ce49" />

## PROGRAM - RARP
## RARP (Reverse Address Resolution Protocol) Implementation

| **RARP Client (client.py)** | **RARP Server (server.py)** |
|-----------------------------|-----------------------------|
| `import socket` <br><br> `client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` <br> `client.connect(("localhost", 9001))` <br><br> `print("Connected to RARP Server")` <br><br> `mac = input("Enter MAC address: ")` <br><br> `client.send(mac.encode())` <br><br> `ip = client.recv(1024).decode()` <br> `print("IP Address:", ip)` <br><br> `client.close()` | `import socket` <br><br> `rarp_table = {` <br> `    "AA:BB:CC:DD:EE:01": "192.168.1.1",` <br> `    "AA:BB:CC:DD:EE:02": "192.168.1.2",` <br> `    "AA:BB:CC:DD:EE:03": "192.168.1.3",` <br> `    "AA:BB:CC:DD:EE:04": "192.168.1.4",` <br> `    "AA:BB:CC:DD:EE:05": "192.168.1.5"` <br> `}` <br><br> `server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` <br> `server.bind(("localhost", 9001))` <br> `server.listen(1)` <br><br> `print("RARP Server running on port 9001")` <br> `print("Waiting for client...")` <br><br> `client, addr = server.accept()` <br> `print("Client connected from:", addr)` <br><br> `while True:` <br> `    mac = client.recv(1024).decode()` <br> `    if not mac:` <br> `        break` <br> `    print("Requested MAC:", mac)` <br> `    if mac in rarp_table:` <br> `        ip = rarp_table[mac]` <br> `        print("IP found:", ip)` <br> `    else:` <br> `        ip = "MAC not found in RARP table"` <br> `        print("IP not found")` <br> `    client.send(ip.encode())` <br><br> `client.close()` <br> `server.close()` |

---

### RARP Table

| **MAC Address** | **IP Address** |
|-----------------|----------------|
| AA:BB:CC:DD:EE:01 | 192.168.1.1 |
| AA:BB:CC:DD:EE:02 | 192.168.1.2 |
| AA:BB:CC:DD:EE:03 | 192.168.1.3 |
| AA:BB:CC:DD:EE:04 | 192.168.1.4 |
| AA:BB:CC:DD:EE:05 | 192.168.1.5 |
## OUTPUT -RARP
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/5058d440-73ad-44df-aa67-af5ffcbe8225" />

## RESULT
Thus, the python program for simulating ARP protocols using TCP was successfully 
executed.
