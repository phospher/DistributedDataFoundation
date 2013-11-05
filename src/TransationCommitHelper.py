import threading;
import thread;

PROTOCOL_MESSAGE_PREPARE =  'PREPARE'
PROTOCOL_MESSAGE_ABORT = 'ABORT'
PROTOCOL_MESSAGE_COMMIT = 'COMMIT'
PROTOCOL_MESSAGE_ACKCOMMIT = 'ACK-COMMIT'
TIME_OUT = 5000

class TransatonCommitCoordinator(object):
	"""docstring for TransatonCommitHelper"""
	def __init__(self, communicateFunc):
		self.communicateFunc = communicateFunc
		self.condition = threading.Condition()
	
	def __checkAllReply(clientReply):
	    i = 0
	    for key in clientReply:
	        i += 1 if not clientReply[key] else 0
	    return True if i == len(clientReply.keys()) else False

	def commit(self, clientList):
	    self.__pharseOneCommit(clientList)
	
	def __pharseOneCommit(self, clientList):
	    clientReplay = {};
	    for client in clientList:
	        clientReplay[client[0]] = None
	    self.condiction.acquire()
		for client in clientList:
		    thread.start_new_thread(self.__sendPrepare, (client, clientReplay))
		self.condiction.wait()
		self.condiction.release()
		
	def __sendPrepare(self, client, clientReply):
	    try:
	       reply = self.communicateFunc(client, PROTOCOL_MESSAGE_PREPARE, TIME_OUT)
	    except:
	        reply = PROTOCOL_MESSAGE_ABORT
	    clientReply[ip] = reply
	    if __checkAllReply(clientReply):
	        condition.acquire()
	        condition.notify()
	        condition.release()
	        