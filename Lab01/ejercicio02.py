import math
#x=Vi*t + (a*t2)/2

print("Ejercicio02: Que desea calcular: 1. distancia, 2.velocidad, 3. tiempo, 4. aceleracion")
condicion=int(input())
if condicion == 1: #calculo de distancia
    print("Ingrese velocidad: ")
    v=float(input())
    print("Ingrese tiempo: ")
    t=float(input())
    print("Ingrese aceleracion: ")
    a=float(input())
    x= v*t +(a*t*t)/2
    
    print("La distancia es : " +f"{x}" )
elif condicion == 2: #calculo de velocidad
    print("Ingrese distancia: ")
    x = float(input())
    print("Ingrese tiempo: ")
    t = float(input())
    print("Ingrese aceleracion: ")
    a=float(input())
    
    print ("el tiempo no puede ser 0 ") if t==0 else print("la velocidad es: " + f"{(x/t)-(a*t/2)}")
    
elif condicion == 3: #calculo de tiempo
    print("Ingrese distancia: ")
    x = float(input())
    print("Ingrese velocidad: ")
    v = float(input())
    print("Ingrese aceleracion: ")
    a=float(input())
    if a==0:
        print ("el la velocidad no ser 0 si la aceleracion es 0 ") if v==0 else print("el tiempo es: " + f"{x/v}")
    elif v==0:
        if a!=0:
            print ("la aceleracion no puede ser 0 si la velocidad es 0") if a ==0 else print ("el tiempo es "+ f"{math.sqrt(2*x/a)}")
        elif 2*x/a<0:
            print ("2*x/a tiene que ser mayor a 0 para cumplir la restriccion de la raiz cuadrada") if a ==0 else print ("el tiempo es "+ f"{math.sqrt(2*x/a)}")
    
    
elif condicion == 4: #calculo de aceleracion
    print("Ingrese distancia: ")
    x = float(input())
    print("Ingrese velocidad: ")
    v = float(input())
    print("Ingrese tiempo: ")
    t = float(input())
    
    print ("el tiempo no puede ser 0 ") if t==0 else print("la aceleracion es: " + f"{(2*x-2*v*t)/t*t}")
else:
    print("Error")