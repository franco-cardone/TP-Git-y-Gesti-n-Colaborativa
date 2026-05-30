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

