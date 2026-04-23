from collections import deque

# Grafo representado con diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def busqueda_anchura(grafo, inicio, objetivo):
    cola = deque([inicio])   # Cola FIFO
    visitados = []

    while cola:
        nodo = cola.popleft()  # Sacar el primero

        if nodo not in visitados:
            print("Visitando:", nodo)
            visitados.append(nodo)

            if nodo == objetivo:
                print("Objetivo encontrado:", nodo)
                return True

            # Agregar vecinos a la cola
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

    print("Objetivo no encontrado")
    return False


# Ejecutar búsqueda
busqueda_anchura(grafo, 'A', 'F')