from tkinter import *
from tkinter import ttk


class DiscussionList:
    def __init__(self, frame):
        self.frame = frame
        self.new_chat = None
        self.list_contacts = None
        self.create_widgets()


    def create_widgets(self):
        contacts = ["Alice", 'Bob',"Charlie","eu"]

        self.new_chat = Button(self.frame, text="New Chat", bg="cadetblue", fg="white", font=("Arial", 16, "bold"))
        self.new_chat.pack(fill=X, padx=10)

        def add_contact():
            self.list_contacts.insert(self.list_contacts.size(), self.add_contact_box.get())
            self.list_contacts.confing(height=self.list_contacts.size())

        self.list_contacts = ttk.Treeview(self.frame, selectmode="browse")
        self.list_contacts.pack(fill=BOTH, expand=True, padx=10, pady=10)
        for contact in contacts:
            self.list_contacts.insert("", END, text=contact)

        self.add_contact_box = Entry(self.frame)
        self.add_contact_box.pack(fill=BOTH, padx=10,pady=10)

        self.add_contact_btn = Button(self.frame, text="Add Contact", bg="cadetblue", fg="white", font=("Arial", 16, "bold"), command=add_contact)
        self.add_contact_btn.pack(fill=X, padx=10)