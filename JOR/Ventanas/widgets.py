from tkinter import *


def click():
    texto = 'Hola, ' + entrada.get()
    etiqueta.configure(text=texto)


ventana = Tk()
ventana.title('Widgets básicos')
ventana.resizable(True, True)
ventana.config()
frame = Frame()
frame.pack()
frame.config(width=640, height=350)
etiqueta = Label(frame, text='Etiqueta', font=('Arial', 18))
etiqueta.grid(column=1, row=2)
entrada = Entry(frame, width=30)
entrada.grid(column=2, row=2)
boton = Button(frame, text='Pulsame', bg='red', fg='yellow', command=click)
boton.grid(column=1, row=4)
ventana.mainloop()  # Para que la ventana se mantenga en vista.
