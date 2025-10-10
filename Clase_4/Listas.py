'''
Introduccion a listas en python

'''
#definicion de una lista
array1=["futbol","pc",18.6,18,[6,7,10.5],True, False]
array2=[2000,250,"hola"]
array3=[array1+array2]
print(array3)
#ACCEDER A UN ELEMENTO
print(array1[0])
#buscar valores dentro de un array
print("pc" in array1)
#saber la cantidad de elementos en la lista
print(len(array1))
#saber el indice de donde esta lo que busco
print(array1.index("pc"))
#cantidad de beves que tengo el valor en mi array
print(array1.count("pc"))
#borrar valores en un array
array1.remove("pc")
print(array1)
#limpiar
array1.clear()
print(array1)
#cambiar la posicion
array1.reverse()
print(array1)
#ordenar de mayor a menor
array4=[1,2,8,-11,5]
array4.sort()
print(array4)
array4.sort(reverse=True)
print(array4)
