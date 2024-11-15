import socket

PORT = 5000
HOST = "localhost"
CLOSE_MESSAGE = "DESCONEXION"

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

try:
    server_socket.bind((HOST, PORT))
    server_socket.listen(3)
    print(f"Server up in {HOST}:{PORT}")

    while True:
        server_conn, client_addr = server_socket.accept()
        print(f"Connection stablished with: {client_addr}")

        try:
            while True:
                message = server_conn.recv(1024).decode("utf-8")
                if not message:
                    break

                if message == CLOSE_MESSAGE:
                    print(f"client {client_addr} disconnected.")
                    server_conn.close()
                    break

                print(f"Message received: {message}")
                server_conn.send(message.upper().encode("utf-8")[:1024])

        except Exception as e:
            print(f"Error stablishing connection with {client_addr}: {e}")
            server_conn.close()

except Exception as exc:
    print(f"Server error: {exc}")

except KeyboardInterrupt as ki:
    print("Server closed manually", ki)
    server_conn.close()
    server_socket.close()

finally:
    print("Server closed.")
