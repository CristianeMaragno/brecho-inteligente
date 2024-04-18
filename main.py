from controle.controlador_peca import ControladorPeca
import tkinter as tk


def main():
    root = tk.Tk()
    root.geometry("500x500")

    controller = ControladorPeca(root)
    controller.tela_menu()

    root.mainloop()


if __name__ == "__main__":
    main()

