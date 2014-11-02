import heapq

def lightest_path(start, end, graph):
    queue = [(0, start, [])]
    seen = set()
    while True:
        (cost, v, path) = heapq.heappop(queue)
        if v not in seen:
            path = path + [v]
            seen.add(v)
            if v == end:
                return path
            for next in graph.edges[v]:
            	weight = graph.weights[(v, next)]
                heapq.heappush(queue, (cost + weight, next, path))
