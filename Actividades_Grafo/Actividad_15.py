from Grafo import Graph

# Creamos el grafo
maravillas_grafo = Graph(dirigido=False)

maravillas_architectonicas = [
    ("Torre Eiffel", "Francia"),
    ("Coliseo", "Italia"),
    ("Gran Muralla China", "China"),
    ("Chichén Itzá", "México"),
    ("Petra", "Jordania"),
    ("Machu Picchu", "Perú"),
    ("Cristo Redentor", "Brasil")
]

maravillas_naturales = [
    ("Amazonas", ["Brasil", "Perú", "Colombia"]),
    ("Bahía de Ha Long", "Vietnam"),
    ("Islas Galápagos", "Ecuador"),
    ("Montañas de la Patagonia", ["Chile", "Argentina"]),
    ("Parque Nacional de Yellowstone", "EE. UU."),
    ("Gran Barrera de Coral", "Australia"),
    ("Desierto de Sahara", "África")
]

for nombre, pais in maravillas_architectonicas:
    maravillas_grafo.insert_vertice(nombre)

for nombre, pais in maravillas_naturales:
    maravillas_grafo.insert_vertice(nombre)

distancias_architectonicas = [
    ("Torre Eiffel", "Coliseo", 1),
    ("Coliseo", "Gran Muralla China", 2),
    ("Gran Muralla China", "Chichén Itzá", 3),
    ("Chichén Itzá", "Petra", 1),
    ("Petra", "Machu Picchu", 2),
    ("Machu Picchu", "Cristo Redentor", 3),
    ("Cristo Redentor", "Torre Eiffel", 4)
]

distancias_naturales = [
    ("Amazonas", "Bahía de Ha Long", 5),
    ("Bahía de Ha Long", "Islas Galápagos", 6),
    ("Islas Galápagos", "Montañas de la Patagonia", 7),
    ("Montañas de la Patagonia", "Parque Nacional de Yellowstone", 8),
    ("Parque Nacional de Yellowstone", "Gran Barrera de Coral", 9),
    ("Gran Barrera de Coral", "Desierto de Sahara", 10),
    ("Desierto de Sahara", "Amazonas", 11)
]

for origen, destino, distancia in distancias_architectonicas:
    maravillas_grafo.insert_arista(origen, destino, distancia)

for origen, destino, distancia in distancias_naturales:
    maravillas_grafo.insert_arista(origen, destino, distancia)

# Hallamos el árbol de expansión mínima para cada tipo
arbol_expansion_architectonicas = maravillas_grafo.kruskal(maravillas_architectonicas[0][0])  
arbol_expansion_naturales = maravillas_grafo.kruskal(maravillas_naturales[0][0])  
print()
print(" Árbol de expansión mínima de maravillas arquitectónicas:", arbol_expansion_architectonicas)
print()
print(" Árbol de expansión mínima de maravillas naturales:", arbol_expansion_naturales)
print()

# Determinar si existen países que dispongan de maravillas arquitectónicas y naturales
paises_architectonicos = set(pais for _, pais in maravillas_architectonicas)
paises_naturales = set()

# Manejar el caso donde los países son listas
for _, pais in maravillas_naturales:
    if isinstance(pais, list):
        for p in pais:
            paises_naturales.add(p)
    else:
        paises_naturales.add(pais)

paises_comunes = paises_architectonicos.intersection(paises_naturales)
if paises_comunes:
    print(" Países que tienen maravillas arquitectónicas y naturales:", paises_comunes)
else:
    print(" No hay países con maravillas arquitectónicas y naturales.")

# Determinar si algún país tiene más de una maravilla del mismo tipo
from collections import defaultdict

# Contar las maravillas por país para arquitectónicas
pais_count_architectonicas = defaultdict(int)
for _, pais in maravillas_architectonicas:
    pais_count_architectonicas[pais] += 1

# Contar las maravillas por país para naturales
pais_count_naturales = defaultdict(int)
for _, pais in maravillas_naturales:
    if isinstance(pais, list):
        for p in pais:  
            pais_count_naturales[p] += 1
    else:
        pais_count_naturales[pais] += 1

# Verificar si hay algún país con más de una maravilla del mismo tipo
print()
paises_multis_architectonicos = [pais for pais, count in pais_count_architectonicas.items() if count > 1]
paises_multis_naturales = [pais for pais, count in pais_count_naturales.items() if count > 1]

if paises_multis_architectonicos:
    print("Países con más de una maravilla arquitectónica:", paises_multis_architectonicos)
else:
    print("No hay países con más de una maravilla arquitectónica.")
print()
if paises_multis_naturales:
    print("Países con más de una maravilla natural:", paises_multis_naturales)
else:
    print("No hay países con más de una maravilla natural.")