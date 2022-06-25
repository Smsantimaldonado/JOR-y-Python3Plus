from tkinter import *

ventana = Tk()
ventana.title('Mi primera ventana')
ventana.resizable(True, True)  # indicar si se puede cambiar el tamaño en alto y ancho
ventana.iconbitmap('JOR\icono.ico')  # QUITAR el ícono de la ventana (al lado del titulo) iconfinder.com
ventana.geometry('640x360')  # designar tamaño de la ventana. va entre comillas como un str. ANCHOxALTO
ventana.config(bg='red')  # bg = background. explorar las otras posibilidades para personalizar
frame = Frame()  # establecer el lienzo donde dibujaremos
frame.pack(
    side='left')  # empaquetarlo dentro de la ventana. side -> le marco la unicacin dentro de la ventana. anchor -> n por norte, para que quede establecido en la parte de arrina.
frame.config(bg='yellow', width=640,
             height=350)  # personalizacion igual que con la ventana con diferentes colores y tamaño para ver la diferencia
# el tamaño de la ventana podemos modificarlo con el mousse pero el del frame no ya que está 'adentro' de la ventana
ventana.mainloop()  # Para que la ventana se mantenga en vista.
