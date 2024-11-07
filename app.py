import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="broker.mqttdashboard.com"
port=1883
#client1= paho.Client("GIT-HUB")
#client1.on_message = on_message



st.title("Música")
st.subheader("Tristeza")


if st.button('ON',key="1"):
    act1="ON"
    client1= paho.Client("GIT-HUB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_s_Camila", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('OFF',key="2"):
    act1="OFF"
    client1= paho.Client("GIT-HUB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_s_Camila", message)
  
    
else:
    st.write('')


st.subheader("Romántico")



if st.button('ON',key="3"):
    act1="ON"
    client1= paho.Client("GIT-HUB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_s_Camila", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('OFF',key="4"):
    act1="OFF"
    client1= paho.Client("GIT-HUB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_s_Camila", message)
  
    
else:
    st.write('')


st.subheader("Felicidad")



if st.button('ON',key="5"):
    act1="ON"
    client1= paho.Client("GIT-HUB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_s_Camila", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('OFF',key="6"):
    act1="OFF"
    client1= paho.Client("GIT-HUB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_s_Camila", message)
  
    
else:
    st.write('')


st.subheader("Meditación")



if st.button('ON',key="7"):
    act1="ON"
    client1= paho.Client("GIT-HUB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_s_Camila", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('OFF',key="8"):
    act1="OFF"
    client1= paho.Client("GIT-HUB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_s_Camila", message)
  
    
else:
    st.write('')


if st.button("Atras"):
    st.link_button("Home", "https://proyecto-final-ztvtetttkapfwq74usy7u6.streamlit.app/")



