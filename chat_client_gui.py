import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)

client_socket.connect(server_address)

def send_message():
    message = client_entry.get()
    if message:
        client_socket.send(message.encode())
        client_entry.delete(0, tk.END)

def receive_message():
    while True:
        try:
            message = client_socket.recv(1024)
            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, message.decode() + '\n')
            chat_window.config(state=tk.DISABLED)
        except:
        
            client_socket.close()
            break

client_gui = tk.Tk()
client_gui.title("Chat Client")

chat_window = scrolledtext.ScrolledText(client_gui, state=tk.DISABLED)
chat_window.pack()

client_entry = tk.Entry(client_gui)
client_entry.pack()

send_button = tk.Button(client_gui, text="Send", command=send_message)
send_button.pack()

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

client_gui.mainloop()
