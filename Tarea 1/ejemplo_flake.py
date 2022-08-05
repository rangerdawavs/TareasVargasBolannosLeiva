# Módulo simple para crear una lista de números pares
# toma un numero x y retorna una lista con todos los numeros pares
# menores o iguales a x
# revisa que x sea entero

def even_list(x):
    # revisamos que sea entero
    if(type(x) != int):
        return 'E22a'
    else:
        # creamos la lista y agregamos los numeros
        lista=[]
        for i in range(0,x+1):
            if (i % 2 == 0):
                lista.append(i)
        return lista
