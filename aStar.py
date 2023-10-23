import heapq
from collections import defaultdict


def aStar(graph, start, goal, heuristics):
    fringe = []
    heapq.heappush(fringe, (0 + heuristics[start], 0, start))
    parents = {}
    g_n_values = {start: 0}
    while fringe:
        _, current_dist, current = heapq.heappop(fringe)
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()

            return current_dist, path
        for nxt in graph[current]:
            g_n = current_dist + graph[current][nxt]
            if nxt not in g_n_values or g_n < g_n_values[nxt]:
                g_n_values[nxt] = g_n
                f_n = g_n + heuristics[nxt]
                heapq.heappush(fringe, (f_n, g_n, nxt))
                parents[nxt] = current
    return float('inf'), []


if __name__ == "__main__":
    graph = {}
    heuristics = {}
    with open('aStar_input.txt', 'r') as file:
        for line in file:
            city_info = line.split()
            heuristics[city_info[0]] = int(city_info[1])
            graph[city_info[0]] = {}
            for i, city in enumerate(city_info[2:]):
                if i % 2 == 0:
                    graph[city_info[0]][city] = int(city_info[2:][i + 1])
                    graph.setdefault(city, {})
                    graph[city][city_info[0]] = int(city_info[2:][i + 1])
    total_cost, path = aStar(graph, 'Arad', 'Bucharest', heuristics)
    print("Path:", " -> ".join(path))
    print("Total Cost:", total_cost)
