import socket
import threading
import tkinter as tk

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)
    
    global client_socket
    global client_address
    
    client_socket, client_address = server_socket.accept()
    
    chat_window.insert(tk.END, "Connection established with client.\n")

    receive_thread = threading.Thread(target=receive_message)
    receive_thread.start()

def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            chat_window.insert(tk.END, f"Client: {message}\n")
        except:
            chat_window.insert(tk.END, "Connection closed by client.\n")
            break

def send_message():
    message = server_entry.get()
    chat_window.insert(tk.END, f"Server: {message}\n")
    client_socket.send(message.encode())
    server_entry.delete(0, tk.END)

server_gui = tk.Tk()
server_gui.title("Chat Server")

chat_window = tk.Text(server_gui)
chat_window.pack()

server_entry = tk.Entry(server_gui)
server_entry.pack()

send_button = tk.Button(server_gui, text="Send", command=send_message)
send_button.pack()

start_server_button = tk.Button(server_gui, text="Start Server", command=start_server)
start_server_button.pack()

server_gui.mainloop()
 