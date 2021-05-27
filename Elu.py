from tkinter import Entry, Button, Tk, PhotoImage, StringVar, Frame, Label

# from tkinter import messagebox, Scrollbar, Spinbox, LabelFrame
import time
import sys
import os


sistema = sys.platform
ruta1 = os.path.abspath(__file__)
ruta2 = os.path.split(ruta1)
user = "user"
passwd = "1234"


class Himitsu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.saliendo)
        self.vista()

    def vista(self):
        usuario = StringVar()
        contras = StringVar()
        self.parent.title("Elu")
        self.parent.geometry("300x500")  # Ancho y largo
        self.parent.resizable(False, False)
        self.parent.config(background="blue")
        if sistema == "linux":
            logo = PhotoImage(file=ruta2[0] + "/imagenes/icono.gif")
            self.parent.call("wm", "iconphoto", self.parent._w, logo)
        else:
            self.parent.iconbitmap(ruta2[0] + "\\imagenes\\icono.ico")

        label1 = Label(self.parent, text="Usuario", bg="blue", fg="white")
        label1.place(x=125, y=115)

        self.entri1 = Entry(self.parent, textvariable=usuario)
        self.entri1.place(x=70, y=140)

        label2 = Label(self.parent, text="contraseña", bg="blue", fg="white")
        label2.place(x=115, y=175)

        self.entri2 = Entry(self.parent, show="*", textvariable=contras)
        self.entri2.place(x=70, y=200)

        self.boton1 = Button(self.parent, text="Ingresar", command=lambda: entrada())
        self.boton1.bind("<Return>", lambda x=None: entrada())
        self.boton1.place(x=110, y=240)

        def entrada(*args):
            if usuario.get() == user and contras.get() == passwd:
                self.vivista()

    def vivista(self):
        frame1 = Frame(self.parent, height=500, width=300)

        label3 = Label(frame1, text="Ingresando.... ")
        label3.place(x=150, y=220)

        for i in range(-300, 1):
            frame1.place(x=i, y=0)
            frame1.update()
            time.sleep(0.005)

        label3.destroy()

        label4 = Label(frame1, text="Ingresado xD")
        label4.place(x=70, y=100)

    def saliendo(self):
        self.parent.quit()
        self.parent.destroy()
        print("Saliendo del programa")


if __name__ == "__main__":
    root = Tk()
    Himitsu(root)
    root.mainloop()
