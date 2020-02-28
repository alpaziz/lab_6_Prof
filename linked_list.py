from node import Node

class LinkedList:
	def __init__(self, size = 0, head = None, tail = None):
		self.size = size
		self.head = head
		self.tail = tail

	def getSize(self):
		return(self.size)

	def setSize(self, s):
		self.size = s

	def getHead(self):
		return(self.head)

	def setHead(self, h):
		self.head = h

	def getTail(self):
		return(self.tail)

	def setTail(self, t):
		self.tail = t

	def isEmpty(self):
		if(self.getSize() > 0):
			return(False)
		return(True)

	def addNode(self, d):
		newNode = Node(data = d)

		# Simple Case
		if(self.isEmpty()):
			self.setHead(newNode)

		else:
			self.getTail().setnextPointer(newNode) 
			# t = self.getTail()
			# t.setnextPointer(newNode)
		self.setTail(newNode)
		self.setSize(self.size + 1)

def main():
	ll = LinkedList()
	ll.addNode(1000)

	ll.addNode(2000)

	ll.addNode("The American University")

	print(ll.getTail().getData())

if __name__ == '__main__':
	main()


