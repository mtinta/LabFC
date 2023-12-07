##Resistencias en serie
def resistencia_serie(*resistencias):
    return sum(resistencias)
##Resistencias en paralelo
def resistencia_paralelo(*resistencias):
    return 1 / sum(1 / r for r in resistencias)
##
def intensidad_circuito(voltaje, *componentes):
    resistencia_equivalente = 0 ##Se inicializa la resistencia equivalente del circuito

    for componente in componentes: 
        tipo, *valores = componente
      ##Se colocan etiquetas para  los componentes : serie, paralelo o para inicio de subcircuito.
      ##Se va modicicando el valor de resistencia equivalente sumando los resultados del calculo de resistencias
        if tipo == "serie": 
            resistencia_equivalente += resistencia_serie(*valores)
        elif tipo == "paralelo":
            resistencia_equivalente += resistencia_paralelo(*valores)

       ##Se usara recursion para crear subcircuitos     
        elif tipo == "subcircuito":
            resistencia_subcircuito = intensidad_circuito(voltaje, *valores)
            resistencia_equivalente += resistencia_subcircuito

    ##Se devuelve como resultado de la funcion el la intensidad
    intensidad = voltaje / resistencia_equivalente
    return intensidad
##Valor del voltaje en voltios
voltaje_fuente = 45
##Transcribir el circuito
componentes_circuito = [
   ("serie",1.5),
   ("subcircuito",
    ("subcircuito",("serie",3.3),("paralelo",430,820)),("subcircuito",("paralelo",6.2,120)))
]

##Calculo del voltaje 
intensidad_resultante = intensidad_circuito(voltaje_fuente, *componentes_circuito)

print(f"La intensidad en el circuito es: {intensidad_resultante} Amperios")
