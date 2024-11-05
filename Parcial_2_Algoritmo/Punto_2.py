from Grafo import Graph

StarWars = Graph(dirigido=False)

# Punto A
StarWars.insert_vertice("Yoda")
StarWars.insert_vertice("Luke")
StarWars.insert_vertice("Leia")
StarWars.insert_vertice("Han")
StarWars.insert_vertice("Obi-Wan")
StarWars.insert_vertice("Anakin")
StarWars.insert_vertice("Padmé")
StarWars.insert_vertice("Mace Windu")
StarWars.insert_vertice("Boba Fett")
StarWars.insert_vertice("Darth Vader")
StarWars.insert_vertice("Ahsoka Tano")
StarWars.insert_vertice("Chewbacca")

StarWars.insert_arista("Yoda", "Luke", 5)
StarWars.insert_arista("Yoda", "Leia", 3)
StarWars.insert_arista("Yoda", "Obi-Wan", 4)
StarWars.insert_arista("Luke", "Leia", 4)
StarWars.insert_arista("Luke", "Han", 1)
StarWars.insert_arista("Han", "Leia", 6)
StarWars.insert_arista("Leia", "Chewbacca", 3)
StarWars.insert_arista("Obi-Wan", "Anakin", 7)
StarWars.insert_arista("Anakin", "Padmé", 5)
StarWars.insert_arista("Padmé", "Leia", 2)
StarWars.insert_arista("Mace Windu", "Yoda", 4)
StarWars.insert_arista("Boba Fett", "Han", 3)
StarWars.insert_arista("Darth Vader", "Luke", 5)
StarWars.insert_arista("Ahsoka Tano", "Anakin", 8)

# Mostrar el grafo
StarWars.show_graph()
print(" ")

# Punto B
def ArbolExpMin(graph):
    Arbol = StarWars.kruskal("Yoda")
    YodaInArbol = any("Yoda" in arbol for arbol in Arbol)
    return Arbol, YodaInArbol

Arbol, Yoda = ArbolExpMin(StarWars)
if Yoda == True:
    print(" Yoda esta en el arbol de expacion minimo")
else:
    print(" Yoda no esta en el arbol de expancion minimo")

# Punto C
print("")
def MaxEpisodes(graph):
    MaxPeso = 0
    for nodo in graph.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > MaxPeso:
                MaxPeso = arista['peso']
    return MaxPeso

MaxPeso = MaxEpisodes(StarWars)
print(f"El número máximo de episodios que comparten dos personajes es: {MaxPeso}")

def arista_mas_grande(graph):
    MaxPeso = 0
    nodos = (None, None) 
    for nodo in graph.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > MaxPeso:
                MaxPeso = arista['peso']
                nodos = (nodo['value'], arista['value'])  
    return MaxPeso, nodos

peso_maximo, nodos_conectados = arista_mas_grande(StarWars)
print(f"La arista más grande tiene un peso de {peso_maximo} y conecta a los nodos: {nodos_conectados[0]} y {nodos_conectados[1]}")

# Punto D (agregando personajes faltantes)
print("")
StarWars.insert_vertice("C-3PO")
StarWars.insert_vertice("Rey")
StarWars.insert_vertice("Kylo Ren")
StarWars.insert_vertice("R2-D2")
StarWars.insert_vertice("BB-8")

StarWars.insert_arista("C-3PO", "Leia", 2)
StarWars.insert_arista("C-3PO", "R2-D2", 3)
StarWars.insert_arista("R2-D2", "Luke", 5)
StarWars.insert_arista("BB-8", "Rey", 4)
StarWars.insert_arista("Kylo Ren", "Rey", 6)
StarWars.insert_arista("Kylo Ren", "Darth Vader", 4)
StarWars.insert_arista("R2-D2", "C-3PO", 1)

