# tcp_server

This repository contains an implementation of a TCP server and client in Python. The server is designed to receive messages from the client, respond with the uppercase version of the received message, and handle disconnections using the special message `DESCONEXION`.

## Requirements

- **Python 3**: This challenge has been developed and tested with Python 3. Make sure you have Python 3 installed on your system.

## Installation

1. **Clone the repository**:

   If you haven't cloned the repository yet, do so with the following command:

   ```bash
   git clone https://github.com/your_username/tcp_server.git

1. **Clone the repository**:

    Once you have cloned the repository, navigate into the project folder:
    ```bash
    cd tcp_server

## Running the Application

To run the server and the client, you need to open two terminals: one for the server and one for the client. You can either do this manually or use the app.py script, which will automatically open the terminals for you.

1. **Method 1: Run Automatically with app.py**: 

    From the root directory of the repository (tcp_server), execute the following command to automatically start both the server and the client in separate terminals:
    ```bash
    python3 app.py

This will open two terminals:
- Terminal 1: Runs the server.
- Terminal 1: Runs the client.

1. **Interact with the client**:

    Once the terminals are open, you will see the message:

    ```bash
        Write your message

In the client's terminal, you can type any message, and the server will respond with the message in uppercase.

Example:

Client: "hello"
Server response: "HELLO"


1. **Disconnect**:

To disconnect the client from the server, simply type:

```bash
    DESCONEXION
```

The client will disconnect, and the server will close the connection.


2. **Method 2: Run the server and de client:**: 

    Open a terminal and execute the following commands to start the server and client connection:
    ```bash
    python3 server.py
    python3 client.py
    ```
    
The client will automatically connect to the server, and you can begin interacting with it by typing messages in the client's terminal.

## Additional Notes

- Ensure that the server's port (`5000`) is not being used by another process before starting the server.
- Both the server and client need to be running simultaneously to interact with each other.
- If you wish to change the port or any other parameters, you can modify the values directly in the `server.py`, `client.py`, or `app.py` files.

