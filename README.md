# Análisis en Lote de Consumo Eléctrico IoT con Apache Spark

Proyecto correspondiente a la Tarea 3 - Procesamiento de Datos con Apache Spark del curso Big Data (UNAD).

La aplicación spark_batch_analysis.py procesa en lote los registros de sensores IoT de consumo eléctrico utilizando PySpark. Realiza la carga de datos masiva, la limpieza de registros incompletos o nulos, y el cálculo de métricas de negocio agregadas por cada sensor.

---

## 🎯 Problema
¿Cómo varían el consumo energético acumulado, el promedio de voltaje y las temperaturas máximas registradas entre diferentes sensores IoT de monitoreo eléctrico mediante procesamiento por lotes?

---

## 📊 Conjunto de Datos
El dataset es generado mediante el script generar_datos_batch.py, el cual simula *1,000 registros* de lecturas de sensores distribuidos a lo largo de 7 días. El archivo en formato CSV incluye las siguientes variables:
* timestamp: Fecha y hora de la lectura.
* sensor_id: Identificador único del sensor IoT.
* consumo_kwh: Consumo energético registrado (kWh).
* voltaje_v: Voltaje medido (V).
* temperatura_c: Temperatura ambiental del equipo (°C).
* humedad_pct: Porcentaje de humedad relativa (%).

---

## 🛠️ Estructura del Proyecto

* *generar_datos_batch.py*: Script en Python para la simulación de datos IoT y generación del archivo datos_energia_batch.csv (incluye la introducción deliberada de valores nulos para validación de limpieza).
* *spark_batch_analysis.py*: Script principal en PySpark que ejecuta el pipeline de lectura, filtrado/limpieza de datos y las operaciones de agregación por sensor (groupBy, sum, avg, max).
* *README.md*: Documentación general del proyecto.

---

## 🚀 Instrucciones de Ejecución

1. *Generar los datos de simulación:*
   ```bash
   python3 generar_datos_batch.py
