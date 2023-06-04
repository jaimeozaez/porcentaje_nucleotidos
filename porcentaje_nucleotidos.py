import os
import platform

# Función que recoge la información sobre la ubicación y nombre del archivo FASTA

def consulta_archivo():


    """
    En la siguiente línea de código debe indicarse la ruta + nombre del archivo FASTA,
    dentro de las comillas de la variable parametro_para_indicar_fichero_FASTA.
    Si se deja vacío (tal como está) se requerirá esta información al usuario por terminal
    """
    parametro_para_indicar_fichero_FASTA = ""



    sistema_operativo = platform.system() # Consulta el sistema operativo donde se ejecuta el script, para configurar correctamente la ruta con un back slash o con un forward lash
    if sistema_operativo == 'Windows':
            separador = '\\'
    else:
            separador = '/'

# Si se especifica la ruta del archivo FASTA dentro de la variable parametro_para_indicar_fichero_FASTA, se usa dicha ruta
    if parametro_para_indicar_fichero_FASTA != "":
        directorio = os.path.dirname(parametro_para_indicar_fichero_FASTA) + separador # Guardamos la ruta
        archivo = os.path.basename(parametro_para_indicar_fichero_FASTA) # Guardamos el nombre del archivo
        ruta = directorio + archivo


# Si no se indica la ruta del archivo en la variable para parametro_para_indicar_fichero_FASTA, se consulta al usuario con varias preguntas
    else:
        directorio_actual = os.getcwd() # Consulta del directorio donde se ejecuta el archivo porcentaje_nucleotidos.py
        respuesta1 = ''
        while respuesta1 not in ['s', 'si', 'sí', 'n', 'no']: # Serie de preguntas para especificar la ruta y el nombre del archivo. Creamos un bucle hasta que haya sido respondida con una respuesta válida
            respuesta1 = input(f'¿El archivo FASTA se encuentra en el DIRECTORIO actual ({directorio_actual})? Responda (s/n). \n').lower() # Usamos la función lower para convertir en minúsculas cualquier input que introduzca el usuario, y asegurar que coincide con las respuestas válidas disponibles
            if respuesta1 == 's' or respuesta1 == 'si' or respuesta1 == 'sí':
                directorio = directorio_actual + separador
            elif respuesta1 == 'n' or respuesta1 == 'no':
                directorio = input('Ingrese ruta del DIRECTORIO (no incluya la barra final):\n') + separador # En caso de que el archivo FASTA no se encuentre en el mismo directorio que el script, se pide que se especifique la ubicación
            else:
                print('\nRespuesta no válida. Indique s(sí) ó n(no).') # Mensaje de aviso de error en la especificación de la ruta
        archivo = input('Ingrese el nombre del ARCHIVO (incluya la extensión):\n') # Se solicita el nombre del archivo FASTA
        ruta = directorio + archivo # Se ensambla la ruta = directorio + nombre de archivo
        
    print('\nBúsqueda del archivo:', ruta) # Printa la ruta completa para que el usuario pueda comprobar si la ha especificado correctamente
    return ruta, directorio, archivo # Utilizaremos esta información más adelante. Ruta completa; directorio (ruta sin archivo); archivo (nombre del archivo, sin la ruta)


# Función para leer el archivo FASTA y cargar las secuencias en la variable "secuencias"
def cargar_secuencias(s_ruta: str) -> list:

    secuencias = [] # Creamos una lista vacía donde se van a almacenar las secuencias
    try:
        with open(s_ruta, 'r') as f:
            lineas = f.readlines()
            for seq in lineas:
                if not seq.startswith('>'): # Se seleccionan  las secuencias, que corresponden con las lineas que no comienzan con el símbolo ">"
                    secuencias.append(seq.strip()) # Se almacenan las secuencias en la lista, eliminando el salto de línea (\n)
    except:
        print('\nDIRECTORIO O ARCHIVO INCORRECTO\n') # Se captura cualquier error y se printa el mensaje de aviso
    return secuencias

# Función para calcular los porcentajes de cada nucleótido. Devuelve una lista con los 4 porcentajes, además de printar el resultado en pantalla
def calculo_porcentajes(l_secuencias: list) -> list:
    lista_porcentajes = [] # Creamos lista vacía
    if len(l_secuencias) > 0: # Nos aseguramos de que la lista que entra a la función no está vacía (error en la carga del archivo FASTA)
        Bases_totales = 0 # Creamos 5 variables para los recuentos, tanto de cada nucleótido como de bases totales
        a = 0
        t = 0
        c = 0
        g = 0

        for i in l_secuencias: # Iteramos todas las secuencias y contamos los nucleótidos, amentando el contador correspondiente en función de las bases encontradas

            a += i.lower().count('a') # Función lower para que cuente las bases siempre, sin importar que en el archivo FASTA las secuencias estén en mayúsculas o en minúsculas
            t += i.lower().count('t')
            c += i.lower().count('c')
            g += i.lower().count('g')
            Bases_totales += len(i)

        porcentaje_a = round(a/Bases_totales*100, 2) # Hacemos el cálculo del porcentaje y redondeamos con 2 decimales. Guardamos el valor en una variable.
        porcentaje_t = round(t/Bases_totales*100, 2)
        porcentaje_c = round(c/Bases_totales*100, 2)
        porcentaje_g = round(g/Bases_totales*100, 2)

        lista_porcentajes = [porcentaje_a, porcentaje_t, porcentaje_c, porcentaje_g] # Guardamos todos los porcentajes en una lista

        print('\nCálculo de porcentajes de cada nucleótido') # Se muestra el resultado en pantalla
        print('-' * 41)
        print(f'Porcentaje A: {lista_porcentajes[0]}%\nPorcentaje T: {lista_porcentajes[1]}%\nPorcentaje C: {lista_porcentajes[2]}%\nPorcentaje G: {lista_porcentajes[3]}%')

    return lista_porcentajes


# Función para generar el documento de texto con los resultados de los cálculos
def generar_nuevo_documento(s_ruta: str, s_archivo: str, datos: str):
    try: # Capturamos por si se produjera un error al buscar el índice .fa (a veces la extensión .fasta está escrita en mayúsculas)
        nuevo_nombre_archivo = s_archivo[:s_archivo.index('.fasta')] + '_calculos.txt' # Se crea un nombre para el nuevo archivo. El nombre es el mismo que el del FASTA original, pero añadiendo "_calculos.txt"
    except:
        nuevo_nombre_archivo = s_archivo[:s_archivo.index('.FASTA')] + '_calculos.txt'
    with open(s_ruta + nuevo_nombre_archivo, 'w') as w: # Escribimos los datos en el nuevo documento, usando el nuevo nombre recién creado, y guardando el documento en el mismo directorio que el archivo FASTA original
        w.write(f'Porcentaje A: {datos[0]}%\nPorcentaje T: {datos[1]}%\nPorcentaje C: {datos[2]}%\nPorcentaje G: {datos[3]}%') # Se escribe el documento con los datos de los porcentajes
        print(f'\nArchivo {nuevo_nombre_archivo} guardado en ruta ({s_ruta}) con éxito.\n')
    return


# A partir de aquí se ejecutan las funciones programadas más arriba
if __name__ == "__main__":
    
    ruta = consulta_archivo()

    try: # Capturamos por si hay error de lectura del FASTA
        secuencias_cargadas = cargar_secuencias(ruta[0])
        calculos = calculo_porcentajes(secuencias_cargadas)
        generar_nuevo_documento(ruta[1], ruta[2], calculos)
    except:
        print('Proceso ejecutado sin éxito.\n')
