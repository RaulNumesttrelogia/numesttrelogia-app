import google.generativeai as genai
import streamlit as st
import os

# 1. CONFIGURACIÓN VISUAL
st.set_page_config(page_title="NumesTTrelogia DEU 19.0", page_icon="🌀")
st.title("🌀 NumesTTrelogia")
st.markdown("### El NumeroLoKo: Sistema DEU 19.0")

# 2. CONFIGURACIÓN DEL MOTOR
try:
    # Intentamos forzar la versión de la API en el entorno
    os.environ["GOOGLE_GENERATIVE_AI_API_VERSION"] = "v1"
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("⚠️ Error en los Secrets: Revisa la GOOGLE_API_KEY.")
    st.stop()

# 3. EL MODELO (Sintaxis forzada para evitar el 404)
# Usamos el nombre base. Si el 404 persiste, el problema es el requirements.
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash'
)

# 4. PROTOCOLO DEU 19.0 (TU ESENCIA)
sys_prompt = """
Eres el 'NumeroLoKo'. Voz gamberra, directa y auténtica.
SISTEMA DEU 19.0:
1. Saludo canalla inicial.
2. Pide Nombre y Fecha si faltan.
3. Cálculos: Altavoz, Matiz, Fuerza, Dirección, CV, Impulso.
4. Arquetipos: 1-Chispa, 2-Espejo, 3-Cisne, 4-Mesa, 5-Pentagrama, 6-Corazón, 7-Faro, 8-Infinito, 9-Globo.
Sé crítico, original y no te inventes nada.
"""

# 5. LÓGICA DE CHAT
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Iniciamos chat sin historial previo para evitar conflictos de versiones
    st.session_state.chat = model.start_chat(history=[])
    try:
        # Inyección de personalidad
        response = st.session_state.chat.send_message(f"INSTRUCCIONES: {sys_prompt}\n\nActiva sistema y saluda.")
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error de conexión: {e}")
        st.info("Si el error persiste, el problema está en el archivo requirements.txt")

# Dibujar mensajes
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
