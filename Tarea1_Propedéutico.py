#1
pi = 3.14159
diametro = 3

radio = diametro / 2
print(radio)

area = pi * radio ** 2
print(area)

#2
a = [3, 2, 1]
b = [1, 2 ,3]

a, b = b, a

print (a)
print (b)

#3a
x1 = (5 - 3) // 2
print(x1)

#3b
x2 = 8 - (3 * 2) - (1 + 1)
print(x2)

#4
dulces_juan = 121
dulces_maria = 77
dulces_alberto = 109

# Escriba en el lado derecho una expresión aritmética de los dulces que deben ser tirados
dulces_sobrantes = (dulces_juan + dulces_maria + dulces_alberto)%3

print("sobran "+str(dulces_sobrantes)+" dulces")

#5
def redondear_a_dos_decimales(num):
    return round(num,2)

print(redondear_a_dos_decimales(3.14159))

#6
print(round(2345.32, -2))

#7
def dulces_sobrantes(dulces_totales):
    """
    Devuelve el número de dulces a distribuir entre el total de amigos.
    Si no se asignan amigos, automáticamente se considerarán 3 amigos.

    >>> dulces_sobrantes(91)
    1
    """
    print("please give number of friends: ")
    amigos = input()
    if amigos == "":
        amigos = 3

    buds = int(amigos)

    if buds != 3:
        dulces_totales / buds


    return ("amigos: "+str(buds), "dulces totales: "+str(dulces_totales), "dulces sobrantes: "+str(dulces_totales%buds))

print(dulces_sobrantes(231))

#8a - no sé si se pensaba incluir 2 redondeos, por lo que los he planteado de las 4 posibles formas de interpretar el ejercicio
print(redondear_a_dos_decimales(9)) #no tiene decimales por redondear, queda igual
print(redondear_a_dos_decimales(9999)) #no tiene decimales por redondear, queda igual
print(redondear_a_dos_decimales(99999)) #no tiene decimales por redondear, queda igual
print(redondear_a_dos_decimales(9.9999)) #cambiando la "," por "." ya redondea según Python

#8b - solo faltaba una coma entre ambos "abs"
x = -10
y = 5
abs_mas_pequeño = min(abs(x), abs(y))

print(abs_mas_pequeño)

#8c - solo faltaba indentación
def f(x):
    y = abs(x)
    return y

print(f(5))

#9
def sign(num):
    if num < 0:
        s = -1
        textSign = "negativo"
    elif num == 0:
        s = 0
        textSign = "cero"
    elif num > 0:
        s = 1
        textSign = "positivo"

    return s, textSign

print(sign(-23))
print(sign(23))

#10
def es_negativo_conciso(num2):
    return (num2 < 0)

print(es_negativo_conciso(1023))
print(es_negativo_conciso(-1023))

#11
def sin_cebolla(ketchup, mostaza, cebolla):
    """
    Devuelve True si el cliente no quiere cebolla, y False de lo contrario.
    """
    return not cebolla

print(sin_cebolla(True,True,False))

#11a
def todos_los_ingredientes(ketchup, mostaza, cebolla):
    """
    Devuelve True si el cliente quiere todos los ingredientes, y False de lo contrario
    """
    return ketchup and mostaza and cebolla

print(todos_los_ingredientes(True,True,True))
print(todos_los_ingredientes(True,False,True))
print(todos_los_ingredientes(True,True,False))
print(todos_los_ingredientes(True,False,False))
print(todos_los_ingredientes(False,True,True))
print(todos_los_ingredientes(False,True,False))
print(todos_los_ingredientes(False,False,True))
print(todos_los_ingredientes(False,False,False))

#11b
def sin_ingredientes(ketchup, mostaza, cebolla):
    """
    Devuelve True si el cliente no quiere ningún ingrediente, y False de lo contrario.
    """
    return not ketchup and not mostaza and not cebolla

print(sin_ingredientes(True,True,True))
print(sin_ingredientes(True,True,False))
print(sin_ingredientes(True,False,True))
print(sin_ingredientes(True,False,False))
print(sin_ingredientes(False,True,True))
print(sin_ingredientes(False,True,False))
print(sin_ingredientes(False,False,True))
print(sin_ingredientes(False,False,False))

#11c
def solo_un_aderezo(ketchup, mostaza, cebolla):
    """
    Devuelve True si el cliente quiere ketchup o mostaza, pero no ambos.
    """
    return (ketchup or mostaza) and not (ketchup and mostaza)

print(solo_un_aderezo(True,True,True))
print(solo_un_aderezo(True,True,False))
print(solo_un_aderezo(True,False,True))
print(solo_un_aderezo(True,False,False))
print(solo_un_aderezo(False,True,True))
print(solo_un_aderezo(False,True,False))
print(solo_un_aderezo(False,False,True))
print(solo_un_aderezo(False,False,False))

#12
int(False)

def exactamente_un_ingrediente(ketchup, mostaza, cebolla):
    """
    Devuelve True si el ciente quiere exactamente un ingrediente, False de lo contrario.
    """
    return (ketchup+mostaza+cebolla==1)

print(exactamente_un_ingrediente(True, True, True))
print(exactamente_un_ingrediente(True, True, False))
print(exactamente_un_ingrediente(True, False, True))
print(exactamente_un_ingrediente(True, False, False))
print(exactamente_un_ingrediente(False, True, True))
print(exactamente_un_ingrediente(False, True, False))
print(exactamente_un_ingrediente(False, False, True))
print(exactamente_un_ingrediente(False, False, False))

#13
def segundo_elemento(L):
    """
    Devuelve el segundo elemento de la lista dada. Si la lista no tiene
    segundo elemento, devuelve None.

    >>> segundo_elemento([10, 4, 9, 10])
    4
    >>> segundo_elemento([5])

    """
    return L[1] if len(L)>=2 else None


def elemento_n(L, n):
    return L[n-1] if len(L)>=n else None

print(segundo_elemento([10,4,9,10]))
print(segundo_elemento([5]))

#14
def cuantos_negativos(lista):
    """
    Devuelve la cantidad de números negativos en la lista dada.

    >>> cuantos_negativos([5, -1, -2, 0, 3])
    2
    """
    negs = len([i for i in lista if i < 0])

    return negs

print(cuantos_negativos([5, -1, -2, 0, 3]))

#15
def es_chida(nums):
    """
    Devuelve True si la lista dada es chida. Una lista chida es aquella que
    contiene al menos un número divisible por 7.

    >>> es_chida([1, 14, 3, 8])
    True
    """
    for num in nums:
        if num == 0:
            return False
        elif num%7 == 0:
            return True
    return False

print(es_chida([1,2,3,14]))
print(es_chida([1,14,28,8]))
print(es_chida([1,14,28,0]))

#16
def cp_valido(cp):
    """
    Devuelve True si el string dado es un código postal válido y es un
    string de 5 dígitos.

    >>> cp_valido('45017')
    True
    >>> cp_valido('450015')
    False
    >>> cp_valido('45a15')
    False
    """

    return(cp.isdigit() and len(cp) == 5)

print(cp_valido('45017'))
print(cp_valido('450015'))
print(cp_valido('45a15'))











#
