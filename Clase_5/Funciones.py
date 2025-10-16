'''
funciones

'''

def sumar (a,b):
    r=a+b
    print(f"sumado dentro de la funcion: {a}+{b}={r}")
    return r

a=5
b=3
resultado=sumar(a,b)
print("-----Fuera de la Funcion-----")
print(f"el resultado de la suma es: {resultado}")    
if resultado>5:
    print("el resultado es mayor a 5")
else:
    print("el resultado es menor o igual a 5")