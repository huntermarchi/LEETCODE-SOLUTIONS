INF = float("inf")
class Solution:
    def __init__(self):
        self.graph = dict()

    def dijkstra(self, edges: List[int], start: int) -> list:
        heap = [[0, start]]
        dist = [INF] * len(edges)
        dist[start] = 0

        while heap:
            curr_cost, curr_node = heappop(heap)

            if curr_node in self.graph:
                nei_node = self.graph[curr_node]
                total_cost = curr_cost + 1

                if total_cost < dist[nei_node]:
                    dist[nei_node] = total_cost
                    heappush(heap, [total_cost, nei_node])

        return dist

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        for i, v in enumerate(edges):
            if v > -1:
                self.graph[i] = v

        dist1 = self.dijkstra(edges, node1)
        dist2 = self.dijkstra(edges, node2)
        min_distance = float("inf")
        answer = -1

        for i in range(len(edges)):
            if (
                dist1[i] != INF
                and dist2[i] != INF
                and min_distance > max(dist1[i], dist2[i])
            ):
                min_distance = max(dist1[i], dist2[i])
                answer = i

        return answer
        
