from Cola import Queue

cola = Queue()
colaAux = Queue()

# Listar personajes
personajes = [
    {'nombre': 'Leia Organa', 'altura': 150, 'edad': 22, 'género': 'f', 'especie': 'Humano', 'planeta_natal': 'Alderaan', 'episodios': [4, 5, 6, 7]},
    {'nombre': 'Obi-Wan Kenobi', 'altura': 180, 'edad': 57, 'género': 'm', 'especie': 'Humano', 'planeta_natal': 'Stewjon', 'episodios': [1, 2, 3, 4, 5, 6]},
    {'nombre': 'Darth Vader', 'altura': 202, 'edad': 45, 'género': 'm', 'especie': 'Humano', 'planeta_natal': 'Tatooine', 'episodios': [4, 5, 6]},
    {'nombre': 'Han Solo', 'altura': 180, 'edad': 33, 'género': 'm', 'especie': 'Humano', 'planeta_natal': 'Corellia', 'episodios': [4, 5, 6, 7]},
    {'nombre': 'Padmé Amidala', 'altura': 165, 'edad': 70, 'género': 'f', 'especie': 'Humano', 'planeta_natal': 'Naboo', 'episodios': [1, 2, 3]},
    {'nombre': 'C-3PO', 'altura': 167, 'edad': 112, 'género': 'm', 'especie': 'Droide', 'planeta_natal': 'Tatooine', 'episodios': [1, 2, 3, 4, 5, 6]},
    {'nombre': 'R2-D2', 'altura': 96, 'edad': 112, 'género': 'm', 'especie': 'Droide', 'planeta_natal': 'Naboo', 'episodios': [1, 2, 3, 4, 5, 6, 7]},
    {'nombre': 'Yoda', 'altura': 66, 'edad': 900, 'género': 'm', 'especie': 'Desconocido', 'planeta_natal': 'Desconocido', 'episodios': [1, 2, 3, 5, 6]},
    {'nombre': 'Chewbacca', 'altura': 228, 'edad': 200, 'género': 'm', 'especie': 'Wookiee', 'planeta_natal': 'Kashyyyk', 'episodios': [3, 4, 5, 6, 7]}
]

for i in personajes:
    cola.arrive(i)

print(" Los personajes femeninos son:")
for i in range(cola.size()):
    personaje = cola.attention()
    if personaje['género'] == 'f':
        print(f"Nombre: {personaje['nombre']}, Edad: {personaje['edad']}, Planeta Natal: {personaje['planeta_natal']}, Episodios: {personaje['episodios']}")
    colaAux.arrive(personaje)

for i in range(colaAux.size()):
    p = colaAux.attention()
    cola.arrive(p)

print(" ")
print(" Los droides que aparecieron en episodios 1 al 6 son: ")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['especie'] == 'Droide' and any(e <= 6 for e in personaje['episodios']):
        print(f"Nombre: {personaje['nombre']}, Episodios: {personaje['episodios']}")
    colaAux.arrive(personaje)


for i in range(colaAux.size()):
    p = colaAux.attention()
    cola.arrive(p)

print(" ")
print(" Informacion de Darth Vader y Han Solo: ")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['nombre'] == 'Darth Vader' or personaje['nombre'] == 'Han Solo':
        print(f"\nNombre: {personaje['nombre']}, Altura: {personaje['altura']}, Edad: {personaje['edad']}, Género: {personaje['género']}, "
              f"Especie: {personaje['especie']}, Planeta: {personaje['planeta_natal']}, Episodios: {personaje['episodios']}")
    colaAux.arrive(personaje)


for i in range(colaAux.size()):
    p = colaAux.attention()
    cola.arrive(p)

print(" ")
print(" Los personajes que aparecen en el episodio VII y en los episodios 4, 5 o 6 son:  ")
while cola.size() > 0:
    personaje = cola.attention()
    if 7 in personaje['episodios'] and any(e in [4, 5, 6] for e in personaje['episodios']):
        print(f"Nombre: {personaje['nombre']}, Episodios: {personaje['episodios']}")
    colaAux.arrive(personaje)


for i in range(colaAux.size()):
    p = colaAux.attention()
    cola.arrive(p)

print(" ")
mayores_de_850 = []
print(" Los personajes con edad mayor a 850 años son: ")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['edad'] > 850:
        mayores_de_850.append(personaje)
        print(f"Nombre: {personaje['nombre']}, Edad: {personaje['edad']}")
    colaAux.arrive(personaje)

print(" ")
mayor_personaje = max(mayores_de_850, key=lambda p: p['edad'])
print(f" El personaje más viejo es: {mayor_personaje['nombre']}, con {mayor_personaje['edad']} años")

# Eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI
for i in range(colaAux.size()):
    p = colaAux.attention()
    cola.arrive(p)

print(" ")
print(" Personajes eliminados (Cap IV, V, VI): ")
x = []
while cola.size() > 0:
    personaje = cola.attention()
    if set(personaje['episodios']) != {4, 5, 6}:
        x.append(personaje)
        print(f"Nombre: {personaje['nombre']}, Episodios: {personaje['episodios']}")
    colaAux.arrive(personaje)

for i in range(colaAux.size()):
    p = colaAux.attention()
    cola.arrive(p)

print(" ")
print(" Humanos originarios del planeta Alderaan: ")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['especie'] == 'Humano' and personaje['planeta_natal'] == 'Alderaan':
        print(f"Nombre: {personaje['nombre']}, Planeta Natal: {personaje['planeta_natal']}")
    colaAux.arrive(personaje)

for i in range(colaAux.size()):
    p = colaAux.attention()
    cola.arrive(p)

print(" ")
print(" Los personajes con altura menor a 70 centímetros son: ")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['altura'] < 70:
        print(f"Nombre: {personaje['nombre']}, Altura: {personaje['altura']}")
    colaAux.arrive(personaje)

for i in range(colaAux.size()):
    p = colaAux.attention()
    cola.arrive(p)

print(" ")
print(" Información de Chewbacca: ")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['nombre'] == 'Chewbacca':
        print(f"Nombre: {personaje['nombre']}, Episodios: {personaje['episodios']}")
        print(f"Altura: {personaje['altura']}, Edad: {personaje['edad']}, Especie: {personaje['especie']}, Planeta Natal: {personaje['planeta_natal']}")