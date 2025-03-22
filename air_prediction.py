import streamlit as st
import pandas as pd
import joblib
import numpy as np
from PIL import Image

# Cargar modelos y normalizador
scaler = joblib.load("scaler3.joblib")
aqi_encoder = joblib.load("aqi_mapping_1.joblib")
hour_encoder = joblib.load("encoded_hour.joblib")
model = joblib.load("rf_model.joblib")

# Título y descripción
st.title("Predicción de Calidad Aérea")
st.subheader("Realizado por Juan Escobar")
st.image("contaminante.png")

st.write("Esta aplicación permite predecir la calidad del aire basándose en el AQI del PM2.5 y PM10, utilizando un modelo entrenado con scikit-learn para la predicción del AQI general, para determinar si se puede realizar actividad física al aire libre.")

# Entrada de datos
time = st.slider("Hora del día", 0, 23, 12)
pm25 = st.slider("AQI PM2.5", 0, 500, 50)
pm10 = st.slider("AQI PM10", 0, 500, 50)

# Escalar solo PM2.5 y PM10
user_data_scaled = scaler.transform([[pm25, pm10]])

# Concatenar la hora con los datos escalados
user_data = np.concatenate(([time], user_data_scaled[0]), axis=0).reshape(1, -1)

# Realizar predicción
prediction = model.predict(user_data)

# Interpretar la predicción
predicted_aqi_category = int(prediction[0])  # Asegurar que sea un entero

# Mapear la predicción a su categoría
category_map = {
    0: ("Bueno", "😊", "El aire es excelente para cualquier actividad al aire libre."),
    1: ("Moderado", "😐", "El aire es aceptable, pero algunas personas sensibles pueden experimentar molestias."),
    2: ("No sano para grupos sensitivos", "😷", "Los niños, ancianos y personas con problemas respiratorios deberían limitar el ejercicio al aire libre."),
    3: ("No sano en general", "🤒", "Se recomienda evitar actividades intensas al aire libre para todas las personas."),
    4: ("Muy poco sano", "🤢", "Ejercicio al aire libre no recomendado. Riesgo alto de problemas de salud."),
    5: ("Peligroso", "☠️", "Evite cualquier actividad al aire libre. Riesgo grave para la salud."),
}

category, emoji, advice = category_map.get(predicted_aqi_category, ("Desconocido", "❓", "Información no disponible."))

# Mostrar predicción
st.markdown(f"### Calidad del aire: {category} {emoji}")

# Mostrar recomendación sobre ejercicio
st.markdown(f"**Recomendación:** {advice}")

# Línea y copyright
st.markdown("---")
st.markdown("© UNAB 2025")
