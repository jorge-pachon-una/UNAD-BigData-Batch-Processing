import csv
import random
from datetime import datetime, timedelta

# Configuración de generación de datos IoT
NUM_REGISTROS = 1000
SENSORES = [101, 102, 103, 104, 105]

fecha_inicio = datetime.now() - timedelta(days=7)

with open('datos_energia_batch.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Encabezados
    writer.writerow(['timestamp', 'sensor_id', 'consumo_kwh', 'voltaje_v', 'temperatura_c', 'humedad_pct'])
    
    for i in range(NUM_REGISTROS):
        timestamp = (fecha_inicio + timedelta(minutes=i*10)).strftime('%Y-%m-%d %H:%M:%S')
        sensor_id = random.choice(SENSORES)
        consumo_kwh = round(random.uniform(0.5, 5.0), 2)
        voltaje_v = round(random.uniform(110.0, 125.0), 1)
        temperatura_c = round(random.uniform(20.0, 35.0), 1)
        humedad_pct = round(random.uniform(40.0, 80.0), 1)
        
        # Introducir algunos valores nulos ocasionales para simular limpieza de datos
        if random.random() < 0.02:
            consumo_kwh = None

        writer.writerow([timestamp, sensor_id, consumo_kwh, voltaje_v, temperatura_c, humedad_pct])

print("Dataset datos_energia_batch.csv generado exitosamente con 1000 registros.")
