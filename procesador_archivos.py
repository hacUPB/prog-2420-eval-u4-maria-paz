# CÓDIGO PYTHON:

import os
import csv
import statistics
import matplotlib.pyplot as plt

def listar_archivos(ruta="."):
    print("Archivos en la ruta actual o especificada:")
    for archivo in os.listdir(ruta):
        print(archivo)

# Funciones para el archivo de texto .txt

def contar_palabras(ruta_txt):
    with open(ruta_txt, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        print(f"Número total de palabras: {len(palabras)}")

def reemplazar_palabra(ruta_txt, palabra_buscar, palabra_reemplazar):
    with open(ruta_txt, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    contenido = contenido.replace(palabra_buscar, palabra_reemplazar)
    with open(ruta_txt, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
    print(f"Reemplazo de '{palabra_buscar}' por '{palabra_reemplazar}' completado.")

def contar_caracteres(ruta_txt):
    with open(ruta_txt, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    caracteres_total = len(contenido)
    caracteres_sin_espacios = len(contenido.replace(" ", ""))
    print(f"Número total de caracteres (incluyendo espacios): {caracteres_total}")
    print(f"Número de caracteres (sin contar espacios): {caracteres_sin_espacios}")

# Funciones para el archivo CSV

def mostrar_15_filas(archivo_csv):
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for i, fila in enumerate(lector):
            if i < 15:
                print(fila)
            else:
                break

def calcular_estadisticas(archivo_csv, columna):
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        datos = [float(fila[columna]) for fila in lector if fila[columna]]
    if datos:
        print(f"Número de datos: {len(datos)}")
        print(f"Promedio: {statistics.mean(datos)}")
        print(f"Mediana: {statistics.median(datos)}")
        print(f"Máximo: {max(datos)}")
        print(f"Mínimo: {min(datos)}")
    else:
        print(f"No se encontraron datos numéricos en la columna '{columna}'.")

def graficar_columna(archivo_csv, columna):
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        datos = [float(fila[columna]) for fila in lector if fila[columna]]
    if datos:
        plt.plot(datos)
        plt.title(f"Gráfico de la columna '{columna}'")
        plt.xlabel("Índice")
        plt.ylabel("Valor")
        plt.show()
    else:
        print(f"No se encontraron datos numéricos en la columna '{columna}'.")

# Menú principal

def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Listar archivos en la ruta actual o especificar una ruta")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo CSV (.csv)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            ruta = input("Ingrese la ruta (o presione Enter para usar la ruta actual): ")
            listar_archivos(ruta or ".")
        elif opcion == '2':
            ruta_txt = input("Ingrese el nombre del archivo .txt a procesar: ")
            menu_texto(ruta_txt)
        elif opcion == '3':
            archivo_csv = input("Ingrese el nombre del archivo .csv a procesar: ")
            menu_csv(archivo_csv)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Submenú para archivos de texto

def menu_texto(ruta_txt):
    while True:
        print("\nSubmenú para archivos de texto (.txt)")
        print("1. Contar número de palabras")
        print("2. Reemplazar una palabra por otra")
        print("3. Contar el número de caracteres")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            contar_palabras(ruta_txt)
        elif opcion == '2':
            palabra_buscar = input("Ingrese la palabra a buscar: ")
            palabra_reemplazar = input("Ingrese la palabra de reemplazo: ")
            reemplazar_palabra(ruta_txt, palabra_buscar, palabra_reemplazar)
        elif opcion == '3':
            contar_caracteres(ruta_txt)
        elif opcion == '4':
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Submenú para archivos CSV

def menu_csv(archivo_csv):
    while True:
        print("\nSubmenú para archivos CSV (.csv)")
        print("1. Mostrar las primeras 15 filas")
        print("2. Calcular estadísticas de una columna")
        print("3. Graficar una columna completa")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_15_filas(archivo_csv)
        elif opcion == '2':
            columna = input("Ingrese el nombre de la columna para calcular estadísticas: ")
            calcular_estadisticas(archivo_csv, columna)
        elif opcion == '3':
            columna = input("Ingrese el nombre de la columna para graficar: ")
            graficar_columna(archivo_csv, columna)
        elif opcion == '4':
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el programa

if __name__ == "__main__":
    menu_principal()
