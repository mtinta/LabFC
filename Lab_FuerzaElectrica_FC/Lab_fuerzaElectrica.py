import matplotlib.pyplot as plt

#funcion
def calcular_fuerza_electrica(q1, q2, k, r):
    return k * q1 * q2 / r**2


#datos
q1 = float(input("Ingrese la magnitud de la carga q1 : "))
q2 = float(input("Ingrese la magnitud de la carga q2 : "))
k = 8.9875e9  
r = float(input("Ingrese la distancia entre las cargas en metros: "))

#calculo Fuerza
fuerza = calcular_fuerza_electrica(q1, q2, k, r)
print(f"\nLa fuerza eléctrica entre las cargas es: {fuerza} newtons")

#calculo Campo
def calcular_campo_electrico(k,q,r):
  return k * q / r**2

campo1 = calcular_campo_electrico(q1,k,r)
campo2 = calcular_campo_electrico(q2,k,r)

#grafico
#fuerza electrica
distancias = [i for i in range(1, int(r))] 
fuerzas = [calcular_fuerza_electrica(q1, q2, k, d) for d in distancias]
#campo electrico de carga 1
campos1 = [calcular_campo_electrico(q1,k,d) for d in distancias]
#campo electrico de carga 2
campos2 = [calcular_campo_electrico(q2,k,d) for d in distancias]
plt.plot(distancias, fuerzas, label='Fuerza electrica')
plt.plot(distancias, campos1, label='Campo de Carga 1')
plt.plot(distancias, campos2, label='Campo de Carga 2')

plt.title('Fuerza  en funcion de la Distancia')
plt.xlabel('Distancia en metros')
plt.ylabel('Fuerza en newtons')
plt.legend()
plt.show()
