import time


class Stopwatch:
	def __init__(self):
		self.start = time.time()
		self.split = time.time()

	def reset(self):
		self.start = time.time()
		self.split = time.time()


	def split_time(self):
		val = time.time() - self.split
		self.split = time.time()
		return val

	def stop(self):
		return time.time() - self.start
