# 📊 Análisis de Ventas - Trabajo Práctico

## 📌 Descripción del Proyecto

Este proyecto consiste en el desarrollo de un sistema de análisis de datos de ventas utilizando Python.  
Se emplea un dataset que contiene el registro de ventas diarias, incluyendo fecha y cantidad de ventas.

A partir de estos datos, se implementan diferentes funciones para analizar la información, obtener métricas relevantes y generar una visualización gráfica de la evolución de las ventas en el tiempo.

***

## 🎯 Objetivos

* Analizar un dataset de ventas reales
* Implementar funciones para procesamiento de datos
* Aplicar conceptos de programación modular
* Generar métricas relevantes a partir de los datos
* Visualizar información mediante gráficos
* Exportar resultados a archivos

***

## ⚙️ Funcionalidades Implementadas

El sistema desarrollado permite:

✅ Cargar el dataset desde un archivo CSV  
✅ Calcular el total de ventas  
✅ Calcular el promedio de ventas  
✅ Identificar el día con mayor volumen de ventas  
✅ Mostrar el detalle de ventas por fecha (formateadas a lenguaje natural)  
✅ Generar un gráfico de evolución de ventas  
✅ Guardar los resultados en un archivo de texto  
✅ Exportar el gráfico como imagen

***

## 🧠 Estructura del Código

El script se encuentra organizado de forma modular, separando claramente:

* **Imports**
* **Funciones específicas**
* **Script principal**

Esto permite una mejor legibilidad, reutilización y mantenimiento del código.

### 📌 Funciones principales

* `load_data()` → carga el dataset
* `format_date()` → formatea fechas a español
* `total_sales()` → calcula ventas totales
* `average_sales()` → calcula promedio
* `best_day()` → identifica día con mayor venta
* `sales_by_date()` → muestra ventas por fecha
* `plot_sales()` → genera gráfico
* `save_results()` → guarda resultados en archivo

***

## 📁 Estructura del Proyecto

```
/datos
    ventas.csv

/scripts
    analisis_datos.py

/resultados
    resultados.txt
    grafico_ventas.png
```

***

## ▶️ Ejecución del Proyecto

Para ejecutar el script:

```bash
python scripts/analisis_datos.py
```

***

## 📊 Resultados Generados

Al ejecutar el programa, se obtiene:

* Salida en consola con métricas principales
* Archivo de texto con resultados (`resultados.txt`)
* Imagen del gráfico (`grafico_ventas.png`)

***

## 🛠️ Tecnologías Utilizadas

* Python
* Pandas
* Matplotlib

***

## 🧩 Consideraciones

El dataset utilizado contiene información agregada por día, por lo que el análisis se centra principalmente en la evolución temporal de las ventas y en métricas globales.

***

## 🚀 Conclusión

El proyecto permite demostrar el uso de herramientas de análisis de datos, control de versiones y organización del trabajo en un entorno colaborativo simulado, aplicando buenas prácticas de programación y estructuración de código...
