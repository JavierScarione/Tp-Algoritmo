# actividad 1
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)


#print(fibonacci(10))


# actividad 2
def sumatoria(num):
    if num == 0:
        return 0
    else:
        return num + sumatoria(num-1)


#print(sumatoria(10))


# actividad 3
def producto(num, num2):
    if num2 == 1:
        return 1
    else:
        return num + producto(num, num2-1)


#print(producto(2, 5))


# actividad 4
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)


#print(potencia(2, 5))


# actividad 6
def invertir_palabra(palabra):
    if len(palabra) == 0:
        return palabra
    else:
        return palabra[-1] + invertir_palabra(palabra[0:-1])


#print(invertir_palabra("hola"))


# actividad 7
def fraccion(denominador):
    if denominador == 1:
        return 1
    else:
        return 1 / denominador + fraccion(denominador-1)


#print(fraccion(6))


# actividad 8
def convertir_binario(num):
    if num <= 1:
        return str(num)
    else:
        return convertir_binario(num // 2) + str(num % 2)


#print(convertir_binario(8))


# actividad 10
def contar_digitos(num):
    if num < 10:
        return 1
    else:
        return 1 + contar_digitos(num // 10)


#print(contar_digitos(5467))


# actividad 11
def invertir_numero(num):
    if num < 10:
        return num
    else:
        return (num % 10) * 10 ** len(str(num // 10)) + invertir_numero(num // 10)


#print(invertir_numero(1432))


# actividad 14
def sumar_digitos(num):
    if num < 10:
        return num
    else:
        return (num % 10) + sumar_digitos(num // 10)

#print(sumar_digitos(1223))


# actividad 15
def raiz_cuadrada(num, valor=1):
    if num == 0 or num == 1:
        return num
    else:
        resultado = valor * valor
        if resultado == num:
            return valor
        elif resultado > num:
            return valor - 1
        else:
            return raiz_cuadrada(num, valor+1)


#print(raiz_cuadrada(16))


# actividad 17
def reordenar_lista(lista):
    if len(lista) == 1:
        print("")
    else:
        print(lista[-1])
        reordenar_lista(lista[0:-1])


#print(reordenar_lista(lista=["juan", "jorge", "maria", "pepe"]))
