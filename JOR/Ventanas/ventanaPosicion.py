from tkinter import *

# constantes
ancho = 600
alto = 400
posx = 350
posy = 100
anchoAlto = str(ancho) + 'x' + str(alto)
posicionx = '+' + str(posx)
posiciony = '+' + str(posy)


def click():
    texto = 'Hola ' + nombre.get() + ' tienes ' + str(edad.get()) + ' años.'
    etiquetaResultado.configure(text=texto)


ventana = Tk()
ventana.title('Posicionando ventana')
ventana.resizable(True, True)
ventana.geometry(anchoAlto + posicionx + posiciony)
frame = Frame()
frame.pack()
frame.config()

nombre = StringVar()
etiquetaNombre = Label(frame, text='Nombre', font=('Arial', 12))
etiquetaNombre.grid(column=1, row=2)
entradaNombre = Entry(frame, textvariable=nombre, width=50)
entradaNombre.grid(column=2, row=2)

edad = IntVar()
etiquetaEdad = Label(frame, text='Edad', font=('Arial', 12))
etiquetaEdad.grid(column=1, row=3)
entradaEdad = Entry(frame, textvariable=edad, width=50)
entradaEdad.grid(column=2, row=3)
edad.set('21')

etiquetaResultado = Label(frame, text='Inserte su nombre y edad', font=('Arial', 12))
etiquetaResultado.grid(column=2, row=9)

boton = Button(frame, text='Pulsame', bg='red', fg='blue', command=click)
boton.grid(column=2, row=5)

ventana.mainloop()  # Para que la ventana se mantenga en vista.
