import heapq

heap=[]

heapq.heappush(heap,10)
heapq.heappush(heap,1)
heapq.heappush(heap,5)
heapq.heappush(heap,8)

heapq.heappop(heap)

print(heap)