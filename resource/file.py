import socket # importing the socket module.

HOST = "127.0.0.1" # specifying the host's address.
PORT = 65432 # specifying the port to be used in the communication between the server and the client.

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating an object that calls on the socket method from module socket.

server_socket.bind((HOST, PORT)) # using the created method to bind the host and port to the socket.

server_socket.listen() # using the created method to lisen for any incoming connection from the specified port.

conn, addr = server_socket.accept() # using the created method to accept a connection when one is established.

with conn:

	print ("connected by", addr)

	while  1:
		
		data = conn.recv(1024)

		print ("\nReceived", data, "from client!")

		print ("\nSending back data...")

		conn.sendall(b"Hello fam!")

server_socket.close()

# research the "with" function