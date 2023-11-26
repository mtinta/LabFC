import matplotlib.pyplot as plt

# Función para calcular la fuerza eléctrica
def calcular_fuerza_electrica(q1, q2, k, r):
    return k * q1 * q2 / r**2

# Función para calcular el campo eléctrico
def calcular_campo_electrico(k, q, r):
    return k * q / r**2

# Datos ingresados por el usuario
q1 = float(input("Ingrese la carga 1 : "))
q2 = float(input("Ingrese la carga 2  : "))
k = 8.9875e9

#control para que la distancia no sea 0
while True:
    r = float(input("Ingrese la distancia entre las cargas en metros (la distancia no debe ser 0): "))
    if r != 0:
        break
    else:
        print("La distancia no puede ser cero. Inténtelo de nuevo.")

# Cálculo de la fuerza eléctrica
fuerza = calcular_fuerza_electrica(q1, q2, k, r)
print(f"\nLa fuerza electrica entre las cargas es: {fuerza} newtons")

# Cálculo del campo eléctrico
campo1 = calcular_campo_electrico(k, q1, r)
campo2 = calcular_campo_electrico(k, q2, r)

# Gráfico
distancias = [i for i in range(1, int(r))]
fuerzas = [calcular_fuerza_electrica(q1, q2, k, d) for d in distancias]
campos1 = [calcular_campo_electrico(k, q1, d) for d in distancias]
campos2 = [calcular_campo_electrico(k, q2, d) for d in distancias]

plt.plot(distancias, fuerzas, label='Fuerza electrica')
plt.plot(distancias, campos1, label='Campo de Carga 1')
plt.plot(distancias, campos2, label='Campo de Carga 2')

plt.title('Fuerza en función de la Distancia')
plt.xlabel('Distancia en metros')
plt.ylabel('Fuerza en newtons / Campo en N/C')
plt.legend()
plt.show()
