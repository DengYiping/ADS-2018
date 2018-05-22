from heapq import *

class Node:
    compare_by_y = False
    def __init__(self, index):
        self.dx = float('inf')
        self.dy = float('inf')
        self.index = index
        self.visited = False

    def __lt__(self, other):
        if Node.compare_by_y:
            return self.dy < other.dy
        return self.dx < other.dx
    def maxval(self):
        if(self.dx > self.dy):
            return self.dx
        return self.dy

def find_meetup_city(adj_matrix, your_city, friend_city):
    n = len(adj_matrix)
    vec = [Node(i) for i in range(n)]
    q = []

    # Dijkstra on x value
    vec[your_city].dx = 0
    heappush(q, vec[your_city])

    while q:
        v = heappop(q)
        for i in range(n):
            if i != v.index:
                altdist = v.dx + adj_matrix[v.index][i]
                if altdist < vec[i].dx:
                    vec[i].dx = altdist
                    heappush(q, vec[i])

    # Dijkstra on y value
    Node.compare_by_y = True
    vec[friend_city].dy = 0
    heappush(q, vec[friend_city])

    while q:
        v = heappop(q)
        for i in range(n):
            if i != v.index:
                altdist = v.dy + adj_matrix[v.index][i]
                if altdist < vec[i].dy:
                    vec[i].dy = altdist
                    heappush(q, vec[i])

    minCity = min(vec, key = Node.maxval)
    return minCity.index



