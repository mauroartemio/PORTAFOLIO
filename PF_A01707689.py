# Diccionario que contiene las electronegatividades de elementos
electronegatividades = {}

# Función para cargar electronegatividades desde un archivo
def cargarElectronegatividades():
    try:
        with open("electronegatividades.txt", "r") as file:
            for line in file:
                element, value = line.strip().split(': ')
                electronegatividades[element] = float(value)
    except FileNotFoundError:
        print("No se encontró el archivo de electronegatividades.")

# Función para guardar electronegatividades en un archivo
def guardarElectronegatividades():
    with open("electronegatividades.txt", "w") as file:
        for element, value in electronegatividades.items():
            file.write(f"{element}: {value}\n")

# Función para buscar la electronegatividad de un elemento específico
def buscarElectronegatividad():
    cargarElectronegatividades()  # Cargar electronegatividades desde el archivo
    resultados = []  # Lista para almacenar los resultados
    while True:
        elemento = input("Ingrese el símbolo del elemento: ").capitalize()
        electronegatividad = electronegatividades.get(elemento)
        if electronegatividad is not None:
            resultado = f"El elemento {elemento} tiene una electronegatividad de {electronegatividad}"
        else:
            resultado= f"No se encontró la electronegatividad para el elemento {elemento}"
            print(f"No se encontró la electronegatividad para el elemento {elemento}")
            electronegividad_personalizada = float(input("Ingrese el valor de electronegatividad personalizado: "))
            electronegatividades[elemento] = electronegividad_personalizada
            guardarElectronegatividades()  # Actualizar el archivo
        resultados.append(resultado)  # Agrega el resultado a la lista

        continuar = str(input("¿Desea ingresar otro símbolo? (S/N): "))
        if continuar.lower() != 's':
            break

    print("\nResultados:")
    for resultado in resultados:
        print(resultado)
#Función para determinar cuál de dos elementos tiene mayor electronegatividad
def mayorMenorElectronegatividad (elemento1, elemento2):
    resultados = []  #Lista para almacenar los resultados
    while True:
        if elemento1 > elemento2:
            resultado = "La electronegatividad del primer elemento es mayor"            
        elif elemento1 < elemento2:
            resultado = "La electronegatividad del segundo elemento es mayor" 
        elif elemento1==elemento2:
            resultado = "Los elementos tienen la misma electronegatividad."
        else:
            resultado = f"No valido"
        resultados.append(resultado)  # Agrega el resultado a la lista
        
        continuar = str(input("¿Desea ingresar otro par de elementos? (S/N): "))
        if continuar.lower() != 's':
            break
            

    print("\nResultados:")
    for resultado in resultados:
        print(resultado)
        
#Función para calcular la electronegatividad de un compuesto entre dos elementos
def calcularElectronegatividadCompuesto(elemento1, elemento2):
    electrone1 = (elemento1 - elemento2)
    electrone2 = (elemento2 - elemento1)
    return electrone1, electrone2

#Función principal que presenta un menú de opciones al usuario
def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Buscar electronegatividad de un elemento")
        print("2. Electronegatividad mayor y menor")
        print("3. Calcular electronegatividad de un compuesto")
        print("4. Salir")
        
        opcion = input("Ingrese el número de la opción: ")
        
        if opcion == "1":
            buscarElectronegatividad()
        elif opcion == "2":
            elemento1 = float(input("Ingresar valor numerico del primer elemento: "))
            elemento2 = float(input("Ingresar valor numerico del segundo elemento: "))
            mayorMenorElectronegatividad(elemento1, elemento2)
        elif opcion == "3":
            elemento1 = float(input("Ingresar valor numerico del primer elemento: "))
            elemento2 = float(input("Ingresar valor numerico del segundo elemento: "))
            electrone1, electrone2 = calcularElectronegatividadCompuesto (elemento1, elemento2)
            
            resultados = []  #Lista para almacenar los resultados
            while True:
                if elemento1 > elemento2:
                    resultado= f"La electronegatividad del compuesto es: {electrone1:.2f}"
                    
                elif elemento1 < elemento2:
                    resultado= f"La electronegatividad del compuesto es: {electrone2:.2f}"
                    
                elif elemento1==elemento2:
                    resultado= "Los elementos tienen la misma electronegatividad."
                else:
                    resultado = f"No valido"
                    
                
                resultados.append(resultado)  # Agrega el resultado a la lista
                
                continuar = str(input("¿Desea ingresar otro par de elementos? (S/N): "))
                if continuar.lower() != 's':
                    break
                
            print("\nResultados:")
            for resultado in resultados:
                print(resultado)

        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
            
        
main()