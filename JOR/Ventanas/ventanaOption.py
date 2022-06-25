from tkinter import *


def click():
    cadena = 'Has pulsado '
    if (opcion.get() == 1):
        cadena += 'Rojo '
        ventana.config(bg='red')
    elif (opcion.get() == 2):
        cadena += 'Azul '
        ventana.config(bg='blue')
    elif (opcion.get() == 3):
        cadena += 'Amarillo '
        ventana.config(bg='yellow')
    etiqueta.config(text=cadena)


ventana = Tk()
ventana.title('Option Button')
ventana.geometry('640x320')
frame = Frame()
frame.pack()
opcion = IntVar()

rdbRojo = Radiobutton(frame, text='Rojo', variable=opcion, value=1, command=click)
rdbRojo.grid(column=1, row=3)
rdbAzul = Radiobutton(frame, text='Azul', variable=opcion, value=2, command=click)
rdbAzul.grid(column=1, row=4)
rdbAmarillo = Radiobutton(frame, text='Amarillo', variable=opcion, value=3, command=click)
rdbAmarillo.grid(column=1, row=5)

etiqueta = Label(frame, text='Selecciona una opción')
etiqueta.grid(column=1, row=6)

ventana.mainloop()  # Para que la ventana se mantenga en vista.
