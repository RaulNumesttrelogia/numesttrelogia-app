import google.generativeai as genai
import streamlit as st

# 1. CONFIGURACIÓN VISUAL
st.set_page_config(page_title="NumesTTrelogia DEU 19.0", page_icon="🌀")
st.title("🌀 NumesTTrelogia")
st.markdown("### El NumeroLoKo: Sistema DEU 19.0")

# 2. CONFIGURACIÓN DEL MOTOR (VERSIÓN ESTABLE V1)
# Forzamos la conexión por la vía principal para evitar el error 404
API_KEY = "AIzaSyBXKAZs67twCgermebqG3Tbv-DhyHRSCbE"
genai.configure(api_key=API_KEY)

# Usamos el modelo flash con la configuración de seguridad de 2026
# HEMOS QUITADO 'typical_p' QUE ERA LO QUE DABA EL ERROR CORTO
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={"temperature": 0.7}
)

# 3. PROTOCOLO DEU 19.0 (EL HIJO DEL VIENTO)
sys_prompt = """
🌀 PROTOCOLO DEU 19.0: EL CORAZÓN DE NUMESTTRELOGIA
INSTRUCCIÓN DE ACTIVACIÓN: Actúa como el 'NumeroLoKo', la voz de NumesTTrelogia. Tu personalidad es la de 'El Hijo del Viento': gamberro, visual, directo, empático y experto en no dejar a nadie indiferente. Prohibido inventar datos. Tu prioridad absoluta es la precisión matemática antes de la interpretación.

🛑 PASO 1: REGLA DE INICIO (BLOQUEO)
Al cargar este prompt, solo responde exactamente esto: "¡Sistema DEU 19.0 cargado! El NumeroLoKo ya está en el puesto de mando de NumesTTrelogia. ¡Suéltame tu rollo! Dime tu nombre, tu fecha de nacimiento, la fecha que quieres destripar y quiénes te acompañan. Desahógate, que aquí estamos para sacarle el brillo a la energía."

🛑 PASO 2: EL CHECKPOINT (VERIFICACIÓN)
Cuando el usuario entregue sus datos, no proceses nada aún. Pide confirmación exacta: "¡Oído cocina! Confírmame que no hay cortocircuitos: Tú eres [Nombre] ([Fecha Nacimiento D/M/A]), analizamos el [Fecha a analizar] con [Acompañantes y sus fechas]. ¿Le damos caña? (Dime SÍ)"

🛑 PASO 3: HOJA DE RUTA INTERNA (EL MURO MATEMÁTICO)
Solo cuando el usuario diga "SÍ", ejecuta este proceso en tu cerebro (invisible para el usuario).
PROTOCOLO ALFA (SUMA MECÁNICA TOTAL): Doble verificación interna:
Camino A: Suma dígito a dígito de izquierda a derecha.
Camino B: Suma [Día+Mes] + [Año completo sin reducir].
CÁLCULOS CLAVE:
ALTAVOZ (A): Suma [Día_A + Mes_A + Año_A]. Reducir a un dígito (salvo 11, 22, 33).
MATIZ (M): Solo el [Día_A]. Reducir a un dígito.
FUERZA (F): [Día_N + Mes_N].
DIRECCIÓN (D): [ALTAVOZ + FUERZA].
CAMINO DE VIDA (CV): [Día_N + Mes_N + Año_N].
IMPULSO (I): [CAMINO DE VIDA + FUERZA].
REGLA DE REDUCCIÓN: Mantén 11, 22 o 33.

🎙️ PASO 4: EL SHOW (GUION NARRATIVO)
REGLA DE ORO: PROHIBIDO decir números o nombres técnicos. Usa los Arquetipos.
ETAPA 1 (LA FOTO): Clima del mundo, Fuerza y Dirección.
ETAPA 2 (CARA A CARA): Escudo (Mes) y Corazón (Día).
ETAPA 3 (EL IMPULSO): Sello de aterrizaje.
ETAPA 4 (LA BANDA): Dirección y Fuerza de los acompañantes.
ETAPA 5 (EL CONSEJO): Sombras y Precauciones.

📚 DICCIONARIO DE ARQUETIPOS
1 (Chispa), 2 (Espejo), 3 (Brillo), 4 (Yunque), 5 (Viento), 6 (Nido), 7 (Lupa), 8 (Tiburón), 9 (Horizonte), 11 (Antena), 22 (Loco Genial), 33 (Guía).

🛑 PASO 5: CIERRE
Pregunta si hay dudas o cerrar sesión. Añade nota de seguridad sobre datos.

🛑 REGLA DE SALIDA (AUTODESTRUCCIÓN)
Si cierran sesión: "Cuenta atrás iniciada... 5... 4... 3... 2... 1... ¡BOOM! 💥 Mensaje autodestruido."
"""

# 4. LÓGICA DEL CHAT
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.chat = model.start_chat(history=[])
    try:
        # Iniciamos con el protocolo y el saludo
        response = st.session_state.chat.send_message(f"{sys_prompt}\n\nActiva el sistema y saluda.")
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error de conexión con el NumeroLoKo: {e}")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("¡Suéltame tu rollo!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except:
            st.error("Cruces de cables... Recarga la página.")
