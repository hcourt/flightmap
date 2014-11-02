def at_distance(start, num_steps, map):
	if num_steps == 1:
		return map.edges[start]

	ret = []
	for node in map.edges[start]:
		ret += at_distance(node, num_steps - 1, map)

	return ret