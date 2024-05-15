from limite.tela_padrao import TelaPadrao
import ttkbootstrap as ttk

class TelaEditCalculadora(TelaPadrao):
    def __init__(self, master, controlador, controladorCalculadora, controladorUsuario):
        self.__controlador_calculadora = controladorCalculadora
        super().__init__(master, controlador, controladorUsuario)

    def conteudo(self):
        bigframe = ttk.Frame(self)
        bigframe.pack(fill='both')
        scroll = ttk.Scrollbar(bigframe,
                               orient='vertical')
        scroll.pack(side='right', fill='y')

        frame = ttk.Frame(bigframe,
                                width=770,
                                height=608,
                                padding=20,
                                style='light')
        frame.pack(fill="none",
                         expand=False,
                         pady=32)
        
        self.label = ttk.Label(frame,
                                 text="EDITAR CALCULADORA",
                                 style="inverse-light",
                                 font=("Helvetica", 12, "bold"))
        self.label.pack(pady=32)

        # Obter todas as categorias do DAO
        categorias = self.__controlador_calculadora.obter_todas_categorias()

        # Criar campos de entrada para cada categoria
        self.campos_custo = {}
        for categoria in categorias:
            # Frame para conter a label e o campo de entrada
            frame_categoria = ttk.Frame(frame,
                                        style="light",
                                        borderwidth=1,
                                        relief="solid")
            frame_categoria.pack(fill="x", padx=10, pady=5)

            # Label da categoria
            label_categoria = ttk.Label(frame_categoria, text=categoria, style="inverse-light")
            label_categoria.pack(side="left", padx=10, pady=5)

            # Campo de entrada para o custo
            campo_custo = ttk.Entry(frame_categoria, width=10)
            campo_custo.pack(side="right")
            self.campos_custo[categoria] = campo_custo

        # Botão de salvar
        botao_salvar = ttk.Button(frame, text="Salvar", command=self.salvar_custos)
        botao_salvar.pack(pady=10)

    def salvar_custos(self):
        # Coletar os valores inseridos nos campos de custo e salvá-los
        for categoria, campo_custo in self.campos_custo.items():
            valor = campo_custo.get()
            # Se o valor estiver vazio ou não for um número, continue para a próxima categoria
            if not valor or not valor.isdigit():
                continue
            # Salvar o custo apenas se o valor for um número válido
            self.__controlador_calculadora.atualizar_custo(categoria, float(valor))