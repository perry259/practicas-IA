import heapq

def ucs(graph, start, goal):
    queue = [(0, start, [start])]  # (costo, nodo, camino)
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        print(f"Visitando: {node} | Costo: {cost} | Camino: {path}")

        if node == goal:
            print(f"\n✓ Meta encontrada! Camino: {path} | Costo total: {cost}")
            return path, cost

        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))

    print("No se encontró camino.")
    return None, float('inf')


# Grafo de ejemplo
graph = {
    'S': [('A', 2), ('B', 5)],
    'A': [('C', 3), ('B', 1), ('D', 7)],
    'B': [('D', 4)],
    'C': [('G', 6)],
    'D': [('G', 2)],
}

ucs(graph, 'S', 'G')