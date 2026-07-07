import json # Se importa el módulo json para trabajar cona rchivos JSON y convertirlos en onjetos de Python

errores = []

try:
    # with open() conexión con archivo objeto tipo file en cual almacenamos
    with open("config.json", "r") as config_file:
         config = json.load(config_file) #Lectura de JSON y convierte en un objeto de Python

    with open(config["ruta_logs"], "r") as archivo:
        for linea in archivo:
            if "ERROR" in linea:
                errores.append(linea)
    print("lectura exitosa")            

    with open(config["ruta_reporte"], "w")as informe:
        for error in errores:
            informe.write(error)
    print("informe generado")        

except FileNotFoundError as inexixtente:
        print("No fue posible acceder al archivo. \n Morivo: El archivo no existe", inexixtente)

except PermissionError as denegado:
     print("No fue posible acceder al archivo. \n Verifique los permisos de lectura o escritura.")
            


        
