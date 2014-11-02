from collections import defaultdict

class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = defaultdict(list)
		self.weights = {}

	def add_node(self, name):
		self.nodes.add(name)

	def add_edge(self, start, end, weight):
		self.edges[start].append(end)
		#self.edges[end].append(start)
		self.weights[(start, end)] = weight