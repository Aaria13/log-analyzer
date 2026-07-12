import json # Se importa el módulo json para trabajar con archivos JSON y convertirlos en objetos de Python
import csv 

errores = []
headers = ["Línea", "Tipo", "Mensaje"]

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
    
    with open("reportes/errores.csv", "w") as informe_csv:
         escritor = csv.writer(informe_csv)
         escritor.writerow(headers)
         contador = 0

         for error in errores:
              contador = contador + 1 
              fila = error.split(" ", 1) #Cómo guardo el resultado de split?
              filas_csv = [
                   contador,
                   fila[0],
                   fila[1]
              ]
              escritor.writerow(filas_csv)
              print(filas_csv)         

except json.JSONDecodeError:
     print("Error en el archivo de configuración. \n El archivo config.json tiene un formato JSON inválido. \n Revise la sintaxis del archivo.")                  

except FileNotFoundError as inexixtente:
        print("No fue posible acceder al archivo. \n Morivo: El archivo no existe", inexixtente)

except PermissionError as denegado:
     print("No fue posible acceder al archivo. \n Verifique los permisos de lectura o escritura.")          
      
    

        
