#funtion to calculate length of linked list means number of niodes in a linked list.
# from linkedList import LinkedList

def len_iterative(self):
	cur_node = self.head
	count = 0
	while cur_node:
		count +=1
		cur_node = cur_node.next
	return count


