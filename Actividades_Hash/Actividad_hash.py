
def hash_nivel(pokemons):
    return pokemon["nivel"] % 10

def hash_tipo(pokemons):
    return tuple(pokemon["tipo"])
   
def hash_num(pokemons):
    return pokemon["numero"] % 10

tabla_nivel = {}
tabla_tipo = {}
tabla_num = {}

pokemons = [
    {"nombre": "Bulbasaur", "tipo": ["Plantas", "veneno"] , "nivel": 5, "numero": 1},
    {"nombre": "Charmander", "tipo": ["Fuego"] , "nivel": 4, "numero": 4},
    {"nombre": "Squirtle", "tipo": ["Agua"], "nivel": 88, "numero": 7},
    {"nombre": "Pikachu", "tipo": ["Eléctrico"] , "nivel": 61, "numero": 25},
    {"nombre": "rattata" ,"tipo": ["Normal"] ,"nivel": 4 ,"numero": 19},
    {"nombre": "meowth" ,"tipo": ["Normal"] ,"nivel": 13 ,"numero": 52},
    {"nombre": "noivern" ,"tipo": ["Volador", "Dragon"] ,"nivel": 17 ,"numero": 715},
    {"nombre": "abra" ,"tipo": ["Psiquico"] ,"nivel": 12 ,"numero": 63},
    {"nombre": "gyarados" ,"tipo": ["Agua","Volador"] ,"nivel": 55 ,"numero": 130},
    {"nombre": "eevee" ,"tipo": ["Normal"] ,"nivel": 7 ,"numero": 133},
    {"nombre": "Jigglypuff", "tipo": ["Normal","Hada"] , "nivel": 5, "numero": 39},
    {"nombre": "hydreigon" ,"tipo": ["Dragon", "Siniestro"] ,"nivel": 43 ,"numero": 635},
    {"nombre": "yveltal" ,"tipo": ["Siniestro","Volador" ],"nivel": 56 ,"numero": 717},
    {"nombre": "sceptile" ,"tipo": ["Planta"] ,"nivel": 71 ,"numero": 254},
    {"nombre": "tyrunt" ,"tipo": ["Roca", "Dragon"] ,"nivel": 2 ,"numero": 696},
    {"nombre": "vibrava" ,"tipo": ["Tierra","Dragon"] ,"nivel": 9 ,"numero": 329},
    {"nombre": "tyranitar" ,"tipo": ["Rocar","Siniestro"] ,"nivel": 48 ,"numero": 248},
    {"nombre": "scraggy" ,"tipo": ["Siniestro","Lucha"] ,"nivel": 37 ,"numero": 559},
    {"nombre": "rhyperior" ,"tipo": ["Tierra", "Roca"] ,"nivel": 69 ,"numero": 464},
    {"nombre": "gengar" ,"tipo": ["Fantasma", "Veneno"] ,"nivel": 74 ,"numero": 94}
]

for pokemon in pokemons:

    # Tabla por tipo
    for tipo in hash_tipo(pokemon):
        if tipo not in tabla_tipo:
            tabla_tipo[tipo] = []
        tabla_tipo[tipo].append(pokemon)
    
    # Tabla por nivel
    key_2 = hash_nivel(pokemon)
    if key_2 not in tabla_nivel:
        tabla_nivel[key_2] = []
    tabla_nivel[key_2].append(pokemon)
    
    # Tabla por numero
    key_3 = hash_num(pokemon)
    if key_3 not in tabla_num:
        tabla_num[key_3] = []
    tabla_num[key_3].append(pokemon)

# Cargar un nuevo pokemon
def cargar_pokemon(nombre, tipo, nivel, numero):
    nuevo_pokemon = {"nombre": nombre, "tipo": tipo, "nivel": nivel, "numero": numero}
    pokemons.append(nuevo_pokemon)

# Mostrar pokemons por el numero:
def mostrar_pokemons_por_numero(terminacion):
    for num in terminacion:
        if num in tabla_num:
            print(f"Pokémons con número terminando en {num}:")
            for pokemon in tabla_num[num]:
                print(pokemon)

# Mostrar pokemons por el nivel:
def mostrar_pokemons_por_nivel(multiplos):
    for nivel in multiplos:
        if nivel in tabla_nivel:
            print(f"Pokémons con nivel múltiplo de {nivel}:")
            for pokemon in tabla_nivel[nivel]:
                print(pokemon)

# Mostrar los pokemons por tipo:
def mostrar_pokemons_por_tipo(tipos):
    for tipo in tipos:
        if tipo in tabla_tipo:
            print(f"Pokémons de tipo {tipo}:")
            for pokemon in tabla_tipo[tipo]:
                print(pokemon)

# Cargar un Pokémon nuevo de ejemplo
cargar_pokemon("metagross", ["Acero", "Psiquico"], 55, 376)

# Mostrar pokemons con diferentes caracteristicas:
print("Pokémons cuyos números terminan en 3, 7 y 9:")
mostrar_pokemons_por_numero([3, 7, 9])

print("Pokémons cuyos niveles son múltiplos de 2, 5 y 10:")
mostrar_pokemons_por_nivel([2, 5, 10])

print("Pokémons de tipo Acero, Fuego, Eléctrico, Hielo:")
mostrar_pokemons_por_tipo(["Acero", "Fuego", "Eléctrico", "Hielo"])