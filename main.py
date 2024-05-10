from controle.controlador_sistema import ControladorSistema
import tkinter as tk

root = tk.Tk()
root.title("Brechó inteligente")

ControladorSistema(root).criar_adm_padrao()
ControladorSistema(root).tela_catalogo()

root.mainloop()
