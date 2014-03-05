#!/usr/bin/env python

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from ui.ui_mainWindow import Ui_MainWindow
from ui.ui_info import Ui_Info
from ui import xscribble_rc
from buddyWindow import BuddyWindow
from gtalkModule import GtalkModule

class Buddy(QtGui.QListWidgetItem):
	def __init__(self, parent, jid, name, status, scribble, gtalkNode):
		QtGui.QListWidgetItem.__init__(self, name, parent)
		self.buddyWindow = None		
		self.jid = jid
		self.scribble = scribble
		self.status = status
		self.gtalkNode = gtalkNode
		self.name = name
		self.setSizeHint(QtCore.QSize(0, 30))		
		self.setIcon(QtGui.QIcon(":/images/scribble" + ("On" if scribble else "Off") + ".png"))
		self.setToolTip("<font size='2'><b>%s</b><br>%s</font>" % (str(jid).split('/')[0], status) )		    
		
	def createBuddyDialog(self):
		if not self.buddyWindow:		    
		    self.buddyWindow = BuddyWindow(None, self.jid, self.name, self.gtalkNode, self.scribble)		    
		self.buddyWindow.show()
		self.buddyWindow.raise_()

	def receiveMessage(self, messageString):
		self.createBuddyDialog()
		self.buddyWindow.receiveMessage(messageString)    	
        	
class Info(QtGui.QDialog, Ui_Info):
	def __init__(self, parent):
		QtGui.QDialog.__init__(self, parent)
		self.setupUi(self)

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)				
		self.clientWidget.hide()
		self.actionLogout.setEnabled(False)		
		self.buddies = []
		self.connect(self.buddyList, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.sendMessage)
		self.info = Info(self)
					
	@QtCore.pyqtSignature("")	
	def on_loginButton_clicked(self):
		self.user = self.usernameEdit.text().replace('@gmail.com', '') + '@gmail.com' 
		self.password = self.passwordEdit.text()
		if self.user == '@gmail.com' or not self.password:
			self.showError("Enter username and password!")
			return False
		self.loginWidget.hide()
		self.statusbar.showMessage("Logging in..")
		self.gtalkNode = GtalkModule(None, self.user, self.password)
		self.gtalkNode.start()
		self.connect(self.gtalkNode, QtCore.SIGNAL("connected"), self.setWindowDisplay)
		self.connect(self.gtalkNode, QtCore.SIGNAL("error"), self.showError)
		self.connect(self.gtalkNode, QtCore.SIGNAL("inpresence"), self.addBuddy)
		self.connect(self.gtalkNode, QtCore.SIGNAL("inmessage"), self.receiveMessage)	
		
	@QtCore.pyqtSignature("")	
	def on_setStatusButton_clicked(self):		
		status = self.statusEdit.text()
		self.gtalkNode.setStatus(str(status))
		
	def setWindowDisplay(self, connected):
		if connected:
			name = self.gtalkNode.getName(self.user) 
			if not name: name = self.user.replace('@gmail.com', '') 
			self.usernameLabel.setText(name)
			self.user += '@gmail.com'
			self.loginWidget.hide()			
			self.clientWidget.show()
			self.statusbar.showMessage("Logged in")
			self.actionLogout.setEnabled(True)
		else:
			self.loginWidget.show()
			self.clientWidget.hide()
			self.statusbar.showMessage("Logged out")
			self.actionLogout.setEnabled(False)	
			
	def showError(self, errorString):
		QtGui.QMessageBox.critical(self, "Error", errorString)
		
	def stripJid(self, jid):		
		bareid = jid.getStripped()
		resource = jid.getResource()
		scribble = str(resource).startswith('xScribble') #;print bareid, '#', resource	
		return  bareid, scribble				
	
	def addBuddy(self, jid, offline, status):
		bareid, scribble = self.stripJid(jid)
		if not scribble: jid = bareid
		if bareid == self.user: return False
		if jid not in self.buddies:
			self.buddies.append(str(jid))			
			name = None
			try:
				name = self.gtalkNode.getName(bareid)
			except:
				pass
			if not name: name = bareid.replace('@gmail.com', '')			
			buddy = Buddy(self.buddyList, jid, name, status, scribble, self.gtalkNode)
			self.buddyList.addItem(buddy)
		elif offline:
			index = self.buddies.index(str(jid))
			self.buddies.pop(index)
			buddy = self.buddyList.takeItem(index)
			buddy = None
						
	def receiveMessage(self, jid, messageString):
		bareid, scribble = self.stripJid(jid)
		if jid not in self.buddies:
			if bareid not in self.buddies:  
				self.addBuddy(jid, True, "")
		if not scribble: jid = bareid
		index = self.buddies.index(jid)
		self.buddyList.item(index).receiveMessage(messageString)
		
	def sendMessage(self, buddy):
		buddy.createBuddyDialog()
		
	@QtCore.pyqtSignature("")	
	def on_actionAbout_activated(self):		
		self.info.show()
		
	@QtCore.pyqtSignature("")	
	def on_actionLogout_activated(self):
		self.setWindowDisplay(False)
		self.gtalkNode.logout = True		
		self.gtalkNode = None	
		self.buddyList.clear()
		self.buddies = []
		
app = QtGui.QApplication(sys.argv)
xScribble = MainWindow()
xScribble.show()
app.exec_()		
			
			
