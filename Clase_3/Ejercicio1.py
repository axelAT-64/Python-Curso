'''
Crear un programa que pida dos numeros 
y obtenga como resultado cual de ellos es par o si ambos lo son.

'''

num1=int(input("ingresa el valor del primer numero: "))
num2=int(input("ingresa el valor del segundo numero: "))

if num1%2==0 and num2%2==0:
    print("ambos numeros son pares.")
elif num1%2==0:
    print("Solo el primer número es par.")
elif num2%2==0:
    print("Solo el segundo número es par.")
else:
    print("Ninguno de los números es par.")
