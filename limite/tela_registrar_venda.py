import tkinter as tk
from tkinter import ttk
from limite.tela_padrao import TelaPadrao
from tkinter import messagebox
from entidade.status_tipos.statusRestauracao import StatusRestauracao
from entidade.status_tipos.statusAVenda import StatusAVenda
from entidade.status_tipos.statusReserva import StatusReserva
from entidade.peca import Peca

class TelaRegistrarVenda(TelaPadrao):
    def __init__(self, master, controladorVendas, controladorSistema,
                 controladorUsuario, erro=""):
        self.mensagem_erro = erro
        self.controladorVendas = controladorVendas
        self.total = 0
        self.pecas = []

        #Para testes com reserva
        self.peca_reserva = Peca("2", "teste", StatusReserva('Cris', '99840-2895'), 45, '', '', 40)
        super().__init__(master, controladorSistema, controladorUsuario)

    def conteudo(self):
        w = 80

        # Frame Venda
        main_frame = ttk.Frame(self,
                                width=770,
                                height=608,
                                padding=20,
                                style='light')

        main_frame.grid(row=1, column=0, padx=10, pady=32)

        # Create the table frame
        table_frame = tk.Frame(main_frame)
        table_frame.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')

        # Create the table
        columns = ('ID', 'Preço', 'Desconto')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Preço', text='Preço')
        self.tree.heading('Desconto', text='Desconto')

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Create the form frame
        self.form_frame = tk.Frame(main_frame)
        self.form_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        # Create ID input
        self.id_label = tk.Label(self.form_frame, text="ID")
        self.id_label.grid(row=0, column=0, pady=5, sticky='w')
        self.id_entry = tk.Entry(self.form_frame)
        self.id_entry.grid(row=0, column=1, pady=5, sticky='ew')

        # Create Discount input
        self.discount_label = tk.Label(self.form_frame, text="Desconto")
        self.discount_label.grid(row=1, column=0, pady=5, sticky='w')
        self.discount_entry = tk.Entry(self.form_frame)
        self.discount_entry.grid(row=1, column=1, pady=5, sticky='ew')

        # Add item button
        add_button = tk.Button(self.form_frame, text="+", command=self.adicionar_item)
        add_button.grid(row=1, column=2, padx=5, pady=5)

        # Remove item button
        remove_button = tk.Button(self.form_frame, text="Remover", command=self.remover_item)
        remove_button.grid(row=2, column=0, columnspan=3, pady=5, sticky='ew')

        # Payment button
        payment_button = tk.Button(self.form_frame, text="Pagamento", command=self.realizar_pagamento)
        payment_button.grid(row=3, column=0, columnspan=3, pady=20, sticky='ew')

        # Voltar Button
        self.go_back_button = tk.Button(self.form_frame, text="Voltar", command=self.controladorVendas.voltar)
        self.go_back_button.grid(row=7, columnspan=3, pady=20, sticky='ew')

        # Create the total labels
        self.total_label_frame = tk.Frame(main_frame)
        self.total_label_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        self.total_label = tk.Label(self.total_label_frame, text="TOTAL", font=('Arial', 14, 'bold'))
        self.total_label.pack(side=tk.LEFT)

        self.total_amount_label = tk.Label(self.total_label_frame, text=f'R$ {self.total:.2f}', font=('Arial', 14, 'bold'))
        self.total_amount_label.pack(side=tk.LEFT, padx=10)

        # Add padding to all widgets in the form frame
        for widget in self.form_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

        # Make the columns and rows of the main frame stretchable
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

    def tela_menu(self):
        self.controladorSistema.tela_menu()

    def adicionar_item(self):
        id = self.id_entry.get()

        # Para testes com reserva
        if id == "2":
            peca = self.peca_reserva
        else:
            peca = self.controladorVendas.pegar_peca_por_id(id)

        if peca is None:
            self.mostrar_mensagem_erro("Nenhuma peça com esse id cadastrada.")
            return

        if isinstance(peca.status, StatusRestauracao):
            self.mostrar_mensagem_erro("Esta peça não está disponível para venda.")
            return

        if isinstance(peca.status, StatusAVenda) and peca.status.vendido:
            self.mostrar_mensagem_erro("Esta peça já foi vendida.")
            return


        if isinstance(peca.status, StatusReserva):
            nome = peca.status.nome
            telefone = peca.status.telefone
            menssagem = f"Esta peça está reservada para a pessoa {nome}, número de telefone {telefone}. Tem certeza que deseja adicionar essa peça na venda?"
            resposta = self.mostrar_mensagem_confirmar(menssagem)
            if not resposta:
                return

        desconto_valido, desconto = self.desconto_valido(peca.preco)
        if not desconto_valido:
            self.mostrar_mensagem_erro("O valor do desconto é inválido.")
            return

        item_na_lista = self.item_na_lista(peca.id)
        if item_na_lista:
            self.mostrar_mensagem_erro("Essa peça já foi adicionada na lista.")
            return

        preco = peca.preco

        self.tree.insert('', tk.END, values=(f'{peca.id}', f'{preco:.2f}', f'{desconto:.2f}'))

        self.total = self.total + (preco - desconto)
        self.update_total()

        # Para testes com reserva
        if id != "2":
            self.pecas.append(peca)
        # Clear the input fields
        self.id_entry.delete(0, tk.END)
        self.discount_entry.delete(0, tk.END)

    def remover_item(self):
        item_id = self.pegar_item_selecionado()
        if item_id is not None:
            for item in self.tree.get_children():
                if item == item_id:
                    item_values = self.tree.item(item, 'values')
                    self.tree.delete(item)
                    self.total = self.total - (float(item_values[1]) - float(item_values[2]))
                    self.update_total()
                    break

    def realizar_pagamento(self):
        self.selecionar_forma_de_pagamento()

    def selecionar_forma_de_pagamento(self):
        self.payment_label = tk.Label(self.form_frame, text="Selecione forma de pagamento")
        self.payment_label.grid(row=4, column=0, columnspan=3, pady=20, sticky='ew')

        formas_pagamento = ["Cartão de crédito", "Cartão de débito", "Pix", "Dinheiro"]
        self.payment_combobox = ttk.Combobox(self.form_frame, values=formas_pagamento, state="readonly")
        self.payment_combobox.grid(row=5, column=0, columnspan=3, pady=20, sticky='ew')

        self.confirm_button = tk.Button(self.form_frame, text="Confirmar", command=self.realizar_pagamento_update)
        self.confirm_button.grid(row=6, column=0, columnspan=3, pady=20, sticky='ew')

    def realizar_pagamento_update(self):
        forma_pagamento = self.payment_combobox.get()
        pecas = self.pegar_pecas_selecionadas()
        pagamento = self.controladorVendas.realizar_pagamento(self.total, forma_pagamento, pecas)
        if pagamento:
            self.mostrar_mensagem_sucesso("Venda registrada com sucesso.")
            self.controladorVendas.voltar()
        else:
            self.mostrar_mensagem_erro("Ocorreu um erro com o pagamento.")

    def pegar_pecas_selecionadas(self):
        pecas_descontos = []
        descontos = []
        for item in self.tree.get_children():
            descontos.append(self.tree.item(item, 'values'))

        for item in descontos:
            peca_id = item[0]
            desconto = item[2]

            for peca in self.pecas:
                if peca.id == peca_id:
                    dados_update = {
                        'id': peca.id,
                        'custo_aquisicao': peca.custo_aquisicao,
                        'descricao': peca.descricao,
                        'status': 'a_venda',
                        'ajustes': [],
                        'imagem': peca.imagem,
                        'titulo': peca.titulo,
                        'preco': peca.preco,
                        'desconto': desconto
                    }
                    pecas_descontos.append(dados_update)

        return pecas_descontos

    def pegar_item_selecionado(self):
        selected_item = self.tree.selection()
        if selected_item:
            return selected_item[0]
        return '0'

    def mostrar_mensagem_confirmar(self, message):
        response = messagebox.askyesno("Confirmação", message)
        return response

    def desconto_valido(self, preco):
        desconto = self.discount_entry.get()
        if not desconto.isdigit():
            return False, 0

        desconto_float = float(desconto)
        if desconto_float >= preco:
            return False, 0

        return True, desconto_float

    def item_na_lista(self, id):
        for item in self.tree.get_children():
            item_values = self.tree.item(item, 'values')
            if item_values[0] == id:
                return True
        return False

    def update_total(self):
        self.total_amount_label.config(text=f"R$ {self.total:.2f}")

    def mostrar_mensagem_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem)

    def mostrar_mensagem_sucesso(self, mensagem):
        messagebox.showinfo("Sucesso", mensagem)



