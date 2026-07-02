archivo = open("logs/servidor.log", "r")


errores = []

for linea in archivo:
    if "ERROR" in linea:
        errores.append(linea)
        print(linea)

archivo.close()



print(len(errores))
print(errores)
