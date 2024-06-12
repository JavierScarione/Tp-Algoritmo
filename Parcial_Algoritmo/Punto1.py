from random import randint

def invertir(Lista):
  if len(Lista) == 0:
    return Lista
  else:
    return  invertir(Lista[1:]) + Lista[:1]

print(invertir(Lista=["Hola,", "Esto", "Es un", "Parcial"]))
