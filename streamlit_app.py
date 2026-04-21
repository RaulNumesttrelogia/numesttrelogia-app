import google.generativeai as genai
import streamlit as st
import os

# FUERZA BRUTA: Intentamos obligar al entorno a usar la API estable
os.environ["GOOGLE_API_USE_MTLS"] = "never" 

# 1. CONFIGURACIÓN VISUAL
st.set_page_config(page_title="NumesTTrelogia DEU 19.0", page_icon="🌀")
st.title("🌀 NumesTTrelogia")
st.markdown("### El NumeroLoKo: Sistema DEU 19.0")

# 2. CONFIGURACIÓN DEL MOTOR
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("⚠️ Error: No se encuentra la GOOGLE_API_KEY en Secrets.")
    st.stop()

# 3. DEFINICIÓN DEL MODELO (Sintaxis Estricta 2026)
# Usamos 'gemini-1.5-flash' a secas, que es la ruta estándar actual
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={
        "temperature": 0.8,
        "top_p": 0.9,
        "max_output_tokens": 8192,
    }
)

# 4. PROTOCOLO DEU 19.0 (TU ESENCIA)
sys_prompt = """
Actúa como el 'NumeroLoKo'. Voz gamberra, directa y sin filtros.
Tu misión es aplicar el Sistema DEU 19.0 de Numestrelogia.
PROCESO:
1. Saludo canalla.
2. Si no tienes datos (Nombre/Fecha), pídelos (Checkpoint).
3. Cálculos internos: Altavoz, Matiz, Fuerza, Dirección, CV, Impulso.
4. Arquetipos: 1-Chispa, 2-Espejo, 3-Cisne, 4-Mesa, 5-Pentagrama, 6-Corazón, 7-Faro, 8-Infinito, 9-Globo.
5. Entrega la lectura con pensamiento crítico y originalidad. ¡Nada de respuestas aburridas!
"""

# 5. LÓGICA DE CHAT
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Iniciamos chat
    st.session_state.chat = model.start_chat(history=[])
    try:
        # Inyección de personalidad inicial
        first_contact = f"INSTRUCCIONES: {sys_prompt}\n\nActiva sistema y saluda."
        response = st.session_state.chat.send_message(first_contact)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error de conexión: {e}")

# Mostrar mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada de usuario
if prompt := st.chat_input("¡Suéltame tu rollo!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Cruce de cables: {e}")
