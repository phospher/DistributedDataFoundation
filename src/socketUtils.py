import socket

def communicate(client, message, timeout):
	ip,port = client
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(client)
    conn.send(message)
    conn.settimeout(timeout)
    message = conn.recv(1024)
    conn.close()
    return message