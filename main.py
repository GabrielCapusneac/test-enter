from tkinter import *
from tkinter import ttk
from chat_app.main_window import MainWindow

if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    root.title("Chat App")
    root.config()
    window = MainWindow(root)
    window.create_widgets()
    root.mainloop()