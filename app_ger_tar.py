import customtkinter as ctk
from tkinter import ttk


class ger_tar_app():

    def __init__(self, root):

        self.root = root
        self.root.title("App")
        self.root.geometry("800x580")
        self.root.resizable(False, False)  

        ctk.set_appearance_mode("light")

        # -------------------------------------------------------------
        # TÍTULO DA TAREFA
        # -------------------------------------------------------------

        ctk.CTkLabel(root, text="Título da Tarefa: ", font=("Arial bold", 15)).grid(row=0, column=0, columnspan=1, sticky="e",pady=15, padx=20)
        
        tit_tar = ctk.CTkEntry(root, width=445, border_width=1, border_color="#5e5e5e").grid(row=0, column=1, columnspan=1, pady=10)

        # -------------------------------------------------------------
        # DESCRIÇÃO DA TAREFA
        # -------------------------------------------------------------

        ctk.CTkLabel(root, text="Descrição da Tarefa: ", font=("Arial bold", 15)).grid(row=1, column=0, pady=10, sticky="n", columnspan=1, padx=20)

        desc_tar = ctk.CTkTextbox(root, width=445, height=100, border_width=1, border_color="#5e5e5e").grid(row=1, column=1, columnspan=1, pady=10)

        # -------------------------------------------------------------
        # FUNÇÕES dos botões
        # -------------------------------------------------------------

        def add_tar():
            print("adicionar funcionou")
            


        def up_tar():
            print("atualizar funcionou")
            


        def del_tar():
            print("excluir funcionou")
            

        # -------------------------------------------------------------
        # BOTÕES: Adicionar / Editar / Excluir
        # -------------------------------------------------------------

        btn = ctk.CTkFrame(root)
        btn.grid(row=2, column=1, pady=15, sticky="w", columnspan=2)

       
        btn_add = ctk.CTkButton(btn, text="Adicionar", hover_color="#51e95c", text_color="#000000", command=add_tar)
        btn_add.grid(row=2, column=0, padx=5)

        btn_up = ctk.CTkButton(btn, text="Atualizar", hover_color="#e3f065", text_color="#000000", command=up_tar)
        btn_up.grid(row=2, column=1, padx=5)

        btn_del = ctk.CTkButton(btn, text="Excluir", hover_color="#f52929", text_color="#000000", command=del_tar)
        btn_del.grid(row=2, column=2, padx=5)

        
        # -------------------------------------------------------------
        # STATUS + FILTRO
        # -------------------------------------------------------------

        ctk.CTkLabel(root, text="Status: ", font=("Arial bold", 15)).grid(row=3, column=0, pady=15, sticky="e",padx=20)


        status_var = ctk.StringVar(value="")

        status_var = ctk.CTkOptionMenu(root, values=["Pendente", "Concluída"], width=150, text_color="#000000", dropdown_hover_color="#0870b1").grid(row=3, column=1, sticky="w")

        btn_flt = ctk.CTkButton(root, text="Aplicar Filtro", text_color="#000000", width=230)
        btn_flt.grid(row=3, column=1, padx=30, sticky="e")
        
        # -------------------------------------------------------------
        # TABELA DE EXIBIÇÃO
        # -------------------------------------------------------------

        tarefas = []
        
        tabela = ttk.Treeview(root, columns=("Tìtulo", "Descrição", "Status"), show="headings")

        tabela.column("Tìtulo", minwidth=1, width=150)
        tabela.column("Descrição", minwidth=0, width=350)
        tabela.column("Status", minwidth=0, width=100)

        tabela.heading("Tìtulo", text="Tarefa")
        tabela.heading("Descrição", text="Descrição")
        tabela.heading("Status", text="Status")

        tabela.grid(row=4, column=1, columnspan=4)


        for (t, d, s) in tarefas:
            tarefas.insert("", "end", values=(t, d, s))



# -------------------------------------------------------------
# INICIALIZAÇÃO DA JANELA
# -------------------------------------------------------------

root = ctk.CTk()

app = ger_tar_app (root)
root.mainloop()    


# "#5e5e5e"