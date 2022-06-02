class SparseArray:
	def __init__(self, A):
		self._orig = A
		self._storage = {}
		for idx, elem in enumerate(A):
			if elem != None:
				self._storage[idx] = elem

	def __len__(self):
		return len(self._storage)

	def __getitem__(j):
	    return self._storage[j]

	def __setitem__(j, e):
    self._storage[j] = e

sparse = [None]*1000 + [1] + [None]*1000 + [2]

new_sparse = SparseArray(sparse)

print(len(new_sparse))