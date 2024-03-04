from tkinter import Tk
from text_editor import TextEditor

if __name__ == "__main__":
    root: Tk = Tk()

    texteditor: TextEditor = TextEditor(root)

    root.mainloop()
