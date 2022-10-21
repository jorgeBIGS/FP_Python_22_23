def funcion1():
    return ', soy una función.'

def funcion_con_funcion(nombre, funcion):
    return nombre + funcion()

print(funcion_con_funcion("Jorge", funcion1))