#Vf=Vi+a*t

print("Que desea calcular: 1. Velocidad final, 2.Velocidad inicial, 3. tiempo, 4. aceleracion")
condicion=int(input())
if condicion ==1: #calculo de Velocidad Final
    print("Ingrese velocidad: ")
    vi=float(input())
    print("Ingrese tiempo: ")
    t=float(input())
    print("Ingrese aceleracion: ")
    a=float(input())

    print("La Velocidad final es : " +f"{vi+a*t}" )
elif condicion == 2: #calculo de velocidad Inicial
    print("Ingrese distancia: ")
    vf = float(input())
    print("Ingrese tiempo: ")
    t = float(input())
    print("Ingrese aceleracion: ")
    a=float(input())
    
    print("La Velocidad inicial  es : " +f"{vf-a*t}" )
    
elif condicion == 3: #calculo de tiempo
    print("Ingrese distancia: ")
    vf = float(input())
    print("Ingrese velocidad: ")
    vi = float(input())
    print("Ingrese aceleracion: ")
    a=float(input())
    
    print ("la aceleracion no puede ser 0 ") if a==0 else print("el tiempo es: " + f"{(vf-vi)/a}")
    
elif condicion == 4: #calculo de aceleracion
    print("Ingrese distancia: ")
    vf = float(input())
    print("Ingrese velocidad: ")
    vi = float(input())
    print("Ingrese tiempo: ")
    t = float(input())
    
    print ("el tiempo no puede ser 0 ") if t==0 else print("la aceleracion es: " + f"{(vf-vi)/t}")
else:
    print("Error")