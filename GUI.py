from tkinter import *
from tkinter import Tk, ttk, StringVar, Text, filedialog, messagebox
from tkinter import font
from main import get_data, make_dict, make_file, check_directory


class Interface(ttk.Frame):
    def __init__(self):
        self.root = Tk()
        self.root.title('Codigos Postales')
        self.root.iconbitmap('icons\\zip-code.ico')
        self.root.resizable(0,0)

        self.frame = ttk.Frame(self.root, borderwidth=2, 
                    relief="raised", padding=(5,5))

        self.label1 = ttk.Label(self.frame, text='Nombre:', padding=(5,5))
        self.label2 = ttk.Label(self.frame, text='C.P.:', padding=(5,5))

        self.name = StringVar()
        self.cp = StringVar()

        self.textbox1 = ttk.Entry(self.frame, textvariable=self.name, width=30)
        self.textbox2 = ttk.Entry(self.frame, textvariable=self.cp, width=30)

        self.label3 = ttk.Label(self.frame, text='Colonia: ', padding=(5,5))
        self.combobox = ttk.Combobox(self.frame, width=27, state="readonly")

        self.button1 = ttk.Button(self.frame, text='Buscar', padding=(5,5), command=self.search)
        self.button2 = ttk.Button(self.frame, text='Aceptar', padding=(5,5), command=self.make_selection)

        self.label4 = ttk.Label(self.frame, text='Previsualizacion', padding=(5,5))
        
        self.textarea = Text(self.frame, height=10, width=30, padx=5, pady=5, state=DISABLED)

        self.button3 = ttk.Button(self.frame, text='Guardar', padding=(5,5), command=self.choose_dir)

        self.frame.grid(column=0, row=0)
        self.label1.grid(column=0, row=0)
        self.textbox1.grid(column=1,row=0, columnspan=3)
        self.label2.grid(column=0, row=1)
        self.textbox2.grid(column=1, row=1, columnspan=3)
        self.label3.grid(column=0, row=3)
        self.combobox.grid(column=1, row=3, columnspan=3)
        self.button1.grid(column=1,row=4)
        self.button2.grid(column=2,row=4)
        self.label4.grid(column=1, row=5)
        self.textarea.grid(column=0, row=6, columnspan=3)
        self.button3.grid(column=1, row=8)

        self.textbox1.focus_set()
        self.root.mainloop() 

    def search(self):
        if not self.check_values():
            messagebox.showerror('Error', 'Ingrese sus datos')
            return

        data = get_data(self.cp.get(), make_dict())
        self.combobox.config(postcommand=self.add_options(data))
        

    def make_selection(self):
        data = get_data(self.cp.get(), make_dict())
        
        for option in data:
            if option.get('d_asenta') == self.combobox.get():
                selection = option

        colonia = selection.get('d_asenta')
        estado = selection.get('d_estado')
        municipio = selection.get('d_mnpio')
        ciudad = selection.get('d_ciudad')

        self.textarea.configure(state=NORMAL)
        self.textarea.delete('1.0', END)
    
        if selection.get('d_ciudad') == '':
            self.textarea.configure(state=NORMAL)
            self.textarea.insert('1.0', f'Nombre: {self.name.get()}\nC.P.: {self.cp.get()}\nColonia: {colonia}\nEstado: {estado}\nMunicipio: {municipio}')
            self.textarea.configure(state=DISABLED)

            return

        self.textarea.configure(state=NORMAL)
        self.textarea.insert('1.0', f'Nombre: {self.name.get()}\nC.P.: {self.cp.get()}\nColonia: {colonia}\nEstado: {estado}\nMunicipio: {municipio}\nCiudad: {ciudad}')
        self.textarea.configure(state=DISABLED)
        
    def add_options(self, data:list):
        colonias = [data[idx].get('d_asenta') for idx in range(len(data))]
        self.combobox['values'] = colonias

    def choose_dir(self):
        if not self.check_values():
            messagebox.showerror('Error', 'Ingrese sus datos')
            return

        parent_dir = filedialog.askdirectory()
        data = self.textarea.get('1.0', END)
        
        if not check_directory(self.cp.get(), parent_dir):
            messagebox.showwarning('Atencion', f'El directorio {self.cp.get()} ya existe')
            make_file(self.name.get(), self.cp.get(), data, parent_dir)
        else:
            make_file(self.name.get(), self.cp.get(), data, parent_dir)

    def check_values(self):
        return len(self.name.get())>0 and len(self.cp.get())>0


def main():
    app = Interface()


if __name__ == '__main__':
    main()
