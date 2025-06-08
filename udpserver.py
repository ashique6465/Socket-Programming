import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("127.0.0.1", 12347))
sock.settimeout(1)  # 1 second timeout to allow interrupt checking

print("UDP server listening on 127.0.0.1:12347")

try:
    while True:
        try:
            data, addr = sock.recvfrom(4096)
            print("Received from {}: {}".format(addr, data.decode('utf-8')))
            message = "Hello I am UDP Server".encode('utf-8')
            sock.sendto(message, addr)
        except socket.timeout:
            # This just allows to loop again and check for KeyboardInterrupt
            continue

except KeyboardInterrupt:
    print("\nServer stopped by user (Ctrl+C)")

finally:
    sock.close()
