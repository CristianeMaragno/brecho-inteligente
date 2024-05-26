import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime, timedelta
import tkcalendar
from limite.tela_padrao import TelaPadrao


class TelaCriarUsuario(TelaPadrao):
    def __init__(self, master, controladorLocal, controladorSistema, usuario):
        self.editar = False if usuario is None else True
        self.controladorLocal = controladorLocal
        self.usuario = usuario
        super().__init__(master, controladorSistema, controladorLocal)

    def conteudo(self):

        # Frame
        main_frame = ttk.Frame(self,
                               width=770,
                               height=608,
                               padding=20,
                               style='light')

        main_frame.grid(row=1, column=0, padx=10, pady=32)


        # Nome
        self.name_label = tk.Label(main_frame, text="Nome:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry = tk.Entry(main_frame)
        if (self.editar):
            self.name_entry.insert(0, self.usuario.nome)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Email
        self.email_label = tk.Label(main_frame, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry = tk.Entry(main_frame)
        if (self.editar):
            self.email_entry.insert(0, self.usuario.email)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        # Senha
        self.password_label = tk.Label(main_frame, text="Senha:")
        self.password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.password_entry = tk.Entry(main_frame, show="*")
        if (self.editar):
            self.password_entry.insert(0, self.usuario.senha)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        self.repeat_password_label = tk.Label(main_frame, text="Repetir senha:")
        self.repeat_password_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.repeat_password_entry = tk.Entry(main_frame, show="*")
        if (self.editar):
            self.repeat_password_entry.insert(0, self.usuario.senha)
        self.repeat_password_entry.grid(row=3, column=1, padx=10, pady=5)

        # Data de nascimento
        '''
        self.dob_label = tk.Label(main_frame, text="Data de nascimento:")
        self.dob_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.dob_calendar = Calendar(main_frame, selectmode="day", year=2000, month=1, day=1)
        self.dob_calendra.pack(pady=20)
        self.dob_calendra.grid(row=4, column=1, padx=5, pady=5)
        '''

        # Papel
        self.role_label = tk.Label(main_frame, text="Papel:")
        self.role_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.role_var = tk.StringVar()
        self.role_combobox = ttk.Combobox(main_frame,
                                          textvariable="Selecione o papel",
                                          state="readonly")
        self.role_combobox['values'] = ("Administrador", "Funcionário")
        self.role_combobox.current(0)
        if (self.editar):
            papel = 'Administrador' if self.usuario.papel == 1 \
                else 'Funcionário'
            self.role_combobox.set(papel)
        self.role_combobox.grid(row=5, column=1, padx=10, pady=5)

        # Criar ou editar Button
        texto = "Editar" if self.editar else "Criar"
        self.create_button = tk.Button(main_frame, text=texto, command=self.create_edit_user)
        self.create_button.grid(row=6, columnspan=2, padx=10, pady=10)

        # Voltar Button
        self.go_back_button = tk.Button(main_frame, text="Voltar", command=self.controladorLocal.voltar)
        self.go_back_button.grid(row=7, columnspan=2, padx=10, pady=10)

    def create_edit_user(self):
        id = self.usuario.identificador if self.editar else 0
        nome = self.name_entry.get()
        email = self.email_entry.get()
        senha = self.password_entry.get()
        senha_repetida = self.repeat_password_entry.get()
        #nascimento = self.dob_calendar.get_date()
        nascimento = '12/01/2000'
        papel = self.role_combobox.get()
        papel_int = 0

        #correct bug of loading role
        #correct bug of loading date

        if not nome or not email or not senha or not senha_repetida or not nascimento:
            messagebox.showerror("Campos inválidos", "Todos os campos devem ser preechidos. Tente de novo.")
            return

        if senha != senha_repetida:
            messagebox.showerror("Senhas diferentes", "Senhas não são iguais. Tente de novo.")
            return

        # Validate age (older than 18)
        '''
        nascimento_data = datetime.strptime(nascimento, "%m/%d/%y")
        eighteen_years_ago = datetime.now() - timedelta(days=365 * 18)
        if nascimento_data > eighteen_years_ago:
            messagebox.showerror("Obrigação de idade", "Os usuários devem ser maiores de idade.")
            return
        '''

        if(papel == 'Administrador'):
            papel_int = 1
        else:
            papel_int = 2

        self.controladorLocal.criar_usuario(id, nome, email, senha, nascimento, papel_int, self.editar)
        self.controladorLocal.voltar()
