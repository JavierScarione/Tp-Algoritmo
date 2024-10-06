from Cola import Queue

cola_jedi = Queue()

# Listar Jedis
jedi = [
    {'nombre': 'Ahsoka Tano', 'maestros': ['Anakin Skywalker'], 'colores_sable': ['verde', 'blanco'], 'especie': 'Togruta'},
    {'nombre': 'Kit Fisto', 'maestros': ['Mace Windu'], 'colores_sable': ['verde'], 'especie': 'Nautolan'},
    {'nombre': 'Yoda', 'maestros': [], 'colores_sable': ['verde'], 'especie': 'Desconocido'},
    {'nombre': 'Luke Skywalker', 'maestros': ['Yoda', 'Obi-Wan Kenobi'], 'colores_sable': ['azul'], 'especie': 'Humano'},
    {'nombre': 'Mace Windu', 'maestros': ['Yoda'], 'colores_sable': ['violeta'], 'especie': 'Humano'},
    {'nombre': 'Qui-Gon Jinn', 'maestros': [], 'colores_sable': ['verde'], 'especie': 'Humano'},
    {'nombre': 'Obi-Wan Kenobi', 'maestros': ['Qui-Gon Jinn'], 'colores_sable': ['azul'], 'especie': 'Humano'},
    {'nombre': 'Aayla Secura', 'maestros': ['Ki-Adi-Mundi'], 'colores_sable': ['verde'], 'especie': 'Twi\'lek'},
    {'nombre': 'Barriss Offee', 'maestros': ['Luminara Unduli'], 'colores_sable': ['verde'], 'especie': 'Mirialan'},
]

for i in jedi:
    cola_jedi.arrive(i)

# Punto A.
print(" ")
print(" Lista ordenada por nombre y especie: ")
jedi_ordenados = []
while cola_jedi.size() > 0:
    jedi_ordenados.append(cola_jedi.attention())

for j in sorted(jedi_ordenados, key=lambda x: (x['nombre'], x['especie'])):
    print(f"Nombre: {j['nombre']}, Especie: {j['especie']}")

# Punto B
print(" ")
print(" Información de Ahsoka Tano y Kit Fisto: ")
for j in jedi_ordenados:
    if j['nombre'] in ['Ahsoka Tano', 'Kit Fisto']:
        print(f"Nombre: {j['nombre']}, Maestros: {j['maestros']}, Colores de sable: {j['colores_sable']}, Especie: {j['especie']}")

# Punto C.
print(" ")
print(" Los padawan de Yoda y Luke Skywalker son: ")
padawans = []
for j in jedi_ordenados:
    if 'Yoda' in j['maestros'] or 'Luke Skywalker' in j['maestros']:
        padawans.append(j['nombre'])

for padawan in padawans:
    print(f"Padawan: {padawan}")

# Punto D.
print(" ")
print(" Los jedi de especie humana y Twi'lek son: ")
for j in jedi_ordenados:
    if j['especie'] in ['Humano', "Twi'lek"]:
        print(f"Nombre: {j['nombre']}, Especie: {j['especie']}")

# Punto E.
print(" ")
print(" Los jedi que comienzan con A son: ")
for j in jedi_ordenados:
    if j['nombre'].startswith('A'):
        print(f"Nombre: {j['nombre']}")

# Punto F.
print(" ")
print(" Los jedi que usan sables de luz de más de un color son: ")
for j in jedi_ordenados:
    if len(j['colores_sable']) > 1:
        print(f"Nombre: {j['nombre']}, Colores de sable: {j['colores_sable']}")

# Punto G.
print(" ")
print(" Los jedi con sable de luz amarillo o violeta son: ")
for j in jedi_ordenados:
    if 'amarillo' in j['colores_sable'] or 'violeta' in j['colores_sable']:
        print(f"Nombre: {j['nombre']}, Colores de sable: {j['colores_sable']}")

# Punto F.
print(" ")
print(" Los padawans de Qui-Gon Jinn y Mace Windu son: ")
padawans_qui_gon_mace = []
for j in jedi_ordenados:
    if 'Qui-Gon Jinn' in j['maestros'] or 'Mace Windu' in j['maestros']:
        padawans_qui_gon_mace.append(j['nombre'])

for padawan in padawans_qui_gon_mace:
    print(f"Padawan: {padawan}")