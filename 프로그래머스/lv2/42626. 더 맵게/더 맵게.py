import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return 0
    else:
        while scoville[0] < K:
            if len(scoville) == 1:
                return -1
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            new = a+b*2
            heapq.heappush(scoville, new)
            cnt += 1
        return cnt