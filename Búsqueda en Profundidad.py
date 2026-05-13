def dfs(graph, start, goal):
    stack = [(start, [start])]  # (nodo, camino)
    visited = set()

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue
        visited.add(node)

        print(f"Visitando: {node} | Camino: {path}")

        if node == goal:
            print(f"\n✓ Meta encontrada! Camino: {path}")
            return path

        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    print("No se encontró camino.")
    return None


# Grafo de ejemplo
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': ['G'],
    'D': [],
    'E': [],
    'G': []
}

dfs(graph, 'S', 'G')