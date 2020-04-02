'''
BINARY HEAP 
min heap implementation

formulas starting from index 1:
parent node --> i // 2
children --> (2 * i) and (2 * i) + 1
'''

class BinHeap(object):

	def __init__(self):
		self.heaplist = [0]
		self.current_size = 0

	def _up_heap(self, idx):

		while idx // 2 > 0:

			# check if parent node is greater
			if self.heaplist[idx] < self.heaplist[idx // 2]:
				# swap with parent node
				temp = self.heaplist[idx // 2]
				self.heaplist[idx // 2] = self.heaplist[idx]
				self.heaplist[idx] = temp

			# decrese to check every parent node
			idx = idx // 2



	def _min_child(self, i):
		# check if right node exists
		if (i * 2) + 1 > self.current_size:
			return i * 2
		else: 
			# return the smaller child
			if self.heaplist[i * 2] < self.heaplist[(i * 2) + 1]:
				return i * 2
			else 
				return (i * 2) + 1


	def _down_heap(self, idx):

		while (idx * 2) <= self.current_size:
			mc = self._min_child(idx)

			# swap the parent node with the smaller child
			if self.heaplist[idx] > self.heaplist[mc]:
				temp = self.heaplist[idx]

				self.heaplist[idx] = self.heaplist[mc]
				self.heaplist[mc] = temp
			
			# move idx to 	
			idx = mc



	def insert(self, new_value):
		# add new value to list --> keep tree property
		self.heaplist.append(new_value)

		# update current size
		self.current_size += 1

		# update nodes values --> keep heap property 
		self._up_heap(self.current_size)


	def delete_min(self):
		# get root of list
		root = self.heaplist[1]

		# replace root with last leaf
		self.heaplist[1] = self.heaplist[self.current_size]

		# reduce list size
		self.current_size -= 1
		self.heaplist.pop()

		# update root value --> keep heap property
		self._down_heap(1)

		return root

	def build_heap(self, values):
		idx = len(valuse) // 2 

		self.current_size = len(values)
		self.heaplist = [0] + value[0:]

		while (i > 0):
			self._down_heap(i)
			i -= 1







	


