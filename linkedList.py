class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node=cur_node.next

	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last_node = self.head
		while  last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def prepend(self, data):
		new_node = Node(data)

		new_node.next = self.head
		self.head = new_node

	def insert_after_node(self, previous_node, data):
		if previous_node:
			print("Previous node does not exist")
			return
		new_node = Node(data)
		new_node.next = previous_node.next
		previous_node.next = new_node
#deleting node by value -_-
	def delete_node(self, key):
		curr_node = self.head
		if curr_node and curr_node.data == key:
			self.head = curr_node.next
			curr_node.next = None
			return
		prev = None
		while curr_node and curr_node.data != key:
			prev = curr_node
			curr_node = curr_node.next

		if curr_node is None:
			return
		prev.next = curr_node.next
		curr_node = None

	# deleting a node using a position instead of value
	def delete_node_at_pos(self, pos):
		curr_node = self.head
		if pos ==0:
			self.head = curr_node.next
			curr_node.next = None
			return
		prev = None
		count =0
		while curr_node and count!= pos:
			prev = curr_node
			curr_node = curr_node.next
			count +=1
		if curr_node is None:
			return
		prev.next = curr_node.next
		curr_node = None
	



	


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")

llist.delete_node_at_pos(0)
# llist.delete_node("E")
# llist.insert_after_node(llist.head.next, "D")

llist.print_list()		
		