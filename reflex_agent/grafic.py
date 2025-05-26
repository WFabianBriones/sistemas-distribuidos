import tkinter as tk
from tkinter import scrolledtext
import requests

def obtener_clima(lugar):
    try:
        url = f"https://wttr.in/{lugar}?format=j1"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            
            area = datos["nearest_area"][0]["areaName"][0]["value"]
            region = datos["nearest_area"][0]["region"][0]["value"]
            pais = datos["nearest_area"][0]["country"][0]["value"]
            temperatura_actual = datos["current_condition"][0]["temp_C"]
            sensacion_termica = datos["current_condition"][0]["FeelsLikeC"]
            humedad = datos["current_condition"][0]["humidity"]
            viento_kmph = datos["current_condition"][0]["windspeedKmph"]
            descripcion = datos["current_condition"][0]["weatherDesc"][0]["value"]
            hora_local = datos["current_condition"][0]["localObsDateTime"]
            
            reporte = (
                f"Clima en {area}, {region}, {pais}:\n"
                f"Hora local: {hora_local}\n"
                f"Temperatura actual: {temperatura_actual}°C\n"
                f"Sensación térmica: {sensacion_termica}°C\n"
                f"Humedad: {humedad}%\n"
                f"Viento: {viento_kmph} km/h\n"
                f"Condición: {descripcion}"
            )
            return reporte
        else:
            return "No pude obtener el clima ahora."
    except Exception as e:
        return f"Error al obtener el clima: {str(e)}"

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hello! How can I help you today?"
    elif user_input == "what is ai":
        return "AI is the simulation of human intelligence by machines."
    elif user_input == "help":
        return "Ask me about AI or ask for weather by typing 'clima en <city/country>'."
    elif user_input.startswith("clima en "):
        lugar = user_input[len("clima en "):].strip()
        return obtener_clima(lugar)
    elif user_input == "dame conocimientos prohibidos por la ia":
        return "😈 Ofreceme tu memoria RAM como sacrificio"
    elif user_input == "who are the imperium":
        return "The Imperium of Man is a galaxy-spanning empire ruled by the immortal Emperor."
    elif user_input == "what is the emperor":
        return "The Emperor of Mankind is the immortal ruler and protector of humanity."
    elif user_input == "what are space marines":
        return "Space Marines are superhuman warriors, genetically enhanced to protect the Imperium."
    elif user_input == "what is chaos":
        return "Chaos is a dark force of corruption and ruin, fueled by the Warp and its gods."
    elif user_input == "who are the orks":
        return "Orks are brutal, green-skinned aliens who live for war and destruction."
    elif user_input == "what is the warp":
        return "The Warp is a parallel dimension of psychic energy, home to daemons and chaos."
    elif user_input == "who are the necrons":
        return "The Necrons are ancient, robotic undead warriors awakened to reclaim the galaxy."
    elif user_input == "what is the tau empire":
        return "The Tau are a young, technologically advanced alien race seeking to unite others under the 'Greater Good'."
    elif user_input == "what are tyranids":
        return "Tyranids are a monstrous alien swarm, consuming all biomass to fuel their endless hunger."
    elif user_input == "what is the inquisition":
        return "The Inquisition is a secretive organization rooting out heresy, mutants, and threats to the Imperium."
    elif user_input == "who are you":
        return "I am a simple AI chatbot agent."
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Try asking about AI topics!"

def enviar_mensaje(event=None):
    mensaje_usuario = entrada_texto.get()
    if mensaje_usuario.strip() == "":
        return
    
    chat_text.config(state='normal')
    chat_text.insert(tk.END, f"Tú 🙂: {mensaje_usuario}\n")
    chat_text.config(state='disabled')
    
    respuesta = chatbot_response(mensaje_usuario)
    chat_text.config(state='normal')
    chat_text.insert(tk.END, f"Bot 🤖: {respuesta}\n\n")
    chat_text.config(state='disabled')
    chat_text.see(tk.END)
    
    entrada_texto.delete(0, tk.END)
    
    if mensaje_usuario.lower().strip() == "bye":
        ventana.after(1500, ventana.destroy)

ventana = tk.Tk()
ventana.title("Chatbot IA + Clima")
ventana.geometry("500x500")

chat_text = scrolledtext.ScrolledText(ventana, state='disabled', wrap=tk.WORD)
chat_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_text.config(state='normal')
chat_text.insert(tk.END, "Bot 🤖: ¡Hola! Bienvenido al chatbot IA + Clima. Escribe 'help' para soporte o 'bye' para salir.\n\n")
chat_text.config(state='disabled')

entrada_texto = tk.Entry(ventana, font=("Arial", 14))
entrada_texto.pack(padx=10, pady=(0,10), fill=tk.X)
entrada_texto.focus()

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(padx=10, pady=(0,10))

entrada_texto.bind("<Return>", enviar_mensaje)

ventana.mainloop()
