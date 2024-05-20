import tkinter as tk
from tkinter import ttk
from limite.tela_padrao import TelaPadrao
from tkinter import messagebox

class TelaRegistrarVenda(TelaPadrao):
    def __init__(self, master, controladorVendas, controladorSistema,
                 controladorUsuario, erro=""):
        self.mensagem_erro = erro
        self.controladorVendas = controladorVendas
        super().__init__(master, controladorSistema, controladorUsuario)

    def conteudo(self):
        w = 80

        # Frame Venda
        main_frame = ttk.Frame(self,
                                width=770,
                                height=608,
                                padding=20,
                                style='light')

        main_frame.pack(fill="none",
                         expand=False,
                         pady=32)

        # Create the table frame
        table_frame = tk.Frame(main_frame)
        table_frame.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')

        # Create the table
        columns = ('ID', 'Preço', 'Desconto')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Preço', text='Preço')
        self.tree.heading('Desconto', text='Desconto')

        for i in range(10):
             self.tree.insert('', tk.END, values=(f'Item {i+1}', f'R$ {i*10:.2f}', f'R$ {i:.2f}'))

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Create the form frame
        form_frame = tk.Frame(main_frame)
        form_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        # Create ID input
        self.id_label = tk.Label(form_frame, text="ID")
        self.id_label.grid(row=0, column=0, pady=5, sticky='w')
        self.id_entry = tk.Entry(form_frame)
        self.id_entry.grid(row=0, column=1, pady=5, sticky='ew')

        # Create Discount input
        discount_label = tk.Label(form_frame, text="Desconto")
        discount_label.grid(row=1, column=0, pady=5, sticky='w')
        discount_entry = tk.Entry(form_frame)
        discount_entry.grid(row=1, column=1, pady=5, sticky='ew')

        # Add item button
        add_button = tk.Button(form_frame, text="+", command=self.add_item)
        add_button.grid(row=1, column=2, padx=5, pady=5)

        # Remove item button
        remove_button = tk.Button(form_frame, text="Remover", command=self.remove_item)
        remove_button.grid(row=2, column=0, columnspan=3, pady=5, sticky='ew')

        # Payment button
        payment_button = tk.Button(form_frame, text="Pagamento", command=self.make_payment)
        payment_button.grid(row=3, column=0, columnspan=3, pady=20, sticky='ew')

        # Create the total labels
        total_label_frame = tk.Frame(main_frame)
        total_label_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        total_label = tk.Label(total_label_frame, text="TOTAL", font=('Arial', 14, 'bold'))
        total_label.pack(side=tk.LEFT)

        total_amount_label = tk.Label(total_label_frame, text="R$ 00,00", font=('Arial', 14, 'bold'))
        total_amount_label.pack(side=tk.LEFT, padx=10)

        # Add padding to all widgets in the form frame
        for widget in form_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

        # Make the columns and rows of the main frame stretchable
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

    def tela_menu(self):
        self.controladorSistema.tela_menu()

    def add_item(self):
        id = self.id_entry.get()
        print(id)
        if id.isdigit():
            messagebox.showerror("Erro", "Adicione um código válido.")
            return
        id_int = int(id)
        print(id_int)

        peca = self.controladorVendas.pegar_peca_por_id(id_int)

        if peca is None:
            messagebox.showerror("Erro", "Nenhuma peça com esse id cadastrada.")
        else:
            print("peca encontrada")
            return

        #O sistema verifica se a peça tem status "A venda"
            #O sistema valida se há valor valor de desconto
        #O sistema verifica se peça tem status "Reserva"
            #O sistema mostra opções para o usuário com texto "Esta peça está reservada para a pessoa x, número de telefone y. Tem certeza que deseja adicionar essa peça na venda?"
        #messagebox.showerror("Erro", "Esta peça não está disponível para venda.")

    def remove_item(self):
        item_id = 2 #validate_and_get_id()
        if item_id is not None:
            # Continue with removing the item
            for item in self.tree.get_children():
                item_values = self.tree.item(item, 'values')
                if int(item_values[0]) == item_id:
                    self.tree.delete(item)
                    break
        pass  # Implement the function to remove an item

    def make_payment(self):
        total = 123
        pagamento = self.controladorVendas.realizar_pagamento(total)
        if pagamento == 1:
            messagebox.showinfo("Sucesso", "Venda registrada com sucesso.")
        else:
            messagebox.showerror("Erro", "Ocorreu um erro com o pagamento.")

