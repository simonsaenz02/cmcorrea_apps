import streamlit as st
from PIL import Image

# =========================
# ESTILOS CSS PERSONALIZADOS
# =========================
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 42px;
        color: #1E88E5;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .exercise-card {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        transition: transform 0.2s ease-in-out;
    }
    .exercise-card:hover {
        transform: scale(1.03);
        box-shadow: 4px 4px 20px rgba(0,0,0,0.2);
    }
    .exercise-title {
        font-size: 20px;
        font-weight: bold;
        color: #0d47a1;
        margin-bottom: 10px;
    }
    .exercise-desc {
        font-size: 14px;
        color: #424242;
        margin-bottom: 10px;
    }
    .btn-link {
        display: inline-block;
        padding: 6px 12px;
        background-color: #1E88E5;
        color: white !important;
        border-radius: 8px;
        text-decoration: none;
        font-size: 14px;
        font-weight: bold;
    }
    .btn-link:hover {
        background-color: #1565C0;
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# TÍTULO PRINCIPAL
# =========================
st.markdown("<h1 class='main-title'>📘 Bitácora de Ejercicios - Interfaces Multimodales</h1>", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.subheader("ℹ️ Acerca de esta Bitácora")
    st.write(
        "Esta bitácora recopila los 15 ejercicios desarrollados en el curso de Interfaces "
        "Multimodales, mostrando ejemplos prácticos de interacción con Inteligencia Artificial "
        "y sistemas ciberfísicos."
    )
    st.markdown("---")
    st.write("**👤 Autor:** Simón Saenz Giraldo")

# =========================
# FUNCION PARA CREAR EJERCICIOS
# =========================
def ejercicio(titulo, img, desc, url):
    with st.container():
        st.markdown("<div class='exercise-card'>", unsafe_allow_html=True)
        st.markdown(f"<div class='exercise-title'>{titulo}</div>", unsafe_allow_html=True)
        st.image(Image.open(img), use_column_width="auto")
        st.markdown(f"<div class='exercise-desc'>{desc}</div>", unsafe_allow_html=True)
        st.markdown(f"<a class='btn-link' href='{url}' target='_blank'>🔗 Ir al Ejercicio</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# =========================
# LAYOUT EN 3 COLUMNAS
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    ejercicio("1. Introducción", "ejercicio1_introduccion.jpg", 
              "Descripción y propósito del curso de Interfaces Multimodales.", 
              "https://introsimonsaenz.streamlit.app/")

    ejercicio("2. Interfaz Texto a Voz", "ejercicio2_texto_voz.png", 
              "Conversión automática de texto escrito en voz.", 
              "")

    ejercicio("3. Interfaz Voz a Texto", "ejercicio3_voz_texto.jpg", 
              "Transformación de audio hablado en texto.", 
              "")

    ejercicio("4. Interfaz OCR", "ejercicio4_ocr.jpg", 
              "Reconocimiento de texto en imágenes mediante OCR.", 
              "")

    ejercicio("5. Análisis de Sentimiento", "ejercicio5_sentimiento.jpg", 
              "Clasificación de emociones y opiniones en texto.", 
              "")

with col2:
    ejercicio("6. Análisis de Texto (Español)", "ejercicio6_texto.jpg", 
              "Procesamiento de texto para extracción de información en español.", 
              "")

    ejercicio("7. Análisis de Texto (Inglés)", "ejercicio7_texto_ingles.jpg", 
              "Procesamiento de texto para extracción de información en inglés.", 
              "")

    ejercicio("8. Reconocimiento de Objetos", "ejercicio8_objetos.jpg", 
              "Detección y clasificación de objetos en imágenes.", 
              "")

    ejercicio("9. Reconocimiento de Gestos", "ejercicio9_gestos.jpg", 
              "Interacción por medio de gestos con cámara.", 
              "")

    ejercicio("10. ChatPat (Sistema Experto)", "ejercicio10_chatpat.png", 
              "Sistema experto basado en reglas y conversación.", 
              "")

with col3:
    ejercicio("11. Interpretación de Imágenes", "ejercicio11_interpretacion.png", 
              "Descripción e interpretación automática de imágenes.", 
              "")

    ejercicio("12. Interfaz Táctil", "ejercicio12_tactil.jpg", 
              "Aplicación que usa gestos táctiles como entrada.", 
              "")

    ejercicio("13. Reconocimiento de Bocetos", "ejercicio13_bocetos.jpg", 
              "Identificación de dibujos y bocetos simples.", 
              "")

    ejercicio("14. Control MQTT con Botones", "ejercicio14_mqtt_botones.png", 
              "Control de dispositivos físicos usando botones vía MQTT.", 
              "")

    ejercicio("15. Control MQTT con Voz", "ejercicio15_mqtt_voz.jpg", 
              "Control de dispositivos físicos usando comandos de voz vía MQTT.", 
              "")




