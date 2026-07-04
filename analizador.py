errores = []

try:

    with open("logs/servidor.log", "r") as archivo:
        for linea in archivo:
            if "ERROR" in linea:
                errores.append(linea)
    print("lectura exitosa")            

    with open("reportes/errores.txt", "w")as informe:
        for error in errores:
            informe.write(error)
    print("informe generado")        

except FileNotFoundError as inexixtente:
        print("Archivo no existe: ", inexixtente)


            


        
