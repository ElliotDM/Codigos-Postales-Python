from tkinter import Tk, ttk, StringVar, Text, messagebox, filedialog
from tkinter import RAISED, HORIZONTAL, END
from main import make_dict, get_data, make_file


class Interface():
    def __init__(self):
        self.dict_list = make_dict()

        self.root = Tk()
        self.root.title('Codigos Postales')
        self.root.iconbitmap('icons\\zip-code.ico')
        self.root.resizable(0,0)

        self.frame = ttk.Frame(self.root, borderwidth=2, relief=RAISED, padding=(5,5))

        self.label1 = ttk.Label(self.frame, text='Nombre:', padding=(5,5))
        self.label2 = ttk.Label(self.frame, text='C.P.:', padding=(5,5))

        self.name = StringVar()
        self.cp = StringVar()

        self.textbox1 = ttk.Entry(self.frame, textvariable=self.name, width=30)
        self.textbox2 = ttk.Entry(self.frame, textvariable=self.cp, width=30)

        self.label3 = ttk.Label(self.frame, text='Colonia:', padding=(5,5))
        self.combobox = ttk.Combobox(self.frame, width=27, state='readonly')

        self.button1 = ttk.Button(self.frame, text='Buscar', padding=(5,5), command=self.search)
        self.button2 = ttk.Button(self.frame, text='Aceptar', padding=(5,5), state='disable', command=self.make_selection)

        self.separator = ttk.Separator(self.frame, orient=HORIZONTAL)

        self.label4 = ttk.Label(self.frame, text='Previsualizacion', padding=(5,5))
        
        self.textarea = Text(self.frame, height=10, width=30, padx=5, pady=5, state='disable')

        self.button3 = ttk.Button(self.frame, text='Guardar', padding=(5,5), state='disable', command=self.choose_dir)

        self.frame.grid(row=0, column=0)
        self.label1.grid(row=0, column=0)
        self.textbox1.grid(row=0, column=1, columnspan=3)
        self.label2.grid(row=1, column=0)
        self.textbox2.grid(row=1, column=1, columnspan=3)
        self.label3.grid(row=3, column=0)
        self.combobox.grid(row=3, column=1, columnspan=3)
        self.button1.grid(row=4, column=1)
        self.button2.grid(row=4, column=2)
        self.separator.grid(row=6, columnspan=3, sticky='we', pady=(5,5))
        self.label4.grid(row=7, column=1)
        self.textarea.grid(row=8, column=0, columnspan=3)
        self.button3.grid(row=10, column=1, pady=(5,5))

        self.textbox1.focus_set()
        self.root.mainloop() 

    def search(self):
        if self.name.get() == '' or self.cp.get() == '':
            messagebox.showerror('Error', 'Ingrese sus datos')
            return

        data = get_data(self.cp.get(), self.dict_list)

        if data == []:
            messagebox.showerror('Error', 'Codigo postal no encontrado')
            return

        self.combobox.configure(postcommand=self.add_options(data), state='readonly')
        self.button2.configure(state='enable')
        

    def make_selection(self):
        if self.combobox.get() == '':
            messagebox.showerror('Error', 'Ingrese su colonia')
            return
        
        data = get_data(self.cp.get(), self.dict_list)
        fun = lambda x: True if x.get('d_asenta') == self.combobox.get() else False
        selection = list(filter(fun, data)).pop()

        colonia = selection.get('d_asenta')
        estado = selection.get('d_estado')
        municipio = selection.get('d_mnpio')
        ciudad = selection.get('d_ciudad')

        self.textarea.configure(state='normal')
        self.textarea.delete('1.0', END)
    
        if selection.get('d_ciudad') == '':
            self.textarea.configure(state='normal')
            self.textarea.insert('1.0', f'Nombre: {self.name.get()}\nC.P.: {self.cp.get()}\nColonia: {colonia}\nEstado: {estado}\nMunicipio: {municipio}')

            self.textarea.configure(state='disable')
            self.button3.configure(state='enable')

            return

        self.textarea.configure(state='normal')
        self.textarea.insert('1.0', f'Nombre: {self.name.get()}\nC.P.: {self.cp.get()}\nColonia: {colonia}\nEstado: {estado}\nMunicipio: {municipio}\nCiudad: {ciudad}')
        
        self.textarea.configure(state='disable')
        self.button3.configure(state='enable')
        
    def add_options(self, data:list):
        colonias = [data[idx].get('d_asenta') for idx in range(len(data))]
        self.combobox['values'] = colonias

    def choose_dir(self):
        parent_dir = filedialog.askdirectory()
        data = self.textarea.get('1.0', END)
        make_file(self.name.get(), self.cp.get(), data, parent_dir)

        self.button2.configure(state='disable')
        self.button3.configure(state='disable')
        self.combobox.set('')


def main():
    app = Interface()


if __name__ == '__main__':
    main()
