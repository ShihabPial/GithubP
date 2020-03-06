class Node:
	
	def __init__(self, data, nextP = None, prevP = None):
		self.data = data
		self.nextP = nextP
		self.prevP = prevP

	#Getter Methods
	def getData(self):
		return self.data

	def getNextPointer(self):
		return self.nextP

	def getPreviousPointer(self):
		return self.prevP

	#Setter Methods
	def setData(self, newD):
		self.data = newD

	def setNextPointer(self, newP):
		self.nextP = newP

	def setPreviousPointer(self, newP):
		self.prevP = newP

