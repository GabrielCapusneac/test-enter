from tkinter import *
from tkinter import ttk

from chat_app.discussion_list import DiscussionList
from chat_app.messages import Messages


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.discussion_frame = None
        self.discussion_list = None

        self.messages_frame = None
        self.messages_part = None

    def create_widgets(self):
        self.discussion_frame = Frame(self.root, bg="thistle", padx=10, pady=10)
        self.discussion_list = DiscussionList(self.discussion_frame)
        self.discussion_frame.pack(side=LEFT, fill=Y)

        self.messages_frame = Frame(self.root, bg="thistle", padx=10, pady=10)
        self.messages_part = Messages(self.messages_frame)
        self.messages_frame.pack(side=RIGHT, fill=BOTH, expand=True)







