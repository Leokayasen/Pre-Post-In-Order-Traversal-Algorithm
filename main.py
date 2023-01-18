class Node:

	def __init__(self, data):

		self.left = None
		self.right = None
		self.data = data

	#insert node
	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	#Print Tree
	def printTree(self):
		if self.left:
			self.left.printTree()
			print(self.data)
		if self.right:
			self.right.printTree()
			print(self.data)

	#In order Traversal
	#Left > Root > Right
	def inOrderTraversal(self, root):
		res = [] #Empty List
		if root:  #Terminating Condition
			res = self.inOrderTraversal(root.left)
			res.append(root.data)
			res = res + self.inOrderTraversal(root.right)
		return res #res becomes a global list

	#Pre Order
	#Root > Left > Right
	def preOrderTraversal(self, root):
		res = [] #Empty List
		if root:  #Terminating Condition
			res.append(root.data)
			res = res + self.preOrderTraversal(root.left)
			res = res + self.preOrderTraversal(root.right)
		return res #res becomes a global list

	#Post Order
	#Left > Right > Root
	def postOrderTraversal(self, root):
		res = [] #Empty List
		if root:  #Terminating Condition
			res = self.postOrderTraversal(root.left)
			res = res + self.postOrderTraversal(root.right)
			res.append(root.data)
		return res #res becomes a global list

	


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inOrderTraversal(root), "- In Order Traversal")
print(root.preOrderTraversal(root), "- Pre Order Traversal")
print(root.postOrderTraversal(root),"- Post Order Traversal")
