import threading;
import thread;

PROTOCOL_MESSAGE_PREPARE =  'PREPARE'
PROTOCOL_MESSAGE_ABORT = 'ABORT'
PROTOCOL_MESSAGE_COMMIT = 'COMMIT'
PROTOCOL_MESSAGE_ROLLBACK = 'ROLLBACK'
PROTOCOL_MESSAGE_ACKCOMMIT = 'ACK-COMMIT'
PROTOCOL_MESSAGE_PREPARED = 'PREPARED'
TIME_OUT = 5000

class TransatonCommitCoordinator(object):
	"""docstring for TransatonCommitHelper"""
	def __init__(self, communicateFunc):
		self.communicateFunc = communicateFunc
		self.condition = threading.Condition()
	
	def __checkAllReply(self, clientReply):
	    i = 0
	    for key in clientReply:
	        i += 1 if not clientReply[key] else 0
	    return True if i == len(clientReply.keys()) else False

	def commit(self, clientList):
	    self.__pharseOneCommit(clientList)
	
	def __pharseOneCommit(self, clientList):
	    pharseOneReplay = {};
	    for client in clientList:
	        pharseOneReplay[client] = None
	    self.condiction.acquire()
		for client in clientList:
		    thread.start_new_thread(self.__sendPrepare, (client, clientReplay))
		self.condiction.wait()
		self.condiction.release()
	
	def __checkAllRepared(self, clientReplay):
	    i = 0
	    for key in clientReplay:
	        i += 1 if clientReply[key] == PROTOCOL_MESSAGE_PREPARED else 0
	    return True if i == len(clientReply.keys()) else False
	 
	def __pharseTwoCommit(self, clientList, pharseOneReplay):
	    pass
	
	def __sendMessageClient(self, client, message, exceptMsg, clientReply):
	    try:
	       reply = self.communicateFunc(client, message, TIME_OUT)
	    except:
	        reply = exceptMsg
	    clientReply[client] = reply
	    if self.__checkAllReply(clientReply):
	        condition.acquire()
	        condition.notify()
	        condition.release()
		
	def __sendPrepare(self, client, clientReply):
	    self.__sendMessageClient(client, PROTOCOL_MESSAGE_PREPARE, PROTOCOL_MESSAGE_ABORT, clientReply)
	 
	def __sendPhaseTwoMessage(self, client, message, clientReplay):
	    self.__sendMessageClient(client, message, None, clientReplay)
	        
	        