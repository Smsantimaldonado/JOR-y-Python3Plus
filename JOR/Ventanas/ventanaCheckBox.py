from tkinter import *


def click():
    cadena = 'Has pulsado el '
    if (color01.get()):
        cadena += 'Rojo '
        ventana.config(bg='red')
    if (color02.get()):
        cadena += 'Azul '
        ventana.config(bg='blue')
    if (color03.get()):
        cadena += 'Amarillo '
        ventana.config(bg='yellow')
    if (not color01.get() and not color02.get() and not color03.get()):
        ventana.config(bg='lightgreen')
    etiqueta.config(text=cadena)


ventana = Tk()
ventana.title('Option Button')
ventana.geometry('640x320')
frame = Frame()
frame.pack()
color01 = IntVar()  # Tomarán valores 1 o 0
color02 = IntVar()
color03 = IntVar()

cbRojo = Checkbutton(frame, text='Rojo', variable=color01, onvalue=1, offvalue=0, command=click)
cbRojo.grid(column=1, row=2)
cbAzul = Checkbutton(frame, text='Azul', variable=color02, onvalue=1, offvalue=0, command=click)
cbAzul.grid(column=1, row=3)
cbAmarillo = Checkbutton(frame, text='Amarillo', variable=color03, onvalue=1, offvalue=0, command=click)
cbAmarillo.grid(column=1, row=4)

etiqueta = Label(frame, text='Selecciona una opción')
etiqueta.grid(column=1, row=6)

ventana.mainloop()  # Para que la ventana se mantenga en vista.
