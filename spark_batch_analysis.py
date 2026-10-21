from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum, max, count

def main():
    # 1. Inicialización de la sesión de Spark
    spark = SparkSession.builder \
        .appName("AnalisisConsumoElectricoBatch") \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("WARN")

    print("\n--- INICIANDO PROCESAMIENTO BATCH CON APACHE SPARK ---\n")

    # 2. Carga del conjunto de datos CSV
    df = spark.read.csv("datos_energia_batch.csv", header=True, inferSchema=True)

    print("Esquema del DataFrame cargado:")
    df.printSchema()

    # 3. Limpieza de datos (eliminación de filas con valores nulos en el consumo)
    df_limpio = df.dropna(subset=["consumo_kwh"])

    # 4. Agregación e métricas principales por sensor
    df_resultados = df_limpio.groupBy("sensor_id").agg(
        sum("consumo_kwh").alias("consumo_total_kwh"),
        avg("consumo_kwh").alias("consumo_promedio_kwh"),
        avg("voltaje_v").alias("voltaje_promedio_v"),
        max("temperatura_c").alias("temp_maxima_c"),
        count("timestamp").alias("total_lecturas")
    ).orderBy("sensor_id")

    # 5. Despliegue de resultados consolidado
    print("\n--- RESULTADOS DEL ANÁLISIS BATCH POR SENSOR ---")
    df_resultados.show(truncate=False)

    spark.stop()

if _name_ == "_main_":
    main()
