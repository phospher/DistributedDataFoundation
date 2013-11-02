PROTOCOL_MESSAGE_PREPARE =  'PRPARE'
PROTOCOL_MESSAGE_ABORT = 'ABORT'
PROTOCOL_MESSAGE_COMMIT = 'COMMIT'
PROTOCOL_MESSAGE_ACKCOMMIT = 'ACK-COMMIT'

def communicate(client, message, answerRecords, timeout, socket):
	ip,port = client
    if ip in answerRecords:
    	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	conn.connect(client)
    	conn.send(message)
    	conn.settimeout(timeout)
    	message = conn.recv(1024)
    	conn.close()
    	return message


class TransatonCommitCoordinator(object):
	"""docstring for TransatonCommitHelper"""
	def __init__(self, socket):
		self.socket = socket

	def commit(self, clientList):
		

