#Δ(x) = v * Δ(t)
#x=distancia
#v = velocidad
#t = tiempo

print("Que desea calcular: 1. distancia, 2.velocidad, 3. tiempo")
a=int(input())
#casos imposibles:
#si se quiere calcular t, v != 0
#si se quiere calcular v , t !=0
#si se quiere calcular x
if a ==1: #calculo de distancia
    print("Ingrese velocidad: ")
    v=float(input())
    print("Ingrese tiempo: ")
    t=float(input())
    x= v*t
    print("La distancia es : " +f"{x}" )
elif a == 2: #calculo de velocidad
    print("Ingrese distancia: ")
    x = float(input())
    print("Ingrese tiempo: ")
    t = float(input())
    print ("el tiempo no puede ser 0 ") if t==0 else print("la velocidad es: " + f"{x*t}")
    
elif a == 3: #calculo de tiempo
    print("Ingrese distancia: ")
    x = float(input())
    print("Ingrese velocidad: ")
    v = float(input())
    print ("la velocidad no puede ser 0 ") if v==0 else print("el tiempo es: " + f"{x/v}")
else:
    print("Error")

