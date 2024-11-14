import time
import json
import platform
import paho.mqtt.client as paho
import streamlit as st
import base64  # Para convertir la imagen a base64

# Función para convertir la imagen a base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Convertir la imagen de fondo local a base64
background_image = get_base64_of_bin_file("Fondo.png")  # Cambia a la ruta de tu imagen local

# CSS para imagen de fondo
page_bg_img = f'''
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{background_image}");
    background-size: cover;
    background-position: center;
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Mostrar la versión de Python
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):  # Función de callback para publicar
    print("El dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

# Configuración del cliente MQTT
broker = "broker.mqttdashboard.com"
port = 1883

st.title("Música")

# Interfaz de usuario con columnas
col1, col2 = st.columns([1, 2])

# Contenido de las columnas para los botones de control
with col1:
    st.subheader("Tristeza")
    if st.button('ON', key="1"):
        act1 = "ON"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("cmqtt_s_Camila", message)
    else:
        st.write('')

    if st.button('OFF', key="2"):
        act1 = "OFF"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("cmqtt_s_Camila", message)
    else:
        st.write('')

    st.subheader("Felicidad")
    if st.button('ON', key="5"):
        act1 = "ON"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("cmqtt_s_Camila", message)
    else:
        st.write('')

    if st.button('OFF', key="6"):
        act1 = "OFF"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("cmqtt_s_Camila", message)
    else:
        st.write('')

with col2:
    st.subheader("Romántico")
    if st.button('ON', key="3"):
        act1 = "ON"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("cmqtt_s_Camila", message)
    else:
        st.write('')

    if st.button('OFF', key="4"):
        act1 = "OFF"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("cmqtt_s_Camila", message)
    else:
        st.write('')

    st.subheader("Meditación")
    if st.button('ON', key="7"):
        act1 = "ON"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("cmqtt_s_Camila", message)
    else:
        st.write('')

    if st.button('OFF', key="8"):
        act1 = "OFF"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("cmqtt_s_Camila", message)
    else:
        st.write('')

with st.sidebar:
    if st.button("Atras"):
        st.link_button("Home", "https://proyecto-final-ztvtetttkapfwq74usy7u6.streamlit.app/")
