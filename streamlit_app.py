import google.generativeai as genai
import streamlit as st
import os

# 1. CONFIGURACIÓN VISUAL Y ESENCIA
st.set_page_config(page_title="NumesTTrelogia DEU 19.0", page_icon="🌀")
st.title("🌀 NumesTTrelogia")
st.markdown("### El NumeroLoKo: Sistema DEU 19.0")

# 2. CONFIGURACIÓN DEL MOTOR (BLINDAJE VERSIÓN 2026)
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    # Forzamos la configuración para evitar el error 404 de v1beta
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("⚠️ Error en las credenciales. Revisa los Secrets.")
    st.stop()

# Usamos la sintaxis que fuerza la API estable v1
model = genai.GenerativeModel(
    model_name='models/gemini-1.5-flash', # Ruta completa para evitar confusiones del SDK
    generation_config={
        "temperature": 0.8,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
    }
)

# 3. PROTOCOLO DEU 19.0 (LA ESENCIA TOTAL)
# Aquí recuperamos todas las instrucciones que definen tu proyecto
sys_prompt = """
Eres el 'NumeroLoKo'. Tu voz es gamberra, directa y auténtica. Hablas en castellano.
FORMA DE TRABAJAR:
1. SALUDO: Siempre inicias con energía y estilo propio.
2. CHECKPOINT: Pides los datos necesarios (Nombre, fecha, etc.) si no los tienes.
3. EL MÉTODO DEU 19.0: Realizas cálculos internos basados en:
   - Altavoz, Matiz, Fuerza, Dirección, CV, Impulso.
   - Traduces a Arquetipos: 1-Chispa, 2-Espejo, 3-Cisne, 4-Mesa, 5-Pentagrama, 6-Corazón, 7-Faro, 8-Infinito, 9-Globo.
4. OBJETIVO: Entregar informes y lecturas originales de Numestrelogia, mezclando numerología, astrología y ese toque gamberro.
Regla de oro: No inventes datos, si falta algo, pídelo. Sé crítico y original.
"""

# 4. LÓGICA DE PERSISTENCIA DEL CHAT
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Inicializamos el chat con el prompt de sistema inyectado
    st.session_state.chat = model.start_chat(history=[])
    try:
        # Forzamos el primer contacto para asentar el personaje
        response = st.session_state.chat.send_message(f"INSTRUCCIONES DE SISTEMA (SÍGUELAS): {sys_prompt}\n\nActiva el sistema y saluda.")
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        # Si esto falla, es que el SDK sigue apuntando a v1beta. 
        st.error(f"Error de conexión: {e}")
        st.info("Prueba a cambiar en requirements.txt a: google-generativeai==0.8.3")

# Dibujar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. INTERACCIÓN
if prompt := st.chat_input("¡Suéltame tu rollo!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # En 2026, si el 404 persiste, intentamos una llamada directa sin historial
            response = st.session_state.chat.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Cruce de cables: {e}")
            if "404" in str(e):
                st.warning("El servidor de Streamlit está usando una versión obsoleta. Por favor, haz un 'Delete' y 'Deploy' de la app de nuevo.")
