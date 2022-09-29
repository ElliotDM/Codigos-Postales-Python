from tkinter import *
from tkinter import Tk, ttk, StringVar

class Interface():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Codigos Postales")
        self.root.resizable(0,0)

        self.frame = ttk.Frame(self.root, borderwidth=2, 
                    relief="raised", padding=(10,10))

        self.label1 = ttk.Label(self.frame, text='Ingrese su nombre:')
        self.label2 = ttk.Label(self.frame, text='Ingrese su codigo postal:')

        self.name = StringVar()
        self.cp = StringVar()

        self.textbox1 = ttk.Entry(self.frame, textvariable=self.name, width=30)
        self.textbox2 = ttk.Entry(self.frame, textvariable=self.cp, width=30)

        self.separator = ttk.Separator(self.frame, orient=HORIZONTAL)

        self.button = ttk.Button(self.frame, text='Buscar')

        self.frame.grid(column=0, row=0)
        self.label1.grid(column=0, row=0)
        self.textbox1.grid(column=0,row=1, columnspan=2)
        self.label2.grid(column=0, row=2)
        self.textbox2.grid(column=0, row=3, columnspan=2)
        self.separator.grid(column=0,row=4, columnspan=3)
        self.button.grid(column=0,row=5)

        self.textbox1.focus_set()
        self.root.mainloop() 


def main():
    app = Interface()


if __name__ == "__main__":
    main()