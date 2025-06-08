import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hello UDP Server"
client_socket.sendto(msg.encode('utf-8'), ('127.0.0.1', 12347))

data, addr = client_socket.recvfrom(4096)
print("Server Says:")
print(data.decode('utf-8'))  # decode bytes to string for clear output

client_socket.close()
