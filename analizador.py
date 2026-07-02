archivo = open("logs/servidor.log", "r")

contenido = archivo.read()

archivo.close()

print(contenido)
