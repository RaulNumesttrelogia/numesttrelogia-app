import google.generativeai as genai
import streamlit as st

# 1. CONFIGURACIÓN VISUAL
st.set_page_config(page_title="NumesTTrelogia DEU 19.0", page_icon="🌀")
st.title("🌀 NumesTTrelogia")
st.markdown("### El NumeroLoKo: Sistema DEU 19.0")

# 2. CONFIGURACIÓN DEL MOTOR
# Extraemos la clave de los secretos de Streamlit
API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=API_KEY)

# Eliminamos typical_p y usamos la sintaxis estable para 2026
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash', # En versión estable, sin prefijos innecesarios
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
    # Iniciamos el chat con el historial vacío
    st.session_state.chat = model.start_chat(history=[])
    try:
        # Enviamos el prompt de sistema como primer mensaje oculto para setear el rol
        response = st.session_state.chat.send_message(f"{sys_prompt}\n\nActiva el sistema y saluda.")
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error de conexión con el NumeroLoKo: {e}")

# Renderizado de mensajes
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
            # Respuesta del modelo
            response = st.session_state.chat.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Cruces de cables... {e}")
