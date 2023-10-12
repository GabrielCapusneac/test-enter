from tkinter import *
from tkinter import ttk


class Messages:
    def __init__(self, frame):
        self.frame = frame
        self.chat = None
        self.text_input = None
        self.send_btn = None
        self.create_widgets()

    def create_widgets(self):
        self.chat = Text(self.frame, bg="cadetblue", fg="white", state="normal", cursor="arrow", font=('Times', 10, 'italic bold'))
        self.chat.pack(fill=BOTH, expand=True, padx=10, pady=10)

        def send_btn(event):
            print(event)


        self.text_input = Text(self.frame, height=3)
        self.text_input.pack(fill=X, padx=10, pady=10)
        self.text_imput.bind('<Return>', send_btn)

        self.send_btn = Button(self.frame, text="SEND", command=self.submit, font=("Arial", 10, "bold"), bg="teal", fg="white")
        self.send_btn.pack(side=RIGHT, padx=10, pady=10)


    def submit(self):
        current_message = self.text_input.get("1.0", "end")
        self.chat.insert("1.0", f"{current_message}")