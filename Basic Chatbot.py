import tkinter as tk
from tkinter import scrolledtext
import random

# Bot response function
def get_bot_reply(msg):
    msg_clean = msg.lower().strip()

    if msg_clean in ["hi", "hello", "hey"]:
        return "Hi! How are you today?"
    elif msg_clean in ["how are you", "how are you?"]:
        return "I'm good, thanks! How about you?"
    elif msg_clean in ["i'm fine", "im fine", "fine", "i am fine"]:
        return "Glad to hear! How's your day going?"
    elif msg_clean in ["bye", "goodbye", "quit"]:
        return "Bye! Talk to you later!"
    else:
        fallback = [
            "Interesting! Tell me more.",
            "I see. Can you explain a bit?",
            "That's cool! What else?",
            "Hmm, I didn't know that. Go on.",
            "Nice! Do you want to chat more?"
        ]
        return random.choice(fallback)

# Function to handle sending messages
chat_count = 0
max_chats = 10

def send_message():
    global chat_count
    user_msg = entry.get().strip()
    if not user_msg:
        return
    chat_window.config(state='normal')
    chat_window.insert(tk.END, f"You: {user_msg}\n")
    entry.delete(0, tk.END)

    bot_msg = get_bot_reply(user_msg)
    chat_window.insert(tk.END, f"Bot: {bot_msg}\n")
    chat_window.config(state='disabled')
    chat_window.yview(tk.END)

    chat_count += 1
    if user_msg.lower() in ["bye", "goodbye", "quit"] or chat_count >= max_chats:
        entry.config(state='disabled')
        send_button.config(state='disabled')
        chat_window.config(state='normal')
        chat_window.insert(tk.END, "\nChat ended.\n")
        chat_window.config(state='disabled')

# GUI setup
root = tk.Tk()
root.title("Chatbot")
root.geometry("400x500")

chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=(0,10), side=tk.LEFT, fill=tk.X, expand=True)
entry.focus()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=(0,10), pady=(0,10), side=tk.RIGHT)

# Bind Enter key to send message
root.bind('<Return>', lambda event: send_message())

root.mainloop()