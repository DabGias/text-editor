from tkinter import Tk, Menu, Text, END, filedialog

class MenuBar:

    def __init__(self, root: Tk, file: str, textarea: Text):
        self.root: Tk = root
        self.file: str = file
        self.textarea: Text = textarea
        self.menubar: Menu = Menu(root, font=("Cascadia Code", 11))

        file_dropdown: Menu = Menu(self.menubar, font=("Cascadia Code", 11), tearoff=0)

        file_dropdown.add_command(label="New File", command=self.new_file, accelerator="Ctrl + N")
        file_dropdown.add_command(label="Open File", command=self.open_file, accelerator="Ctrl + O")
        file_dropdown.add_command(label="Save", command=self.save_file, accelerator="Ctrl + S")
        file_dropdown.add_command(label="Save As", command=self.save_as, accelerator="Ctrl + Shift + S")
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit")

        self.menubar.add_cascade(label="File", menu=file_dropdown)

        self.textarea.bind("<Control-n>", self.new_file)
        self.textarea.bind("<Control-o>", self.open_file)
        self.textarea.bind("<Control-s>", self.save_file)
        self.textarea.bind("<Control-S>", self.save_as)

        self.root.config(menu=self.menubar)

    def save_file(self, *args):
        if self.file is None:
            self.file = filedialog.asksaveasfilename(initialfile="*.txt", filetypes=[("All Files", "*.*")]).strip()

            if self.file != "": 
                self.root.title(self.file.split("/")[-1])

                with open(self.file, "w") as f:
                    f.write(self.textarea.get(0.0, END))

                    f.close()
        else:
            with open(self.file, "w") as f:
                f.write(self.textarea.get(0.0, END))

                f.close()

    def save_as(self, *args):
        self.file = filedialog.asksaveasfilename(initialfile="*.txt", filetypes=[("All Files", "*.*")]).strip()

        if self.file != "": 
            self.root.title(self.file.split("/")[-1])

            with open(self.file, "w") as f:
                f.write(self.textarea.get(0.0, END))

                f.close()

    def open_file(self, *args):
        self.file = filedialog.askopenfilename(filetypes=[("All Files", "*.*")]).strip()

        if self.file != "":
            self.root.title(self.file.split("/")[-1])
            self.textarea.delete(0.0, END)

            with open(self.file, "r") as f:
                self.textarea.insert(0.0, f.read())

                f.close()

    def new_file(self, *args):
        self.file = None
        self.textarea.delete(0.0, END)
        self.root.title("untitled")
