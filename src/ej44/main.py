'''
Asignar una funcion a un elemento de la lista,
ES DECIR GUARDAR LA FUNCION COMO UN VALOR MAS
RECORDAR QUE LA LISTA NO EJECUTA A LAS FUNCIONES SOLO LAS GUARDA
'''
def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

def double(number):
    return number*2

def new_list(lista, function):
    #llamamaos la funcion con el valor x
    return [function(x) for x in lista]


