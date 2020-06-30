class Distribution:
	def __init__(self, res = 100):
		self.res = res
		self.dist = [(0,1/res)]
		for t in range(1, res):
			self.dist.append( (self.dist[-1][0] + self.dist[-1][1]*t/res, self.dist[-1][1]* (1 + 1/res)))

	def get_dist(self, t, index):
		if index == 0:
			return self.dist[t][0]
		if t < index:
			return self.dist[t][1]
		else:
			return 0

	def print_matrix(self):
		matrix = [[dist.get_dist(i,j) for j in range(res + 1)] for i in range(res)]
		print(matrix)

