import streamlit as st
import joblib
import pandas as pd
import json

st.title("Clasificador de mascotas")
st.write("Casificador de mascotas. Introzca los datos de su mascota y le diremo a que clase pertenece.")
st.image("img/mascotas.jpg")

model = joblib.load("model/pets_model.joblib")
with open("model/category_mapping.json") as f:
    category_mapping = json.load(f)

# Extrae los valores categóricos
eye_color_values = category_mapping["eye_color"]
fur_length_values = category_mapping["fur_length"]

# Pide los datos de la mascota
weigth = st.number_input("Peso (kg)", min_value=0.0, max_value=100.0, value=0.0)
heigth = st.number_input("ALtura (cm)", min_value=0.0, max_value=100.0, value=0.0)
eye_color = st.selectbox("Color de ojos", ["Azul", "Marrón", "Gris", "Verde"])
fur_length = st.selectbox("Largo del pelo", ["Largo", "Medio", "Corto"])

# Mapea la selección de color de ojos y largo del pelo al español
eye_color_map = {"Marrón": "brown", "Azul": "blue", 'Gris' : 'gray', 'Verde': 'green'}
fur_length_map = {"Largo": "long", "Medio": "medium", "Corto": "short"}

selected_eye_color = eye_color_map[eye_color]
selected_fur_length = fur_length_map[fur_length]

# Genera las columnas binarias para eye_color y fur_length
eye_color_binary = [ (color == selected_eye_color) for color in eye_color_values]
fur_length_binary = [ (length == selected_fur_length) for length in fur_length_values]

# Crea un DataFrame con los datos de la mascota
input_data = ["weight_kg", "height_cm"] + eye_color_binary + fur_length_binary
colums = ["weight_kg", "height_cm"] + [f"eye_color_{color}" for color in eye_color_values] + [f"fur_length_{length}" for length in fur_length_values]
input_df = pd.DataFrame([input_data], columns=colums)

# Realizar prediccion
if st.button("Clasificar mascota"):
    prediccion = model.predict(input_df)[0]
    prediccion_map = {"dog": "Perro", "cat": "Gato", "rabibit": "Conejo"}
    st.success("La mascota es un: {prediccion}", icon="✅")
