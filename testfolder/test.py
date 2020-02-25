import heapq
pq = [[1,1],[2,4],[5,6],[6,7],[10,56],[7,98],[3,10]]
heapq.heapify(pq)
print(pq)
heapq.heappush(pq,[0,56])
print(pq)