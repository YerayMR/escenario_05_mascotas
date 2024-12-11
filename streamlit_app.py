import streamlit as st

st.title("Suma de dos números")

# Pedir el primer número
num1 = st.number_input("Introduce el primer número", value=0.0)

# Pedir el segundo número
num2 = st.number_input("Introduce el segundo número", value=0.0)

# Calcular la suma
resultado = num1 + num2

# Mostrar el resultado
st.write("La suma de los dos números es:", resultado)