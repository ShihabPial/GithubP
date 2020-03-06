from myNode import Node
class Queue:
	def __init__(self, size = 0, front = None, end = None):
		self.size = size
		self.front = front
		self.end = end

	def enQueue(self, newData):
		newNode = Node(newData)
		if(self.size == 0):
			self.front = newNode
		else:	
			newNode.setNextPointer(self.end)
			self.end.setPreviousPointer(newNode)

		self.end = newNode
		self.size += 1

	def deQueue(self):
		if(self.size > 0):
			old_front = self.front
			if(self.size > 1):
				self.front = self.front.getPreviousPointer()
				self.front.setNextPointer(None)
				old_front.setPreviousPointer(None)
			self.size -= 1

		else:
			print("Queue is empty")

	def printQueue(self):
		currentNode = self.front

		while(currentNode):
			print(currentNode.getData())
			currentNode = currentNode.getNextPointer()

def main():

	q = Queue()
	q.enQueue(1)
	q.enQueue(5)
	q.enQueue("AU")
	#q.enQueue("Long Island")
	#q.enQueue("NY")

	#print("List: ",q.printQueue())
	print(q.size)

	q.deQueue()
	q.deQueue()
	q.deQueue()
	print(q.size)

	#print(q.size)

	
	#print("List: ", q.printQueue())

	#print(q.front.getData())
	#print(q.end.getData())

if __name__ == '__main__':
	main()