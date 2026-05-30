import pandas as pd

#carga de dataset.
def load_data():
    dataset = pd.read_csv("datos/ventas.csv")
    if not dataset.empty:
        print("dataset cargado correctamente")
        return dataset
    else:
        print("error al cargar el dataset: ")
        return None
load_data()