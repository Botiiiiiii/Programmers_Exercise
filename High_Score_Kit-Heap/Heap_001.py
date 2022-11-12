def solution(scoville, K):
    import heapq
    heap = scoville
    heapq.heapify(heap)
    answer = 0
    while(heap[0] < K):
        if len(heap) <= 1:
            return -1
        min = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        heapq.heappush(heap,min+(min2 * 2))
        answer += 1

    return answer


print(solution([1,2,3,9,10,12],7))