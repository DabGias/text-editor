from tkinter import Tk, Text, Scrollbar
from menu_bar import MenuBar

class TextEditor:

    def __init__(self, root: Tk):
        root.title("untitled")
        root.geometry("1200x700")

        self.file: str = None
        self.textarea: Text = Text(
            root,
            tabs=40,
            font=("Cascadia Code", 12), 
            borderwidth=0, 
            wrap="none",
            background="#262736",
            foreground="#FFFFFF",
            blockcursor=True, 
            insertbackground="white", 
            insertborderwidth=0,
            insertofftime=500,
            insertontime=500
        )
        self.yscroll: Scrollbar = Scrollbar(
            root, 
            command=self.textarea.yview, 
            orient="vertical", 
            background="#262736", 
            activebackground="#42445c"
        )
        self.xscroll: Scrollbar = Scrollbar(
            root, 
            command=self.textarea.xview, 
            orient="horizontal", 
            background="#262736",
            activebackground="#42445c"
        )

        self.xscroll.pack(side="bottom", fill="x")
        self.yscroll.pack(side="right", fill="y")

        self.textarea.config(yscrollcommand=self.yscroll.set, xscrollcommand=self.xscroll.set)
        self.textarea.pack(side="left", fill="both", expand=True)

        self.menubar: MenuBar = MenuBar(root, self.file, self.textarea)

