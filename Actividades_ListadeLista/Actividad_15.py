from random import choice
from Lista import show_list_list, by_name, search

entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]

pokemons = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Pikachu",
        "nivel": 20,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Dragonite",
        "nivel": 55,
        "tipo": "Dragón",
        "subtipo": "Volador"
    },
    {
        "nombre": "Aerodactyl",
        "nivel": 52,
        "tipo": "Roca",
        "subtipo": "Volador"
    },
    {
        "nombre": "Terrakion",
        "nivel": 78,
        "tipo": "Roca",
        "subtipo": "Lucha"
    },
    {
        "nombre": "Wingull",
        "nivel": 44,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Tyrantrum",
        "nivel": 68,
        "tipo": "Roca",
        "subtipo": "Dragon"
    }
]

names = ["Ash Ketchum", "Goh", "Leon", "Chloe", "Raihan"]

lista_entrenadores = []

#cargando una nueva lista de entrenadores
for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)
print("")

#asignando pokemons a cada entrenador
for pokemon in pokemons:
    pos = search(lista_entrenadores, 'nombre', choice(names))
    if pos is not None:
        lista_entrenadores[pos]['sublist'].append(pokemon)
    else:
        print('no existe el entrenador')
print("")

#ordenando y mostrando la lista de entrenadores con sus pokemons
lista_entrenadores.sort(key=by_name)
show_list_list('Entrenadores', 'Pokemons', lista_entrenadores)

#cantidad de pokemons de un entrenador en particular (generado automaticamente)
busqueda_entrenador = search(lista_entrenadores, "nombre", choice(names))
total_pokemons = 0
for i in lista_entrenadores[busqueda_entrenador]["sublist"]:
    total_pokemons +=1
print("la cantidad de pokemons de", lista_entrenadores[busqueda_entrenador]["nombre"] ,"es:", total_pokemons)
print("")

#entrenadores con mas de 3 torneos ganados
j = 0
for i in lista_entrenadores:
    if lista_entrenadores[j]["torneos_ganados"] > 3:
        print(lista_entrenadores[j]["nombre"], "ha ganado", lista_entrenadores[j]["torneos_ganados"], "torneos")
    j +=1
print("")

#pokemon del entrenador con mas torneos ganados
j = 0
numero_entrenador = 0
mas_torneos = 0
for i in lista_entrenadores:
    if lista_entrenadores[j]["torneos_ganados"] > mas_torneos:
        mas_torneos = lista_entrenadores[j]["torneos_ganados"]
        entrenador_torneo = lista_entrenadores[j]["nombre"]
    j += 1

pos = search(lista_entrenadores, "nombre", entrenador_torneo)
nivel_mayor = 0
for pokemon_nivel in lista_entrenadores[pos]["sublist"]:
    if pokemon_nivel["nivel"] > nivel_mayor:
        nivel_mayor = pokemon_nivel["nivel"]
        pokemon_mayor = pokemon_nivel["nombre"]
print(f"El pokemon de mayor nivel: {pokemon_mayor} ({nivel_mayor}) del entrenador con mas torneos ganados {entrenador_torneo} ({mas_torneos})")
print("")

# entrenadores con %80 batallas ganadas 
for i in lista_entrenadores:
    total = i["batallas_ganadas"] + i["batallas_perdidas"]
    porcentaje = (total * i["batallas_ganadas"]) /100
    if porcentaje > 79:
       print("entrenador con mas de 79% de victorias: ", i["nombre"])
print("")

#pokemon con tipos especificos
for i in lista_entrenadores:
    for j in i["sublist"]:
        if j["tipo"] == "Fuego" or j["tipo"] == "Planta":
            print(f" el pokemon {j["nombre"]} es de tipo {j["tipo"]}")
        if j["tipo"] == "Agua" and j["subtipo"] == "Volador":
            print(f" el pokemon {j["nombre"]} es de tipo {j["tipo"]} / {j["subtipo"]}")
print("")

#promedio de nivel de pokemons de un entrenador en particular (generado automaticamente)
busqueda_entrenador = search(lista_entrenadores, "nombre", choice(names))
nombre_ent = lista_entrenadores[busqueda_entrenador]["nombre"]
cant_pokemon = 0
for i in lista_entrenadores[busqueda_entrenador]["sublist"]:
    total = i["nivel"]
    cant_pokemon +=1 

print("el promedio de nivel de los pokemon de ",  nombre_ent, "es ", total/cant_pokemon)
print("")

#pokemones iguales entre entrenadores
repetidos = []
for index, pokemon in enumerate(entrenador["sublist"]):
    for nextPokemon in range(index+1, len(entrenador["sublist"])):
        if pokemon["nombre"] == entrenador["sublist"][nextPokemon]["nombre"]:
            if pokemon["nombre"] not in repetidos:
                repetidos.append(pokemon["nombre"])
print("pokemon repetidos: ", repetidos)
print("")

#pokemons terrakion, wingull y tyrantrum
for pos, entrenador in enumerate(entrenadores):
    for i in lista_entrenadores[pos]["sublist"]:
        if i["nombre"] == "Terrakion" or i["nombre"] == "Wingull" or i["nombre"] == "Tyrantrum":
            print(f" {lista_entrenadores[pos]["nombre"]} tiene al pokemon {i["nombre"]}")
print("")

#determinar si un entrenador tiene a x pokemon
cont = 0
entren = input("ingrese el entrenador que desea buscar: ")
entren_bus = search(lista_entrenadores, "nombre", entren)
poken = input("ingrese el pokemon que desea buscar: ")
for busqueda in lista_entrenadores[entren_bus]["sublist"]:
    if busqueda["nombre"] == poken:
        cont += 1
    
if cont >= 1:
        print(f" {poken} pertenece a {entren}")
else:
    print(f" {poken} no pertenece a este entrenador")