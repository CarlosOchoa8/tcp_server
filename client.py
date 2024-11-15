import socket

SERVER_ADD = "localhost"
SERVER_PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((SERVER_ADD, SERVER_PORT))
    print(f"Connecting to {SERVER_ADD}:{SERVER_PORT}")

    while True:
        client_socket.send(input("Write your message: \n").encode("utf-8"))

        try:
            response = client_socket.recv(1024)
            if not response:
                print("Connection closed by server.")
                break
            print("Response received:", response.decode("utf-8"))

        except (ConnectionResetError, socket.error) as e:
            print(f"Connection error: {e}")
            break

except Exception as exc:
    print(f"Connection error: {exc}")

except KeyboardInterrupt as ki:
    print("Client closed manually", ki)
    client_socket.send("DESCONEXION".encode("utf-8"))

finally:
    client_socket.close()
    print("Server closed.")
