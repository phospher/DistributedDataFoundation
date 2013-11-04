PROTOCOL_MESSAGE_PREPARE =  'PRPARE'
PROTOCOL_MESSAGE_ABORT = 'ABORT'
PROTOCOL_MESSAGE_COMMIT = 'COMMIT'
PROTOCOL_MESSAGE_ACKCOMMIT = 'ACK-COMMIT'

class TransatonCommitCoordinator(object):
	"""docstring for TransatonCommitHelper"""
	def __init__(self, communicateFunc):
		self.communicateFunc = communicateFunc

	def commit(self, clientList):
		pass