errores = []

with open("logs/servidor.log", "r") as archivo:
    for linea in archivo:
        if "ERROR" in linea:
            errores.append(linea)


with open("reportes/errores.txt", "w")as informe:
    for error in errores:
            informe.write(error)
            


        
