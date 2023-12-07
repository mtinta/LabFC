##Resistencias en serie
def resistencia_serie(*resistencias):
    return sum(resistencias)
##Resistencias en paralelo
def resistencia_paralelo(*resistencias):
    return 1 / sum(1 / r for r in resistencias)
##
def intensidad_circuito_mixto(intensidad, *componentes):
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
            resistencia_subcircuito = intensidad_circuito_mixto(intensidad, *valores)
            resistencia_equivalente += resistencia_subcircuito

    ##Se devuelve como resultado de la funcion el voltaje
    voltaje = resistencia_equivalente * intensidad
    return voltaje
##Valor de la intensidad en amperios
intensidad_corriente = 0.0601  
##Transcribir el circuito
componentes_circuito = [
    ("serie",1,3),
    ("subcircuito",
      ("subcircuito",("serie",8.2,160),("subcircuito",("serie",16,75),("paralelo",82,150)))
     )
    ,("paralelo",51,130)
    ##("subcircuito", ("paralelo", 1.5,10,4.7,100))
]

##Calculo del voltaje 
voltaje_resultante = intensidad_circuito_mixto(intensidad_corriente, *componentes_circuito)
##Imprime el voltaje y resistencia equivalente
print(f"El voltaje en el circuito es: {voltaje_resultante} Voltios")
print(f"La resistencia equivalente en el circuito es: {voltaje_resultante/intensidad_corriente} Ohmios")
