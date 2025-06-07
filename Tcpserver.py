import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 12346))
server_socket.listen(5)

# Set a timeout so accept() doesn't block forever
server_socket.settimeout(1.0)  # 1 second

print("Server is running...")

try:
    while True:
        try:
            print("Server waiting for connection")
            client_socket, addr = server_socket.accept()
            print("Client connected from", addr)

            client_socket.settimeout(1.0)  # Set timeout for recv()

            while True:
                try:
                    data = client_socket.recv(1024)
                    if not data or data.decode('utf-8').strip() == 'END':
                        break
                    print("Received from client:", data.decode("utf-8"))
                    client_socket.send(b"Hey client")
                except socket.timeout:
                    continue  # Wait for next message or Ctrl+C

            client_socket.close()
            print("Client disconnected\n")

        except socket.timeout:
            continue  # Wait for next connection or Ctrl+C

except KeyboardInterrupt:
    print("\nServer shutting down by Ctrl+C...")

finally:
    server_socket.close()
    print("Socket closed.")
