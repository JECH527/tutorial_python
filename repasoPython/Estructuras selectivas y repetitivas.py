#Repetitiva
#while Para la creación de bucles utilizaremos la palabra clave while, seguida de la condición que queremos que cumpla. Vamos a realizar un primer problema con este tipo de estructura.

x=0
total=0
while x<10:
    nota=int(input("Ingrese la nota: "))
    if nota>4:
        total=total+1
    x=x+1
print("Han aprobado ",total)

#For
suma=0
for x in range(5):
 num=int(input("Ingrese un valor:"))
 suma=suma+num
promedio=suma/5
print("La suma es: ")
print(suma)
print("El promedio es: ")
print(promedio)

#Selectiva
#if
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:

 print("Notable")
elif nota >= 5:

 print("Aprobado")
else:


 print("Suspendido")

#if else
number = 10

if number > 0:
    print('4')

else:
    print('-5')

print('Ejecutar la sentencia')

#elif
z = 7

if z > 8:
  print("¡No voy a imprimir!") #esta sentencia no se ejecuta
elif z > 5:
  print("¡Yo lo haré!") #esta sentencia se ejecuta
elif z > 6:
  print("¡Tampoco voy a imprimir!") #esta sentencia no se ejecuta
else:
  print("¡Yo tampoco!") #esta sentencia no se ejecuta