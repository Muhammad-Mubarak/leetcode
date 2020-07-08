from length_of_linked_list import len_iterative

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



	# number of nodes in linked list recursive approach
	def len_recursive(self, node):
		if node is None:
			return 0
		return 1+ self.len_recursive(node.next)	

	def reverse_iterative(self):

		pre = None
		cur = self.head
		while cur:
			nxt = cur.next
			cur.next = pre
			pre = cur 
			cur = nxt
		self.head = pre 

	def reverse_recursive(self):
		def _reverse_recursive(curr, prev):
			if not curr:
				return
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt

			return _reverse_recursive(curr, prev)
		self.head= _reverse_recursive(curr = self.head, prev = None)

    

	def merge_sorted(self, llist):
		p = self.head
		q = llist.head
		s = None
		if not p:
			return
		if not q:
			return
			


		if p and q:
			if p.data <= q.data:
				# s.next = p
				s = p
				p = s.next
			else:
				s.head = q
				s = q
				# q = s.head
			new_head = s

		while p and q:
			if p.data <= q.data:
				s.next = p
				s = p
				p = s.next
			else:
				s.next = q
				s = q
				q = s.next

		if not p:
			s.next = q
		if not q:
			s.next = p

		return new_head
    # program to sort two merged linked lists
    # def merge_sorted(self, llist):
    # 	p = self.head
    # 	q = llist.head
    # 	s = None
    # 	if not p:
    # 		return q

    # 	if not q:
    # 		return p

    # 	if p and q:
    # 		if p.data <= q.data:
    # 			s = p
    # 			p = p.next
    # 		else:
    # 			s = q
    # 			q= q.next
    # 		new_head = s

    # 	while p and q:
    # 		if p.data <= q.data:
    # 			s.next = p
    # 			s = p
    # 			p= s.next
    # 		else:
    # 			s.next = q
    # 			s = q
    # 			q = s.next

    # 	if not p:
    # 		s.next = q
    # 	if not q:
    # 		s.next = p

    # 	return new_head



    
    # Swapping of nodes

    # def swap_nodes(self, key_1, key_2):
    	
    # 	if key_1 == key_2:
    # 		return

    # 	previous_node_1 = None
    # 	current_node_1 = self.head
    # 	while current_node_1 and current_node_1.data != key:
    # 		previous_node_1 = current_node_1
    # 		current_node_1 = current_node_1.next

    # 	previous_node_2 = None
    # 	current_node_2 = self.head
    # 	while current_node_2 and current_node_2.data != key:
    # 		previous_node_2 = current_node_2
    # 		current_node_2 = current_node_2.next

    # 	if not current_node_1 and not current_node_2:
    # 		return 

    # 	if previous_node_1:
    # 		previous_node_1.next = current_node_2
    # 	else:
    # 		self.head = current_node_2

    # 	if previous_node_2:
    # 		previous_node_2.next = current_node_1
    # 	else:
    # 		self.head = current_node_1

    # 	# current_node_1.next , current_node_2.next = current_node_2.next, current_node_1.next
    
    # def remove_duplicates(self):
    # 	previous = None
    # 	curr = self.head
    # 	dup_values = dic()
    # 	while curr:
    # 		if curr.data in dup_values:
    # 			curr.next = previous.next
    # 			curr = None
    # 		else:
    # 			dup_values [curr.data] = 1
    # 			previous = curr
    # 		curr = previous.next	


#  s == s[:: -1] is a short method for checking reverse of string in python
#  given a linked list to check it is pailin drome or not?

	


llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)

print("Original Linked List")
llist.print_list()
print("Linked List After Removing Duplicates")
llist.remove_duplicates()
llist.print_list()