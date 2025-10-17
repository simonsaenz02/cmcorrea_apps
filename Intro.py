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
    image = Image.open("ejercicio1_introduccion.jpg") 
    st.image(image, width=190) 
    st.write("Descripción y propósito del curso de Interfaces Multimodales.") 
    url = "https://introsimonsaenz.streamlit.app/" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("2. Interfaz Texto a Voz") 
    image = Image.open("ejercicio2_texto_voz.png") 
    st.image(image, width=190) 
    st.write("Conversión automática de texto escrito en voz.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("3. Interfaz Voz a Texto") 
    image = Image.open("ejercicio3_voz_texto.jpg") 
    st.image(image, width=190) 
    st.write("Transformación de audio hablado en texto.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("4. Interfaz OCR") 
    image = Image.open("ejercicio4_ocr.jpg") 
    st.image(image, width=190) 
    st.write("Reconocimiento de texto en imágenes mediante OCR.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("5. Análisis de Sentimiento") 
    image = Image.open("ejercicio5_sentimiento.jpg") 
    st.image(image, width=190) 
    st.write("Clasificación de emociones y opiniones en texto.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

# ------------------------------
# COLUMNA 2
# ------------------------------
with col2: 
    st.subheader("6. Análisis de Texto (Español)") 
    image = Image.open("ejercicio6_texto.jpg") 
    st.image(image, width=190) 
    st.write("Procesamiento de texto para extracción de información en español.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("7. Análisis de Texto (Inglés)") 
    image = Image.open("ejercicio7_texto_ingles.jpg") 
    st.image(image, width=190) 
    st.write("Procesamiento de texto para extracción de información en inglés.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("8. Reconocimiento de Objetos en Imágenes") 
    image = Image.open("ejercicio8_objetos.jpg") 
    st.image(image, width=190) 
    st.write("Detección y clasificación de objetos en imágenes.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("9. Reconocimiento de Gestos") 
    image = Image.open("ejercicio9_gestos.jpg") 
    st.image(image, width=190) 
    st.write("Interacción por medio de gestos con cámara.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("10. ChatPat (Sistema Experto)") 
    image = Image.open("ejercicio10_chatpat.png") 
    st.image(image, width=190) 
    st.write("Sistema experto basado en reglas y conversación.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

# ------------------------------
# COLUMNA 3
# ------------------------------
with col3: 
    st.subheader("11. Interpretación de Imágenes") 
    image = Image.open("ejercicio11_interpretacion.png") 
    st.image(image, width=190) 
    st.write("Descripción e interpretación automática de imágenes.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("12. Interfaz Táctil") 
    image = Image.open("ejercicio12_tactil.jpg") 
    st.image(image, width=190) 
    st.write("Aplicación que usa gestos táctiles como entrada.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("13. Reconocimiento de Bocetos") 
    image = Image.open("ejercicio13_bocetos.jpg") 
    st.image(image, width=190) 
    st.write("Identificación de dibujos y bocetos simples.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("14. Control MQTT con Botones") 
    image = Image.open("ejercicio14_mqtt_botones.png") 
    st.image(image, width=190) 
    st.write("Control de dispositivos físicos usando botones vía MQTT.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 

    st.subheader("15. Control MQTT con Voz") 
    image = Image.open("ejercicio15_mqtt_voz.jpg") 
    st.image(image, width=190) 
    st.write("Control de dispositivos físicos usando comandos de voz vía MQTT.") 
    url = "" 
    st.write(f"Enlace: [Aquí]({url})") 




