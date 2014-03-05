from PyQt4 import QtCore
import warnings
with warnings.catch_warnings():
	warnings.simplefilter("ignore", category=DeprecationWarning)
        import xmpp	

class GtalkModule(QtCore.QThread):
	def __init__(self, parent, user, password):
		QtCore.QThread.__init__(self, parent)
		self.logout = False
		self.appResource = 'xScribble'
		self.user = str(user)
		self.password = str(password)
		
	def run(self):
		if self.connect():
			self.logout = False
		else:
			self.logout = True
			
		while not self.logout:
			self.connection.Process(1)
			
		if self.connection.isConnected():
            		self.connection.disconnect()
		self.emit(QtCore.SIGNAL("connected"), False)	
						
	def logout():
		self.logout = True		
			
	def connect(self):
		server = "gmail.com"
		jid = xmpp.JID(self.user)
		self.connection = xmpp.Client(server, debug=[])
		print "Connecting.."	
		server = ('talk.google.com', 5223)	
		if not self.connection.connect(server):
			self.emit(QtCore.SIGNAL("error"), "<b>Connection Error!</b><br>Check your internet connection")
			return False
		print "Connected!"
			
		result = self.connection.auth(jid.getNode(), self.password, self.appResource)
		if not result:
			self.emit(QtCore.SIGNAL("error"), "<b>Authentication Error!</b><br>Check your username and password")
			return False
			
		self.connection.RegisterHandler('message', self.receiveHandler)
		self.connection.RegisterHandler('presence', self.presenceHandler)
		self.connection.sendInitPresence()
		self.setStatus("Scribbling in Colors")
		self.roster = self.connection.getRoster()
		self.emit(QtCore.SIGNAL("connected"), True)
		return True
	
	def receiveHandler(self, connectObject, messageNode):
		self.emit(QtCore.SIGNAL("inmessage"), messageNode.getFrom(), messageNode.getBody())
				
	def sendHandler(self, toJid, sendString):
		if len(sendString) > 12500:
                        self.emit(QtCore.SIGNAL("error"), "<b>Data limit exceeded!</b><br>The text is too long")
                        return False			
		self.connection.send(xmpp.Message(xmpp.JID(toJid), sendString)) 
		
	def presenceHandler(self, connectObject, presenceNode):
		if presenceNode:
			try:	
				jid = presenceNode.getFrom()
				if presenceNode.getType() == "unavailable":
					offline = True
				else:
					offline = False		
				self.emit(QtCore.SIGNAL("inpresence"), jid, offline, presenceNode.getStatus()) 
			except:
				pass	
		
	def setStatus(self, status):
		pres = xmpp.Presence(priority=5, show='dnd',status = status)		
		self.connection.send(pres)	
		
	def getName(self, jid):
        	return self.roster.getName(str(jid))	
			
		
