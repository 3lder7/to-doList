import tkinter;
import customtkinter as ctk;
from tkinter import *;
from tkinter import messagebox;

#functions
def add():
    tarefa = add_tarefa.get()
    if tarefa:
        lista_tarefas.insert(0,tarefa)
        add_tarefa.delete(0, END)
        salvarTarefas()
    else:
        messagebox.showerror("Erro!, Digite uma Tarefa")

def delet():
    selecionada = lista_tarefas.curselection()
    if selecionada:
        lista_tarefas.delete(selecionada)
        salvarTarefas()
    else:
        messagebox.showerror("Erro, Selecione uma Tarefa")

def salvarTarefas():
    with open("tarefas.txt", "w") as t:
        tarefas = lista_tarefas.get(0, END)
        for x in tarefas:
            t.write(x+"\n")
            
def carregar_tarefas():
   try:
    with open('tarefas.txt', 'r') as t:
        tarefas = t.readlines()
        for x in tarefas:
            lista_tarefas.insert(0,x.strip())
   except:
       messagebox.showinfo("APP", "Bem Vindo ao APP Tarefas")

#execução da janela:
janela = ctk.CTk()
janela.minsize(350,500)
janela.maxsize(350,500)
janela.title("APP Tarefas V1.0")
ctk.set_appearance_mode("dark")

#decoração janela
ctk.CTkLabel(janela, text='APP Tarefas', 
             text_color='green', 
             font=("Arial",30,"bold")).pack(pady=10)

#botões
bt_adicionar = ctk.CTkButton(janela, text="Adicionar Tarefa",
                             fg_color="green", text_color="white",
                             font=("Arial", 15,"bold"),
                             hover_color="darkgreen", command=add)
bt_adicionar.place(x=20, y=70)

bt_remover = ctk.CTkButton(janela, text="Remover Tarefa",
                             fg_color="red", text_color="white",
                             font=("Arial", 15,"bold"),
                             hover_color="darkred", command=delet)
bt_remover.place(x=190, y=70)

#caixa de texto
add_tarefa = ctk.CTkEntry(janela,width=300,
                          height=30,
                          placeholder_text="Digite uma nova Tarefa:")
add_tarefa.place(x=25,y=130)

#caixa de terafas adicionadas
lista_tarefas = Listbox(janela, width=27, 
                        height=13,
                        bg="#363636",
                        fg="white",
                        bd=0,
                        font=("Arial", 15))
lista_tarefas.place(x=25, y=180)

carregar_tarefas()
janela.mainloop()