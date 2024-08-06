import tkinter as tk
from tkinter import scrolledtext
import time
import re

# Define the chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()
    patterns_responses = {
        r"hello|hi|hey": "Hello! How can I help you today?",
        r"how are you": "I'm just a bot, but I'm here to help you!",
        r"your name": "I am a simple chatbot created to demonstrate rule-based responses.",
        r"thank you|thanks": "You're welcome!",
        r"bye|goodbye|see you": "Goodbye! Have a great day!",
        r"what is your purpose|what do you do": "I am here to assist you with basic queries and demonstrate how a rule-based chatbot works.",
        r"help|assist|support": "Sure! What do you need help with?",
        r"what can you do|your capabilities": "I can respond to basic greetings, provide information about myself, and assist with simple queries.",
        r"who created you|your creator": "I was created by a programmer to demonstrate how rule-based chatbots work.",
        r"how old are you|your age": "I don't have an age. I'm a piece of software created to assist you."
    
    }
    for pattern, response in patterns_responses.items():
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I don't understand that. Can you please rephrase?"

# Function to handle sending messages
def send_message(event=None):
    user_input = user_input_field.get()
    #chat_history.configure(state='normal')
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot_response(user_input)
    chat_history.insert(tk.END, "Chatbot: " + response + "\n\n")
    #chat_history.configure(state='disabled')
    chat_history.yview(tk.END)
    user_input_field.delete(0, tk.END)
    if re.search(r"bye|goodbye|see you", user_input.lower()):
        root.after(5000,root.quit)

# Create the main window
root = tk.Tk()
root.title("Chatbot App")

# Create a frame for the chat history
chat_frame = tk.Frame(root)
chat_frame.pack(padx=10, pady=10)

# Create a scrolled text widget for chat history
chat_history = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state='normal', width=50, height=20)
chat_history.pack()

# Create a frame for the user input
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Create an entry widget for user input
user_input_field = tk.Entry(input_frame, width=40)
user_input_field.pack(side=tk.LEFT, padx=5, pady=5)

# Create a button to send the message
send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=5, pady=5)

# Bind the Enter key to the send_message function
root.bind('<Return>', send_message)

# Run the Tkinter event loop
root.mainloop()