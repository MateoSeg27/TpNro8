#Comenzamos creando las variables que utilizaremos en el codigo
mayor=None
menor=None  #Utilizamos None porque el usuario puede poner numeros demasiados grandes
suma=0

for i in range (1000):
    #El usuario ingresa al numero
    numero=int(input(f"Ingrese un numero {i+1}: "))
    
    #Se hace la comparacion de numeros para averiguar cual es el menor y el mayor
    if mayor is None or numero > mayor:
        mayor=numero
    if menor is None or numero < menor:
        menor=numero
        
    #Vamos sumando cada numero que el usuario agrega
    suma+=numero
        
#Calculamos el promedio 
promedio=suma/1000

#Mostramos los resultados
print(f"El mayor numero es: {mayor}, y el menor es: {menor}")
print(f"El promedio de todos los numeros ingresados es: {promedio}")