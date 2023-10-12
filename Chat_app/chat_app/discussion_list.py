from tkinter import *
from tkinter import ttk


class DiscussionList:
    def __init__(self, frame):
        self.frame = frame
        self.new_chat = None
        self.list = None
        self.create_widgets()


    def create_widgets(self):
        names = ["Alice", 'Bob',"Charlie"]

        self.new_chat = Button(self.frame, text="New Chat", bg="cadetblue", fg="white", font=("Arial", 16, "bold"))
        self.new_chat.pack(fill=X, padx=10)

        self.list = ttk.Treeview(self.frame, selectmode="browse")
        self.list.pack(fill=BOTH, expand=True, padx=10, pady=10)
        for name in names:
            self.list.insert("", END, text=name)