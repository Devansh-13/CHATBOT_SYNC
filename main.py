import random
import speech_recognition as sr
from gtts import gTTS
import os

# Define a dictionary of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well.", "All good!"],
    "what's your name": ["I'm a chatbot.", "You can call me Bot.", "I don't have a name."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure what you're saying.", "Could you please rephrase that?", "I'm still learning."]
}


def get_response(user_input):
    user_input = user_input.lower()

    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])


# Initialize the recognizer
recognizer = sr.Recognizer()

print("Chatbot: Hi! I'm a simple chatbot. Say 'bye' to exit.")
while True:
    with sr.Microphone() as source:
        print("Speak something:")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)

        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input)
        print("Chatbot:", response)

        # Convert response to speech
        response_tts = gTTS(text=response, lang='en')
        response_tts.save("response.mp3")
        os.system("start response.mp3")

    except sr.UnknownValueError:
        print("Chatbot: Sorry, I couldn't understand that.")
    except sr.RequestError as e:
        print(f"Chatbot: Could not request results from Google Speech Recognition service; {e}")
