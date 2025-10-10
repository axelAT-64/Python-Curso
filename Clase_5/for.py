'''
for - bucle

'''

for i in [6,8,9,4,7,True,"hola",[0,1,2]]:
    print("el dato es: ",i)
    print(f"datos: {i}")
print("------------")
data=["futbol","pc",18.6,18,[6,7,10.5],True, False]
for i in data:
    print("el numero es: ",i)
    print(f"datos: {i}")
print("------For Range------")
for i in range(0,20): #range(inicio,fin,salto)
    print(f"numero: {i}")
print("------While------")
num=0
while num<20:
    print("el numero es:", num)
    num+=1
