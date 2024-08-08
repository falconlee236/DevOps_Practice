import socket
import time
import random
import json

host = 'localhost'
port = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Listening on {host}:{port}...")

client_socket, addr = server_socket.accept()
print(f"Connection from {addr} has been established.")

categories = list(range(1, 6)) 
num_records = 100  

try:
    for _ in range(num_records):
        data = {
            "product_id": random.randint(1000, 9999),
            "category_id": random.choice(categories),
            "view_count": random.randint(0, 1000),
            "purchase_count": random.randint(0, 500),
            "rating": round(random.uniform(1.0, 5.0), 1)
        }
        client_socket.sendall((json.dumps(data) + '\n').encode('utf-8'))
        time.sleep(1) 
finally:
    client_socket.close()
    server_socket.close()
