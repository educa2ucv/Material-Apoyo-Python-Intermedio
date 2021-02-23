from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = ''

root = Tk()
root.title('Mi Editor')

def nuevo():
    global ruta
    mensaje.set('Nuevo Fichero')
    ruta = ''
    texto.delete(1.0,'end')
    root.title('Mi Editor')

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='.', 
        filetypes=(("Ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")

def guardar():
    mensaje.set('Guardar Fichero')
    if ruta != '':
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set('Fichero guardado exitosamente')
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set('Guardar Como')

    fichero = FileDialog.asksaveasfile(title='Guardar Fichero', mode='w', defaultextension='.txt')

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w')
        fichero.write(contenido)
        fichero.close()
        mensaje.set('Fichero guardado exitosamente')
    else:
        mensaje.set('Guardado cancelado')
        ruta = ''

menubar = Menu(root)
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="Nuevo", command=nuevo)
fileMenu.add_command(label="Abrir", command=abrir)
fileMenu.add_command(label="Guardar", command=guardar)
fileMenu.add_command(label="Guardar Como", command=guardar_como)
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=fileMenu, label="Archivo")

texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0,padx=6,pady=4, font=('Consolas', 12))

mensaje = StringVar()
mensaje.set('Bienvenido a Mi Editor')
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side='left')

root.config(menu=menubar)

root.mainloop()