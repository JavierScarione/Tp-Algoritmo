from Pila import Stack
Pila = Stack()
dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": 7000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": 6000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": 15,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": 56000,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": 5000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": 10000,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": 2000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": 23000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": 15000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": 6000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": 2500,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": 1500,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": 2700,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": 5000,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": 25,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": 200,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": 450,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": 15000,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

lista_desc = []
lista_especie = []
for dinosaurio in dinosaurios:
    lista_desc.append(dinosaurio["descubridor"])
    lista_especie.append(dinosaurio["especie"])
DescubridoresSinRepetir = set(lista_desc)
EspecieSinRepetir = set(lista_especie)


Lista_T = []
Lista_peso = []
for dinosaurio in dinosaurios:
    if dinosaurio["nombre"][0] == "T":
        Lista_T.append(dinosaurio["nombre"])
    if dinosaurio["peso"] < 275:
        Lista_peso.append(dinosaurio["nombre"])
    if dinosaurio["nombre"][0] == "A" or dinosaurio["nombre"][0] == "Q" or dinosaurio["nombre"][0] == "S":
        Pila.push(dinosaurio["nombre"])
 

print(f"""Descubridores: {DescubridoresSinRepetir}
Especies: {EspecieSinRepetir}
      
Los dinosaurios que comienzan con T, son: {Lista_T}

Los dinosaurios que pesan menos de 275 kg, son: {Lista_peso}

Los dinosaurios que comienzan con Q, S o A; son: """)

for i in range(Pila.size()):
    elemento = Pila.pop()
    print(elemento)


