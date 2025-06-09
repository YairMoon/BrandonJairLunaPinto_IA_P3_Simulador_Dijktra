import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola = [(0, inicio)]
    visitados = set()
    previos = {}

    paso = 1
    print(f"\n--- Simulación del algoritmo de Dijkstra desde el nodo '{inicio}' ---\n")

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        print(f"Paso {paso}:")
        print(f"   Nodo actual: {nodo_actual}")
        print(f"   Distancia mínima conocida: {distancia_actual}")

        for vecino, peso in grafo[nodo_actual].items():
            if vecino not in visitados:
                nueva_distancia = distancia_actual + peso
                print(f"   Evaluando vecino: {vecino}")
                print(f"      Distancia conocida: {distancias[vecino]}")
                print(f"      Nueva distancia posible: {nueva_distancia}")

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    previos[vecino] = nodo_actual
                    heapq.heappush(cola, (nueva_distancia, vecino))
                    print(f"      ✅ Se actualiza la distancia de '{vecino}' a {nueva_distancia}")
                else:
                    print(f"      ❌ No se actualiza")

        paso += 1
        print("\n----------------------------------\n")

    print("Distancias finales desde el nodo inicial:")
    for nodo, distancia in distancias.items():
        print(f"   {nodo}: {distancia}")
    
    return distancias, previos

def reconstruir_camino(previos, nodo):
    camino = []
    while nodo in previos:
        camino.insert(0, nodo)
        nodo = previos[nodo]
    camino.insert(0, nodo)
    return camino

def graficar_grafo(grafo, inicio, distancias, previos):
    G = nx.DiGraph()

    for nodo in grafo:
        for vecino, peso in grafo[nodo].items():
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)
    etiquetas = nx.get_edge_attributes(G, 'weight')

    # Dibujar nodos y aristas
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1200, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

    # Resaltar el nodo de inicio
    nx.draw_networkx_nodes(G, pos, nodelist=[inicio], node_color='green', node_size=1300)

    # Dibujar caminos más cortos
    for destino in distancias:
        if destino == inicio:
            continue
        camino = reconstruir_camino(previos, destino)
        edges_en_camino = list(zip(camino[:-1], camino[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges_en_camino, edge_color='red', width=2)

    plt.title(f'Rutas más cortas desde "{inicio}"')
    plt.show()

# Ejemplo de grafo
grafo_ejemplo = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

# Ejecutar simulador
inicio = 'A'
distancias, previos = dijkstra(grafo_ejemplo, inicio)
graficar_grafo(grafo_ejemplo, inicio, distancias, previos)
# Este código implementa el algoritmo de Dijkstra y lo simula paso a paso,
# mostrando las distancias mínimas desde un nodo inicial a todos los demás nodos.