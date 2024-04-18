from controle.controlador_sistema import ControladorSistema
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

ControladorSistema(root).tela_sistema()

root.mainloop()