# =========================
# Librerías a utilizar.
# =========================

import pandas as pd
import matplotlib.pyplot as plt


# =========================
# Funciones a ejecutar en script principal.
# =========================

# Carga de dataset
def load_data():
    try:
        #intentar leer dataset.
        dataset = pd.read_csv("datos/ventas.csv")
        #verificar que el dataset no esté vasío.
        if not dataset.empty:
            print("Dataset cargado correctamente")
            return dataset
        else:
            print("Error: el dataset está vacío")
            return None
        #verificación de errores al cargar el dataset.
    except Exception as e:
        print("Error al cargar el dataset:", e)
        return None



# Formateo de fecha a español

def format_date(date_str):

#división de la columna "sales date" en variables utilizables, strings; utilizando el guión - como divisor.

    partes = date_str.split("-")

    anio = partes[0]

    mes = partes[1]

    dia = partes[2]


    #diccionario de meses

    meses = {

        "01": "enero", "02": "febrero", "03": "marzo",

        "04": "abril", "05": "mayo", "06": "junio",

        "07": "julio", "08": "agosto", "09": "septiembre",

        "10": "octubre", "11": "noviembre", "12": "diciembre"

    }


    #obtención de fecha en formato comprensible.

    mes_nombre = meses.get(mes, "mes desconocido")

    #formateado y ordenamiento final.

    return f"{int(dia)} de {mes_nombre} del {anio}"



