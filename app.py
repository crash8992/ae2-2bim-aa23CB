import requests
import time
import csv
import threading
import os

def obtener_data():
    lista = []
    with open("informacion/data.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        for row in lineas:
            print(row[0].split("|"))
            num = row[0].split("|")[0]
            pag = row[0].split("|")[1]
            lista.append((num, pag))  
    return lista

def worker(num, url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url ))
    pag = requests.get(url)
    archivo_path = os.path.join("salida", f"{num}.txt")
    os.makedirs(os.path.dirname(archivo_path), exist_ok=True)
    with open(archivo_path, "w") as archivo:
        archivo.write(pag.text)
    time.sleep(10)
    print("Finalizando %s" % (threading.current_thread().getName()))

for c in obtener_data():
    # Se crea los hilos
    # en la función
    num = c[0]
    url = c[1]
    hilo1 = threading.Thread(name='navegando...',
                            target=worker,
                            args=(num, url))
    hilo1.start()