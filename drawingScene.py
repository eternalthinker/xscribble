import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import time

class drawingScene(QtGui.QGraphicsScene):
	def __init__(self, parent, startString, jid, gtalkNode):
		QtGui.QGraphicsScene.__init__(self, parent)		
		self.pointsList = [] #Encodes drawn lines as a list of points and color data
		self.splitStrings = ""
		self.mousePressFlag = False
		self.color = QtGui.QColor(0,0,0)
		self.pen = QtGui.QPen(self.color, 1, QtCore.Qt.SolidLine)
		self.stroke = 3
		self.startPoint	= QtCore.QPoint(0,0)
		self.startString = startString
		self.gtalkNode = gtalkNode
		self.jid = jid
		self.dataLimit = 12500
						
	# Supporter for mouse events - checks whether cursor is in drawing frame			
	def isinFrame(self, event):		
		if self.mousePressFlag:
			x = 0
			y = 0
			w = 320
			h = 240		
			mx = event.scenePos().x()
			my = event.scenePos().y()
			if mx > x and mx < w :
				if my > y and my < h :					
					return True					
			return False
					
	# Mouse drawing and simultaneous building of pointsList[]
			
	def mousePressEvent(self,event):		
		self.mousePressFlag = True		
		if self.isinFrame(event):
			self.startPoint = event.scenePos()
			self.pen = QtGui.QPen(self.color, self.stroke, \
			  QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)			
			self.pointsList.extend([[self.color.name(), self.stroke], self.startPoint])
			brush = QtGui.QBrush(self.color)
			pen = QtGui.QPen(QtCore.Qt.NoPen)
			d = self.stroke*1.1
			self.addEllipse(self.startPoint.x()-d/2, self.startPoint.y()-d/2, d, d, pen, brush)
		
	def mouseMoveEvent(self,event):		
		if self.isinFrame(event):			
			self.pointsList.append(event.scenePos())			
			self.addLine(self.startPoint.x(), self.startPoint.y(), \
			  event.scenePos().x(), event.scenePos().y(), self.pen)			
			self.startPoint = event.scenePos()
		elif self.mousePressFlag:
			self.mouseReleaseEvent(event)						
				
	def mouseReleaseEvent(self,event):		
		if self.mousePressFlag: #self.isinFrame(event):			
			self.mousePressFlag = False
			#print self.pointsListEncode()
			pointsString = self.pointsListEncode()
			dataLength = len(pointsString)
			print dataLength
			
			if dataLength > self.dataLimit:
				limit = self.dataLimit
				pointsString = pointsString[len(self.startString):]
				for i in range(dataLength/limit):
					self.gtalkNode.sendHandler(self.jid, \
					 self.startString + pointsString[i*limit:(i+1)*limit] + '>')
					time.sleep(1) #;print "Part", i+1
				self.gtalkNode.sendHandler(self.jid, \
					 self.startString + pointsString[(i+1)*limit:] + '<>') 
				#print "Part", i+2				
			else:
				self.gtalkNode.sendHandler(self.jid, pointsString)
							
			self.pointsList = []	
			
		
	# pointsList[] to pointsString conversion				
	def pointsListEncode(self):
		pointsList = self.pointsList[:]	#;print pointsList				
		pointsString = ""
		infoList = pointsList.pop(0)
		pointsString += self.startString + str(infoList[0]) + ';' + str(infoList[1]) + ','
		for point in pointsList:			
			pointsString += str(int( point.x() )) + ':' + str(int( point.y() )) + '|'
		#print pointsString
		return pointsString		
	
	# pointsString to pointsList[] conversion			
	def pointsStringDecode(self, pointsString):
		# pointsString have an extra '|' at end
                # "~aaa~bbb".split('~') = ['', 'aaaa', 'bbb'] 
                # "aaa~bbb".split('~') = ['aaaa', 'bbb']
		components = pointsString[len(self.startString):-1].split(',')
		infoString = components.pop(0).split(';')
		return [ [QtGui.QColor(infoString[0]), int(infoString[1])] ] + \
		  [apply( QtCore.QPoint, [float(offset) for offset in newpoint.split(':')] ) \
		    for newpoint in components[0].split('|')]	
	
	# Draw actual lines based on a given pointsString after converting it to pointsList[]	    
	def drawPoints(self, pointsString):
	
		if pointsString.endswith('>'):
			if pointsString.endswith('<>'):
				self.splitStrings += pointsString[len(self.startString):-2]
				pointsString = self.startString + self.splitStrings
				self.splitStrings = ""
			else:
				self.splitStrings += pointsString[len(self.startString):-1]
				return False
					
		pointsList = self.pointsStringDecode(pointsString)
		infoList = pointsList.pop(0)
		color, stroke = infoList[0], infoList[1]
		pen = QtGui.QPen(color, stroke, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
		startPoint = pointsList.pop(0)
		for point in pointsList:						
			self.addLine(startPoint.x(), startPoint.y(), point.x(), point.y(), pen)  
			startPoint = point	
				
	# Clear the current scene			
	def clearPoints(self):
		self.clear()		
		

