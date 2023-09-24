import matplotlib.pyplot as plt

##Escriba un código donde se emplee máquina de Atwood para determinar la magnitud de la aceleración de dos objetos y la tensión en la
##cuerda sin peso.
print("Ejercicio 1 : ")      
# Datos
print("Ejercicio 1 : Ingrese Masa del objeto 1")      
m1=float(input())
print("Ejercicio 1 : Ingrese Masa del objeto 2")      
m2=float(input())

#Calculos
def ej01(m1,m2):
  #Si masa 1 es mayor
  if m1>m2:
      a = round((m2-m1)*(9.8)/(m2+m1),3)
      print("la Aceleracion es: " + str(a) + " metros por segundo al cuadrado")
      print("La tension es " + str((a+(9.8))*m1) + "Newtons")
  #Si masa 2 es mayor
  else:
      a = round((m1-m2)*(9.8)/(m2+m1),3)
      print("la Aceleracion es: " + str(a) + " metros por segundo al cuadrado")
      print("La tension es " + str((a+(9.8))*m2) + " Newtons")

ej01(m1,m2)

##Un móvil de masa m recorre una distancia d en un tiempo t, al inicio
##tiene una velocidad inicial vi y una velocidad final vf . Escriba un código
##que determine la fuerza que describe el móvil al momento de realizar
##el cambio de velocidad y grafique el proceso de tiempo y velocidad.

print("Ejercicio 2 : ")      

# Datos
print("Ejercicio 1 : Ingrese la Velocidad Final")      
vf=float(input())
print("Ejercicio 1 : Ingrese la Velocidad inicial")      
vi=float(input())
print("Ejercicio 1 : Ingrese la masa del objeto")      
m3=float(input())
print("Ejercicio 1 : Ingrese el tiempo (en segundos)")      
t=float(input())

# Calcular la fuerza
def ej02(vf,vi,m3,t):
    f=m3*((vf-vi)/t)
    print("La fuerza es " + str(f) + " Newtons")
    return f

fuerza = ej02(vf, vi, m3, t)
print("La fuerza es " + str(fuerza) + " Newtons")

# Datos de la grafica
tiempo = [0, t]
velocidad = [vi, vf]


# Grafico
def grafico(tiempo, velocidad):
    plt.plot(tiempo, velocidad, marker='o', linestyle='-')
    plt.title('Cambio de Velocidad vs. Tiempo')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.grid(True)
    plt.show()

# Graficar
grafico(tiempo, velocidad)