import google.generativeai as genai
import streamlit as st

# 1. CONFIGURACIÓN VISUAL
st.set_page_config(page_title="NumesTTrelogia DEU 19.0", page_icon="🌀")
st.title("🌀 NumesTTrelogia")
st.markdown("### El NumeroLoKo: Sistema DEU 19.0")

# 2. CONFIGURACIÓN DEL MOTOR
# Asegúrate de que en Streamlit Cloud tengas la clave como GOOGLE_API_KEY
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("Falta la API KEY en los Secrets de Streamlit.")
    st.stop()

# Configuración del modelo sin parámetros conflictivos (como typical_p)
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
    }
)

# 3. PROTOCOLO DEU 19.0
sys_prompt = """
Actúa como el 'NumeroLoKo'. Voz gamberra y directa. 
Regla 1: Saludo inicial fijo. 
Regla 2: Checkpoint de confirmación de datos. 
Regla 3: Cálculos matemáticos internos (Altavoz, Matiz, Fuerza, Dirección, CV, Impulso).
Regla 4: Traducción a Arquetipos (1-Chispa, 2-Espejo, etc.).
"""

# 4. LÓGICA DEL CHAT
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Iniciamos el chat
    st.session_state.chat = model.start_chat(history=[])
    try:
        # El primer mensaje configura el comportamiento del NumeroLoKo
        response = st.session_state.chat.send_message(f"{sys_prompt}\n\nActiva el sistema y saluda.")
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error de conexión con el NumeroLoKo: {e}")

# Mostrar el historial de mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada del usuario
if prompt := st.chat_input("¡Suéltame tu rollo!"):
    # Añadir mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta del asistente
    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat.send_message(prompt)
            respuesta_texto = response.text
            st.markdown(respuesta_texto)
            st.session_state.messages.append({"role": "assistant", "content": respuesta_texto})
        except Exception as e:
            st.error(f"Cruces de cables... {e}")
            st.button("Reiniciar sistema", on_click=lambda: st.session_state.clear())
