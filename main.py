from controle.controlador_peca import ControladorPeca
import ttkbootstrap as ttk


def main():
    root = ttk.Window(themename="lumen")

    controller = ControladorPeca(root)
    controller.tela_menu()

    root.mainloop()


if __name__ == "__main__":
    main()

