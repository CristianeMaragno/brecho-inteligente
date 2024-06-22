import tkinter as tk
from tkinter import ttk
from limite.tela_padrao import TelaPadrao
from tkinter import messagebox
from entidade.status_tipos.statusRestauracao import StatusRestauracao
from entidade.status_tipos.statusAVenda import StatusAVenda
from entidade.status_tipos.statusReserva import StatusReserva
from datetime import datetime, timedelta

class TelaReserva(TelaPadrao):
    def __init__(self, master, controladorReservas, controladorSistema,
                controladorUsuario, erro=""):
        self.mensagem_erro = erro
        self.controladorReservas = controladorReservas
        self.pecas = []
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
        columns = ('ID', 'Data')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Data', text='Data')

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Create the form frame
        self.form_frame = tk.Frame(main_frame)
        self.form_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        # Create ID input
        self.id_label = tk.Label(self.form_frame, text="ID")
        self.id_label.grid(row=0, column=0, pady=5, sticky='w')
        self.id_entry = tk.Entry(self.form_frame)
        self.id_entry.grid(row=0, column=1, pady=5, sticky='ew')

        # Add item button
        add_button = tk.Button(self.form_frame, text="+", command=self.adicionar_item)
        add_button.grid(row=0, column=2, padx=5, pady=5)

        # Remove item button
        remove_button = tk.Button(self.form_frame, text="Remover", command=self.remover_item)
        remove_button.grid(row=1, column=0, columnspan=3, pady=5, sticky='ew')

        # Create reservation
        reserve_button = tk.Button(self.form_frame, text="Reservar", command=self.criar_reserva)
        reserve_button.grid(row=2, column=0, columnspan=3, pady=5, sticky='ew')

        # List button
        remove_button = tk.Button(self.form_frame, text="Ver reservas", command=self.ver_reservas)
        remove_button.grid(row=3, column=0, columnspan=3, pady=5, sticky='ew')

        # Voltar Button
        self.go_back_button = tk.Button(self.form_frame, text="Voltar", command=self.controladorReservas.voltar)
        self.go_back_button.grid(row=8, columnspan=3, pady=20, sticky='ew')


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
        peca = self.controladorReservas.pegar_peca_por_id(id)

        if peca is None:
            self.mostrar_mensagem_erro("Nenhuma peça com esse id cadastrada.")
            return

        if isinstance(peca.status, StatusRestauracao):
            self.mostrar_mensagem_erro("Esta peça não está disponível para reserva.")
            return

        if isinstance(peca.status, StatusAVenda) and peca.status.vendido:
            self.mostrar_mensagem_erro("Esta peça já foi vendida.")
            return

        if isinstance(peca.status, StatusReserva):
            date_format = "%d/%m/%Y"
            data_limite = datetime.strptime(peca.status.data, date_format)
            data_atual = datetime.now()
            if data_limite > data_atual:
                nome = peca.status.nome
                telefone = peca.status.telefone
                menssagem = f"Esta peça já está reservada para a pessoa {nome}, número de telefone {telefone}."
                self.mostrar_mensagem_erro(menssagem)
                return

        item_na_lista = self.item_na_lista(peca.id)
        if item_na_lista:
            self.mostrar_mensagem_erro("Essa peça já foi adicionada na lista.")
            return

        data_semana = datetime.now() + timedelta(days=7)
        data = data_semana.strftime('%d/%m/%Y')

        self.tree.insert('', tk.END, values=(f'{peca.id}', data))

        self.pecas.append(peca)
        # Clear the input fields
        self.id_entry.delete(0, tk.END)

    def remover_item(self):
        item_id = self.pegar_item_selecionado()
        if item_id is not None:
            for item in self.tree.get_children():
                if item == item_id:
                    item_values = self.tree.item(item, 'values')
                    self.tree.delete(item)
                    break

    def criar_reserva(self):
        self.pegar_dados_cliente()

    def pegar_dados_cliente(self):
        self.data_label = tk.Label(self.form_frame, text="Preencha os dados do cliente")
        self.data_label.grid(row=4, column=0, columnspan=3, pady=20, sticky='ew')

        # Name input
        self.name_label = tk.Label(self.form_frame, text="Nome")
        self.name_label.grid(row=5, column=0, pady=5, sticky='w')
        self.name_entry = tk.Entry(self.form_frame)
        self.name_entry.grid(row=5, column=1, pady=5, sticky='ew')

        # Number input
        self.number_label = tk.Label(self.form_frame, text="Número")
        self.number_label.grid(row=6, column=0, pady=5, sticky='w')
        self.number_entry = tk.Entry(self.form_frame)
        self.number_entry.grid(row=6, column=1, pady=5, sticky='ew')

        self.confirm_button = tk.Button(self.form_frame, text="Confirmar", command=self.salvar_reserva)
        self.confirm_button.grid(row=7, column=0, columnspan=3, pady=20, sticky='ew')

    def salvar_reserva(self):
        pecas = self.pegar_pecas_selecionadas()
        nome = self.name_entry.get()
        telefone = self.number_entry.get()
        # create data of one week
        data_semana = datetime.now() + timedelta(days=7)
        data = data_semana.strftime('%d/%m/%Y')
        reserva = self.controladorReservas.realizar_reserva(nome, telefone, data, pecas)
        if reserva:
            self.mostrar_mensagem_sucesso("Reserva registrada com sucesso.")
            self.controladorReservas.voltar()
        else:
            self.mostrar_mensagem_erro("Ocorreu um erro com na reserva.")

    def pegar_pecas_selecionadas(self):
        response = []
        tabela = []
        for item in self.tree.get_children():
            tabela.append(self.tree.item(item, 'values'))

        for value in tabela:
            peca_id = value[0]

            for peca in self.pecas:
                print(peca.id)
                print(peca_id)
                print(peca.id == peca_id)
                if peca.id == peca_id:
                    dados_update = {
                        'id': peca.id,
                        'custo_aquisicao': peca.custo_aquisicao,
                        'descricao': peca.descricao,
                        'status': 'a_venda',
                        'ajustes': [],
                        'imagem': peca.imagem,
                        'titulo': peca.titulo,
                        'preco': peca.preco
                    }
                    print(peca.id)
                    response.append(dados_update)

        return response

    def ver_reservas(self):
        reservas = self.controladorReservas.pegar_reservas()
        if len(reservas) == 0:
            self.mostrar_mensagem_erro("Não há reservas.")
        else:
            # Create the popup window
            popup = tk.Toplevel()
            popup.title("Reservas")

            # Create a frame to contain the Listbox and Scrollbar
            frame = ttk.Frame(popup)
            frame.pack(fill=tk.BOTH, expand=True)

            # Create a Listbox widget
            listbox = tk.Listbox(frame)
            listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Create a Scrollbar widget and set it to the Listbox
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
            listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Add items to the Listbox
            for reserva in reservas:
                text = "Peça " + reserva["id"] + " - " + reserva["nome"] + "/" + reserva["telefone"] + " - Data limite: " + reserva["data"]
                listbox.insert(tk.END, text)

    def pegar_item_selecionado(self):
        selected_item = self.tree.selection()
        if selected_item:
            return selected_item[0]
        return '0'

    def item_na_lista(self, id):
        for item in self.tree.get_children():
            item_values = self.tree.item(item, 'values')
            if item_values[0] == id:
                return True
        return False

    def mostrar_mensagem_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem)

    def mostrar_mensagem_sucesso(self, mensagem):
        messagebox.showinfo("Sucesso", mensagem)



