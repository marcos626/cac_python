
import os
import tkinter as tk
from tkinter.filedialog import askopenfile
class my_window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Programa")
        self.window.geometry("500x200")
        button_file = tk.Button(self.window, text="Abrir archivo", command=self._open_file)
        self.text = tk.Label(self.window, text="")
        button_file.pack()
        self.text.pack()
    def mainloop(self):
        self.window.mainloop()
    def _open_file(self):
        file = askopenfile(mode ="r", filetypes =[("Programillas Python", "*.py")])
        file_name = os.path.basename(file.name)
        self.text["text"] = "Nombre del archivo: {}".format(file_name)

ventana = my_window()
ventana.mainloop()

"""
#ejemplo de 3 opciones
import tkinter as tk
class my_window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Programa")
        self.window.geometry("500x200")
        self.variable = tk.StringVar()
        radio_button1 = tk.Radiobutton(text="Opción 1", variable=self.variable, value="uno", command=self._btn)
        radio_button2 = tk.Radiobutton(text="Opción 2", variable=self.variable, value="dos", command=self._btn)
        radio_button3 = tk.Radiobutton(text="Opción 3", variable=self.variable, value="tres", command=self._btn)
        self.text = tk.Label(self.window, text="")
        radio_button1.pack()
        radio_button2.pack()
        radio_button3.pack()
        self.text.pack()
    def mainloop(self):
        self.window.mainloop()
    def _btn(self):
        self.text["text"] = "Seleccionado: {}".format(self.variable.get())

ventana = my_window()
ventana.mainloop()

---------------------------------------------
import tkinter as tk
class my_window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Programa")
        self.window.geometry("500x200")
        self.text = tk.Label(self.window, text="Dime tu nombre")
        self.name_input = tk.Entry(self.window)
        button_hola = tk.Button(self.window, text="¡Hola!", bg="green", fg="white", command=self._hello_btn)
        button_adios = tk.Button(self.window, text="¡Me voy!", bg="red", fg="white", command=self._bye_btn)
        self.text.pack()
        self.name_input.pack()
        button_hola.pack()
        button_adios.pack()
    def mainloop(self):
        self.window.mainloop()
    def _hello_btn(self):
        text = "Hola {}".format(self.name_input.get())
        self._show_text(self.text, text)
    def _bye_btn(self):
        text = "Adiós {}".format(self.name_input.get())
        self._show_text(self.text, text)
    def _show_text(self, widget_out, text):
        widget_out["text"] = text

ventana = my_window()
ventana.mainloop()

-------------------------
import tkinter as tk
class my_window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Programa")
        self.window.geometry("500x200")
        self.text = tk.Label(self.window, text="Hola")
        button_hola = tk.Button(self.window, text="¡Hola!", bg="green", fg="white", command=self._hello_btn)
        self.text.pack()
        button_hola.pack()
    def mainloop(self):
        self.window.mainloop()
    def _hello_btn(self):
        text = "Chao"
        self._show_text(self.text, text)
    def _show_text(self, widget_out, text):
        widget_out["text"] = text

ventana = my_window()
ventana.mainloop()

---------------------------
import tkinter as tk
def adios():
    text["text"] = "Adiós"

window = tk.Tk()
window.title("Programa")
window.geometry("500x200")
text = tk.Label(window, text="Hola")
text.pack()
button = tk.Button(window, text="¡Me voy!", bg="green", fg="white", command=adios)
button.pack()
window.mainloop()

------------------------
import tkinter as tk
window = tk.Tk()
window.title("Programa")
window.geometry("300x300")
frame = tk.Frame(window)
text1 = tk.Label(frame, text="uno") #dentro del frame están los textos "uno" y "dos"
text2 = tk.Label(frame, text="dos")
text3 = tk.Label(window, text="tres")
text4 = tk.Label(window, text="cuatro")
frame.pack()
text1.pack(side=tk.LEFT)
text2.pack(side=tk.RIGHT)
text3.pack(side=tk.TOP)
text4.pack(side=tk.TOP)
window.mainloop()

---------------------------------
#Utiliza el método place()
import tkinter as tk
window = tk.Tk()
window.geometry("300x300")
txt_top_left = tk.Label(window, text="Arriba a la izquierda")
txt_top_left.place(x=10, y=10)
txt_bottom_right = tk.Label(window, text="Abajo a la derecha")
txt_bottom_right.place(x=150, y=200)
window.mainloop()

-------------------------------
#utiliza una rejilla para ubicar los textos
import tkinter as tk
window = tk.Tk()
window.geometry("300x300")
for x in range(3):
    for y in range(3):
        entry = tk.Label(window, width=10, text="({}:{})".format(x, y))
        entry.grid(row = x, column = y)

window.mainloop()

-------------------------------
import tkinter as tk
window = tk.Tk()
window.title("Programa")
window.geometry("300x300")
text1 = tk.Label(window, text="uno")
text2 = tk.Label(window, text="dos")
text3 = tk.Label(window, text="tres")
text4 = tk.Label(window, text="cuatro")
text1.pack(side=tk.TOP)
text2.pack(side=tk.LEFT)
text3.pack(side=tk.RIGHT)
text4.pack(side=tk.BOTTOM)
window.mainloop()

---------------------------------------
import tkinter as tk
window = tk.Tk()
window.title("Programa")
window.geometry("500x200")
text = tk.Label(window, text="Hola mundo")
text.pack()
window.mainloop()
"""