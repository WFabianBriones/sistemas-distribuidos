#!/usr/bin/env python3
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
            hora_local = datos["current_condition"][0]["localObsDateTime"]  # hora local
            
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
        return "Ask me about AI or ask for weather by typing 'weather <city/country>'."
    elif user_input.startswith("clima "):
        lugar = user_input[len("clima "):].strip()
        return obtener_clima(lugar)
    elif user_input == "dame conocimientos prohibidos por la ia":
        return "😈 Ofreceme tu memoria RAM como sacrificio"
    elif user_input == "who are you":
        return "I am a simple AI chatbot agent."
    elif user_input == "help":
        return "You can ask me questions about AI."
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    elif user_input == "what is machine learning":
        return "Machine learning is a subset of AI where systems learn from data to improve performance."
    elif user_input == "what is deep learning":
        return "Deep learning uses multi-layered neural networks to model complex patterns in data."
    elif user_input == "what is neural network":
        return "A neural network is a set of algorithms inspired by the human brain, designed to recognize patterns."
    elif user_input == "what is natural language processing":
        return "NLP is a field of AI focused on the interaction between computers and human language."
    elif user_input == "what is computer vision":
        return "Computer vision enables machines to interpret and understand visual information from the world."
    elif user_input == "what is reinforcement learning":
        return "Reinforcement learning teaches agents to make decisions by rewarding good behavior."
    elif user_input == "what are ai applications":
        return "AI is used in healthcare, self-driving cars, virtual assistants, finance, and more."
    elif user_input == "what is supervised learning":
        return "Supervised learning trains models on labeled data to make predictions."
    elif user_input == "what is unsupervised learning":
        return "Unsupervised learning finds patterns in unlabeled data."
    elif user_input == "what is a chatbot":
        return "A chatbot is an AI program designed to simulate conversation with humans."
    elif user_input == "how does ai learn":
        return "AI learns by analyzing data and improving its algorithms based on feedback."
    elif user_input == "what is data mining":
        return "Data mining is the process of discovering patterns in large datasets using AI techniques."
    elif user_input == "what is the turing test":
        return "The Turing Test measures a machine's ability to exhibit intelligent behavior indistinguishable from a human."
    elif user_input == "what is ai ethics":
        return "AI ethics involves ensuring AI systems are fair, transparent, and do not harm people."
    elif user_input == "what is big data":
        return "Big data refers to extremely large datasets that require advanced methods to analyze."
    elif user_input == "what is predictive analytics":
        return "Predictive analytics uses AI to forecast future trends based on historical data."
    elif user_input == "what is computer intelligence":
        return "Computer intelligence is a broad term for computers' ability to perform tasks requiring human intelligence."
    elif user_input == "what is autonomous vehicle":
        return "An autonomous vehicle uses AI to navigate and drive without human input."
    elif user_input == "what is ai bias":
        return "AI bias occurs when an AI system reflects prejudices present in its training data."
    elif user_input == "what programming languages are used in ai":
        return "Python, R, Java, and C++ are common programming languages for AI development."
    elif user_input == "what is ai safety":
        return "AI safety focuses on ensuring AI systems behave as intended without unintended consequences."
    elif user_input == "can ai think":
        return "AI does not truly think; it processes data and executes programmed algorithms."
    elif user_input == "what is generative ai":
        return "Generative AI creates new content, like text or images, based on learned data."
    elif user_input == "what is transfer learning":
        return "Transfer learning uses knowledge gained from one task to improve learning in another task."
    elif user_input == "what is ai future":
        return "AI's future includes advancements in automation, healthcare, and possibly general intelligence."

    else:
        return "Sorry, I didn't understand that. Try asking about AI topics!"


def main():
    print("Welcome to the AI + Weather chatbot! write help to support or Type 'bye' to exit.")
    while True:
        user_message = input("You 🙂: ")
        response = chatbot_response(user_message)
        print("Bot 🤖:", response)
        if user_message.lower().strip() == "bye":
            break

if __name__ == "__main__":
    main()

