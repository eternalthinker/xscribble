from PyQt4 import QtGui
from PyQt4 import QtCore
from ui.ui_buddyWindow import Ui_BuddyWindow
from ui import xscribble_rc
from drawingScene import drawingScene

class BuddyWindow(QtGui.QWidget, Ui_BuddyWindow):
	def __init__(self, parent, jid, name, gtalkNode, scribble):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.setWindowIcon(QtGui.QIcon(":/images/chat" + ("On" if scribble else "Off") + ".png"))		    
		self.setWindowTitle("Chat with " + name)
		
		self.gtalkNode = gtalkNode
		self.jid = jid
		self.name = name
		self.startString = '~^%+'
		self.clearString = '~^%-'
		self.chatEdit.setFocus()
		self.scribble = scribble	
		
		self.scene = drawingScene(self, self.startString, self.jid, self.gtalkNode)        	
        	self.scene.setSceneRect(0,0,self.frame.width(),self.frame.height())
        	self.frame.setScene(self.scene)			
		self.frame.setHorizontalScrollBarPolicy ( QtCore.Qt.ScrollBarAlwaysOff )
		self.frame.setVerticalScrollBarPolicy ( QtCore.Qt.ScrollBarAlwaysOff )			
		self.frame.setRenderHints( QtGui.QPainter.Antialiasing | QtGui.QPainter.HighQualityAntialiasing)
		self.setMouseTracking(True)
		
		self.penBackup = None, None
			
		if not self.scribble:
			self.drawingareaWidget.hide()
			self.setGeometry(200, 200, 376, 240)	
		else:
			self.errorLabel.hide()						
			
	@QtCore.pyqtSignature("")
	def on_chatEdit_returnPressed(self):
		chatString = self.chatEdit.text()
		if not chatString: return False
		self.chatEdit.clear()		
		chat = """<b><font color='black'>Me: </font></b><font color='black'>%s</font>""" % (chatString)
		self.chatBrowser.append(chat)
		self.gtalkNode.sendHandler(self.jid, chatString)
		
	def receiveMessage(self, messageString):
		if not messageString: return False
		if messageString.startswith(self.startString):
			self.scene.drawPoints(messageString)
		elif messageString == self.clearString:
			self.scene.clearPoints()	
		else:
			chat = 	"""<b><font color='darkred'>%s: </font></b><font color='black'>%s</font>""" % (self.name, messageString)
			self.chatBrowser.append(chat)
			
	@QtCore.pyqtSignature("")	
	def on_colorButton_clicked(self):		
		col = QtGui.QColorDialog.getColor()
		if col.isValid():
			self.scene.color = col
			self.colorShowLabel.setStyleSheet("QLabel { background-color: %s }" % col.name())		
			
	@QtCore.pyqtSignature("")	
	def on_clearButton_clicked(self):
		self.scene.clearPoints()		
		self.gtalkNode.sendHandler(self.jid, self.clearString)
		
	@QtCore.pyqtSignature("int")
	def on_strokeSlider_valueChanged(self, stroke):		
		self.scene.stroke = 2*stroke + 1
		self.strokeShowLabel.setText(str(stroke+1))
		
	@QtCore.pyqtSignature("")	
	def on_strokeButton_clicked(self):
		if self.strokeButton.isChecked():
			self.scene.color, self.scene.stroke = self.penBackup
			self.eraseButton.setChecked(False)
			self.colorButton.setEnabled(True)					
		else:
			self.strokeButton.setChecked(True)
			
	@QtCore.pyqtSignature("")	
	def on_eraseButton_clicked(self):
		if self.eraseButton.isChecked():
			self.penBackup = self.scene.color, self.scene.stroke
			self.scene.color, self.scene.stroke = QtGui.QColor(255,255,255), 11
			self.strokeButton.setChecked(False)
			self.colorButton.setEnabled(False)			
		else:
			self.eraseButton.setChecked(True)
			
	@QtCore.pyqtSignature("")	
	def on_saveButton_clicked(self):
		filename = QtGui.QFileDialog.getSaveFileName(self, 'Save scribble', '/home', 'PNG Image(*.png)')
        	#print filename
        	if filename:
        		image = QtGui.QImage(320, 240, QtGui.QImage.Format_RGB32)
        		image.fill(QtGui.QColor(255,255,255).rgb())
        		painter = QtGui.QPainter(image)
        		painter.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing|\
        		  QtGui.QPainter.SmoothPixmapTransform)        		
        		self.frame.render(painter) 
        		painter.end() 
        		image.save(str(filename).replace('png','')+'.png', "PNG")
				
if __name__ == "__main__":
	import sys
    	app = QtGui.QApplication(sys.argv)
   	window = BuddyWindow(None, 'et@gmail.com', 'Rahul', None, True)
    	window.show()
    	sys.exit(app.exec_())
    
