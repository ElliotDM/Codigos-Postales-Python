from tkinter import Tk, ttk, StringVar, Text
from tkinter import *
from main import get_data, make_dict


class Interface():
    def __init__(self):
        self.root = Tk()
        self.root.title("Codigos Postales")
        self.root.resizable(0,0)

        self.frame = ttk.Frame(self.root, borderwidth=2, 
                    relief="raised", padding=(10,10))

        self.label1 = ttk.Label(self.frame, text='Nombre:', padding=(5,5))
        self.label2 = ttk.Label(self.frame, text='C.P.:', padding=(5,5))

        self.name = StringVar()
        self.cp = StringVar()

        self.textbox1 = ttk.Entry(self.frame, textvariable=self.name, width=30)
        self.textbox2 = ttk.Entry(self.frame, textvariable=self.cp, width=30)

        self.button1 = ttk.Button(self.frame, text='Buscar', padding=(5,5), command=self.search)
        self.button2 = ttk.Button(self.frame, text='Crear archivo', padding=(5,5))

        self.textarea = Text(self.frame, height=10, width=30, padx=5, pady=5, state=DISABLED)

        self.frame.grid(column=0, row=0)
        self.label1.grid(column=0, row=0)
        self.textbox1.grid(column=1,row=0, columnspan=2)
        self.label2.grid(column=0, row=1)
        self.textbox2.grid(column=1, row=1, columnspan=2)
        self.button1.grid(column=1,row=3)
        self.button2.grid(column=2,row=3)
        self.textarea.grid(column=0, row=5, columnspan=3)

        self.textbox1.focus_set()
        self.root.mainloop() 

    def search(self):
        data = get_data(self.cp.get(), make_dict())
        colonia = data.get('d_asenta')
        estado = data.get('d_estado')
        municipio = data.get('d_mnpio')

        self.textarea.configure(state=NORMAL)
        self.textarea.delete('1.0', END)
    
        if not data.get('d_ciudad'):
            self.textarea.configure(state=NORMAL)
            self.textarea.insert('1.0', f'Nombre: {self.name.get()}\
                \nC.P.: {self.cp.get()}\nColonia: {colonia}\nEstado: {estado}\
                \nMunicipio: {municipio}')
            self.textarea.configure(state=DISABLED)
            
        ciudad = data.get('d_ciudad')

        self.textarea.configure(state=NORMAL)
        self.textarea.insert('1.0', f'Nombre: {self.name.get()}\
                \nC.P.: {self.cp.get()}\nColonia: {colonia}\nEstado: {estado}\
                \nMunicipio: {municipio}\nCiudad: {ciudad}')
        self.textarea.configure(state=DISABLED)


def main():
    app = Interface()


if __name__ == "__main__":
    main()