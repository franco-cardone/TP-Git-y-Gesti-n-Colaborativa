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



# Ventas totales

def total_sales(dataset):

    total = sum(dataset["sales_amount"])

    print(f"Ventas totales: {total}")



# Promedio de ventas

def average_sales(dataset):

    total = sum(dataset["sales_amount"])

    cantidad = len(dataset)

    promedio = total / cantidad


    print(f"Promedio de ventas: {promedio:.2f}")



# Día con más ventas

def best_day(dataset):

    max_ventas = max(dataset["sales_amount"])


    #búsqueda de la fecha correspondiente al día con más ventas y salida por pantalla.

    for i in range(len(dataset)):

        if dataset["sales_amount"][i] == max_ventas:

            fecha = dataset["sales_date"][i]

            fecha_formateada = format_date(fecha)


            print(f"Día con más ventas: {fecha_formateada} ({max_ventas})")

            break



# Ventas por fecha

def sales_by_date(dataset):

    print("
Ventas por fecha:")


    for i in range(len(dataset)):

        fecha = format_date(dataset["sales_date"][i])

        ventas = dataset["sales_amount"][i]


        print(f"{fecha}: {ventas}")



# Gráfico de ventas

def plot_sales(dataset):

    #variables a operar.

    fechas = dataset["sales_date"]

    ventas = dataset["sales_amount"]


    # Promedio

    promedio = sum(ventas) / len(ventas)


    # Día máximo

    max_ventas = max(ventas)

    indice_max = ventas.idxmax()

    fecha_max = fechas[indice_max]


    #construcción del gráfico.

    plt.figure()


    # Línea principal

    plt.plot(fechas, ventas, marker='o', label="Ventas diarias")


    # Línea de promedio

    plt.axhline(y=promedio, linestyle='--', label="Promedio")


    # Punto máximo

    plt.scatter(fecha_max, max_ventas, color='red', label="Máximo")


    #etiquetas de ejes X e Y, Título.

    plt.xlabel("Fecha")

    plt.ylabel("Ventas")

    plt.title("Evolución de ventas")

    plt.xticks(rotation=45)


    #formateado final y salida por pantalla.

    plt.legend()

    plt.tight_layout()

    plt.savefig("resultados/grafico_ventas.png")

    plt.show()



#guardar resultados
def save_results(dataset):
    with open("resultados/resultados.txt", "w") as f:

        # Ventas totales
        total = sum(dataset["sales_amount"])
        f.write(f"Ventas totales: {total}
")

        # Promedio
        promedio = total / len(dataset)
        f.write(f"Promedio de ventas: {promedio:.2f}
")

        # Mejor día
        max_ventas = max(dataset["sales_amount"])
        for i in range(len(dataset)):
            if dataset["sales_amount"][i] == max_ventas:
                fecha = dataset["sales_date"][i]
                fecha_formateada = format_date(fecha)
                f.write(f"Día con más ventas: {fecha_formateada} ({max_ventas})
")
                break

        # Ventas por fecha
        f.write("
Ventas por fecha:
")
        for i in range(len(dataset)):
            fecha = format_date(dataset["sales_date"][i])
            ventas = dataset["sales_amount"][i]
            f.write(f"{fecha}: {ventas}
")

    print("Resultados guardados en resultados/resultados.txt")