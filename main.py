from controle.controlador_sistema import ControladorSistema
import tkinter as tk

root = tk.Tk()
root.title("Brechó inteligente")
root.geometry("600x600")

ControladorSistema(root).criar_adm_padrao()
ControladorSistema(root).tela_sistema()

root.mainloop()
