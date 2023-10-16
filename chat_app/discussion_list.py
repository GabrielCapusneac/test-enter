from tkinter import *
from tkinter import ttk
import json


class DiscussionList:
    def __init__(self, frame):
        self.frame = frame
        self.new_chat = None
        self.list_contacts = None
        self.create_widgets()


    def create_widgets(self):
        contacts = ["Alice", 'Bob',"Charlie","eu"]

        self.new_chat = Button(self.frame, text="New Chat", bg="cadetblue", fg="white", font=("Arial", 16, "bold"), command=self.new_chat_window)
        self.new_chat.pack(fill=X, padx=10)

        #self.label_disscusions = Label(self.frame, text=)

        self.list_contacts = ttk.Treeview(self.frame, selectmode="browse")
        self.list_contacts.pack(fill=BOTH, expand=True, padx=10, pady=10)
        self.list_contacts.heading("#0", text="Disscusions")
        for contact in contacts:
            self.list_contacts.insert("", 'end', text=contact)

    def new_chat_window(self):
        self.chat_select_window = Tk()
        self.chat_select_window.title("New Chat")
        self.chat_select_window.geometry("400x400")
        self.chat_select_window.pack()


    #    self.add_contact_box = Entry(self.frame)
    #    self.add_contact_box.pack(fill=BOTH, padx=10,pady=10)

    #    self.add_contact_btn = Button(self.frame, text="Add Contact", bg="cadetblue", fg="white", font=("Arial", 16, "bold"), command=self.add_contact)
    #    self.add_contact_btn.pack(fill=X, padx=10)

    #def add_contact(self):
    #    new_contact = self.add_contact_box.get()
    #    self.list_contacts.insert("", END, text=new_contact)
    #    self.list_contacts.config(height=self.list_contacts.size())
    #    self.add_contact_box.delete("1.0", END)

    def load_data(self, path):
        with open(path, "r") as file:
            data = json.load(file)
        return data

    contacte = load_data("D:\\CapusneacGabriel\\Chat_app\\contacts.json")
    print(contacte)


