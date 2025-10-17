import streamlit as st
from PIL import Image

st.title("Bitácora de Ejercicios - Interfaces Multimodales")

with st.sidebar:
    st.subheader("Acerca de esta Bitácora")
    parrafo = (
        "Esta bitácora recopila los 15 ejercicios desarrollados en el curso de Interfaces "
        "Multimodales, mostrando ejemplos prácticos de interacción con Inteligencia Artificial "
        "y sistemas ciberfísicos."
    )
    st.write(parrafo)

    st.markdown("---")
    st.write("**Autor:** Simón Saenz Giraldo")

col1, col2, col3 = st.columns(3)

# ------------------------------
# COLUMNA 1
# ------------------------------
with col1:
    st.subheader("1. Introducción")
    image = Image.open("ejercicio1_introduccion.png")
    st.image(image, width=190)

    st.subheader("2. Interfaz Texto a Voz")
    image = Image.open("ejercicio2_texto_voz.png")
    st.image(image, width=190)

    st.subheader("3. Interfaz Voz a Texto")
    image = Image.open("ejercicio3_voz_texto.png")
    st.image(image, width=190)

    st.subheader("4. Interfaz OCR")
    image = Image.open("ejercicio4_ocr.png")
    st.image(image, width=190)

    st.subheader("5. Análisis de Sentimiento")
    image = Image.open("ejercicio5_sentimiento.png")
    st.image(image, width=190)

# ------------------------------
# COLUMNA 2
# ------------------------------
with col2:
    st.subheader("6. Análisis de Texto (Español)")
    image = Image.open("ejercicio6_texto.png")
    st.image(image, width=190)

    st.subheader("7. Análisis de Texto (Inglés)")
    image = Image.open("ejercicio7_texto_ingles.png")
    st.image(image, width=190)

    st.subheader("8. Reconocimiento de Objetos en Imágenes")
    image = Image.open("ejercicio8_objetos.png")
    st.image(image, width=190)

    st.subheader("9. Reconocimiento de Gestos")
    image = Image.open("ejercicio9_gestos.png")
    st.image(image, width=190)

    st.subheader("10. ChatPat (Sistema Experto)")
    image = Image.open("ejercicio10_chatpat.png")
    st.image(image, width=190)

# ------------------------------
# COLUMNA 3
# ------------------------------
with col3:
    st.subheader("11. Interpretación de Imágenes")
    image = Image.open("ejercicio11_interpretacion.png")
    st.image(image, width=190)

    st.subheader("12. Interfaz Táctil")
    image = Image.open("ejercicio12_tactil.png")
    st.image(image, width=190)

    st.subheader("13. Reconocimiento de Bocetos")
    image = Image.open("ejercicio13_bocetos.png")
    st.image(image, width=190)

    st.subheader("14. Control MQTT con Botones")
    image = Image.open("ejercicio14_mqtt_botones.png")
    st.image(image, width=190)

    st.subheader("15. Control MQTT con Voz")
    image = Image.open("ejercicio15_mqtt_voz.png")
    st.image(image, width=190)



