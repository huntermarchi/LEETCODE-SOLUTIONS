class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        q = []
        for n in nums:
            q.append(-2 * n if n & 1 else -n)
        res, maxv = float('inf'), max(q)
        heapq.heapify(q)
        while True:
            t = heapq.heappop(q)
            res = min(res, maxv - t)
            if t & 1:
                break
            t >>= 1
            maxv = max(maxv, t)
            heapq.heappush(q, t)
        return res
