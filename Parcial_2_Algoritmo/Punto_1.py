from Arbol_avl import BinaryTree

pokemones = [
    {"nombre": "Bulbasaur","id":1, "tipos": ["Planta", "Veneno"]},
    {"nombre": "Charmander","id":4, "tipos": ["Fuego"]},
    {"nombre": "Squirtle","id":7, "tipos": ["Agua"]},
    {"nombre": "Pikachu","id":25, "tipos": ["Eléctrico"]},
    {"nombre": "Vulpix","id":37, "tipos": ["Fuego"]},
    {"nombre": "Meowth","id":52, "tipos": ["Normal"]},
    {"nombre": "Gastly","id":92, "tipos": ["Fantasma", "Veneno"]},
    {"nombre": "Eevee","id":133, "tipos": ["Normal"]},
    {"nombre": "Mewtwo","id":150, "tipos": ["Psíquico"]},
    {"nombre": "Chikorita","id":152, "tipos": ["Planta"]},
    {"nombre": "Scizor","id":212, "tipos": ["Bicho", "Acero"]},
    {"nombre": "Blaziken","id":257, "tipos": ["Fuego", "Lucha"]},
    {"nombre": "Absol","id":359, "tipos": ["Siniestro"]},
    {"nombre": "Garchomp","id":445, "tipos": ["Dragón", "Tierra"]},
    {"nombre": "Lucario","id":448, "tipos": ["Lucha", "Acero"]},
    {"nombre": "Rotom","id":479, "tipos": ["Eléctrico", "Fantasma"]},
    {"nombre": "Excadrill","id":530, "tipos": ["Tierra", "Acero"]},
    {"nombre": "Volcarona","id":637, "tipos": ["Bicho", "Fuego"]},
    {"nombre": "Sylveon","id":700, "tipos": ["Hada"]},
    {"nombre": "Regidrago","id":895, "tipos": ["Dragón"]},
    {"nombre": "Lycanroc", "id": 745, "tipos": ["Roca"]},
    {"nombre": "Jolteon", "id": 135, "tipos": ["Eléctrico"]},
    {"nombre": "Tyrantrum", "id": 697, "tipos": ["Roca", "Dragón"]},
]

# Punto A
ArbolPorTipo = BinaryTree()
ArbolPorNombre = BinaryTree()
ArbolPorNumero = BinaryTree()

for pokemon in pokemones:
    ArbolPorNombre.insert_node(pokemon['nombre'], pokemon['id'], pokemon['tipos'])
    ArbolPorNumero.insert_node(pokemon['id'], pokemon['nombre'], pokemon['tipos'])
    for tipo in pokemon['tipos']:
        ArbolPorTipo.insert_node(tipo, pokemon, pokemon['id'])


# Punto B
print("Busca pokemon por nombre: ")
ArbolPorNombre.proximity_search("S")
print("")
print("Busca pokemon por numero de pokedex")
print(ArbolPorNumero.search(150).value, ArbolPorNumero.search(150).other_value, ArbolPorNumero.search(150).other_other_value)

# Punto C
print("")
tipo_buscado = "Agua"
ResultadoAgua = ArbolPorTipo.search(tipo_buscado)
if ResultadoAgua:
    pokemon_data = ResultadoAgua.other_value  
    print(f"Número de pokedex: {pokemon_data['id']}, Nombre: {pokemon_data['nombre']}, Tipos: {pokemon_data['tipos']}")
else:
    print("No se encontraron Pokémon de tipo Agua.")

tipo_buscado = "Planta"
ResultadoPlanta = ArbolPorTipo.search(tipo_buscado)
if ResultadoPlanta:
    pokemon_data = ResultadoPlanta.other_value  
    print(f"Número de pokedex: {pokemon_data['id']}, Nombre: {pokemon_data['nombre']}, Tipos: {pokemon_data['tipos']}")
else:
    print("No se encontraron Pokémon de tipo Planta.")

tipo_buscado = "Eléctrico"
ResultadoElec = ArbolPorTipo.search(tipo_buscado)
if ResultadoElec:
    pokemon_data = ResultadoElec.other_value  
    print(f"Número de pokedex: {pokemon_data['id']}, Nombre: {pokemon_data['nombre']}, Tipos: {pokemon_data['tipos']}")
else:
    print("No se encontraron Pokémon de tipo Eléctrico")

tipo_buscado = "Fuego"
ResultadoFuego = ArbolPorTipo.search(tipo_buscado)
if ResultadoFuego:
    pokemon_data = ResultadoFuego.other_value  
    print(f"Número de pokedex: {pokemon_data['id']}, Nombre: {pokemon_data['nombre']}, Tipos: {pokemon_data['tipos']}")
else:
    print("No se encontraron Pokémon de tipo Fuego")

# Punto D
print("")
print(" Listado por nivel")
ArbolPorNombre.by_level()
print("")
print(" Listado de orden ascendente:")
print(" Por nombre:")
ArbolPorNombre.inorden()
print("")
print("por numero de pokedex:")
ArbolPorNumero.inorden()

# Punto E
print("")
ArbolPorNombre.proximity_search("Lycanroc")
ArbolPorNombre.proximity_search("Jolteon")
ArbolPorNombre.proximity_search("Tyrantrum")

# Punto F
print("")
print(" Cantidad de pokemon acero y eléctrico respectivamente: ")
print(ArbolPorTipo.contar_acero())
print(ArbolPorTipo.contar_electrico())
