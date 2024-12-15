# importando dependencias do Tkinter
import locale
import subprocess
import pandas as pd
from docx import Document
import babel.numbers
from IPython.core.display_functions import display
from tkcalendar import *
from datetime import *
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import shutil
from openpyxl.workbook import Workbook
from IPython.display import clear_output

# importando pillow
from PIL import ImageTk, Image

from viewSYSTEM import *

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co2 = "#e5e5e5"  # grey
co3 = "#248eff"  # Verde
co4 = "#403d3d"  # letra
co5 = "#3152b7"  # azul
co7 = "#d42e2b"  # vermelha
co6 = "#378258"  # Verde novo
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + verde
c10 = "#031904"  # Verde escuro
c11 = "#5D6A5E"  # verde claro
# Criando janela
root = Tk()
root.title("HIGHER")
root.iconbitmap('icone/sistema.ico')
root.geometry('600x400')
root.configure(background=c10)
style = Style(root)
style.theme_use("clam")
root.resizable(width=FALSE, height=FALSE)

#Corrigindo importação de Imagens****************************************************************************************


# Criando Imagens********************************************************************************************************
img_logo = Image.open("icone/mostrar96.png")
img_logo = img_logo.resize((60, 60))
img_logo = ImageTk.PhotoImage(img_logo)

img_user = Image.open("icone/Clientes2.png")
img_user = img_user.resize((28, 28))
img_user = ImageTk.PhotoImage(img_user)

img_senha = Image.open("icone/Aluguel.png")
img_senha = img_senha.resize((28, 28))
img_senha = ImageTk.PhotoImage(img_senha)

# Criando Frames********************************************************************************************************
frame_lateral = Frame(root, width=200, height=600, bg=c10)
frame_lateral.grid(row=0, column=0, pady=0, padx=0, sticky=EW)

separador = Frame(root, width=3, height=600, bg=c10)
separador.grid(row=0, column=1, pady=0, padx=0, sticky=EW)

l_linha = Label(separador, relief=GROOVE, text='|', width=5, height=170, anchor=NW, font=('Ivy 1'), bg=co0,
                    fg=co0)
l_linha.place(x=0, y=25)

frame_detalhes = Frame(root, width=400, height=600, bg=c10)
frame_detalhes.grid(row=0, column=2, pady=0, padx=10, sticky=EW)


#Criando as funções necessárias******************************************************************************************
def reset_login():
    root.destroy()
def criar_password():
    global e_pergunta
    def update():
        nome = e_usuario.get()
        chave = e_pergunta.get()
        senha = e_senha.get()
        if nome == "":
            messagebox.showerror('Erro', 'Favor informar um usuário!')
            return
        elif senha == "":
            messagebox.showerror('Erro', 'Favor informar uma senha!')
            return
        elif chave == "":
            messagebox.showerror('Erro', 'Digite uma resposta!')
            return

        # Conectando ao banco de dados
        conn = sqlite3.connect('bdsystem.db')
        cursor = conn.cursor()

        # Realizando a busca
        consulta = "SELECT * FROM password WHERE nome = ?"
        # cursor.execute(consulta)
        cursor.execute(consulta, (nome,))

        # Recuperando os resultados
        resultados = cursor.fetchall()

        # Fechando a conexão com o banco de dados
        conn.close()
        # Verificando se os valores estão dentro do solicitado
        for resultado in resultados:
            if nome in resultado[1]:
                messagebox.showwarning('Erro', 'Nome de usuário já existe, digite outro nome!')
                return
        lista = [nome, senha, chave]
        # Inserindo os dados
        criar_senha(lista)
    c_check.configure(text="Qual a sua cor favorita?")
    c_checkbox.destroy()
    l_esqueci.destroy()

    e_pergunta = Entry(frame_detalhes, width=23, background='darkblue', borderwidth=2, font=('Ivy 18'), bg=c11,
                       fg=co1)
    e_pergunta.place(x=24, y=260)

    botao_reset = Button(frame_detalhes, command=reset_login, anchor=CENTER, height=1,
                         text='Login'.upper(), width=10,
                         overrelief=RIDGE,
                         font=('Ivy 14 bold'), bg=co1, fg=co0)
    botao_reset.place(x=204, y=310)

    botao_salvar = Button(frame_detalhes, command=update, anchor=CENTER, height=1,
                          text='Salvar'.upper(), width=10,
                          overrelief=RIDGE,
                          font=('Ivy 14 bold'), bg=co1, fg=co0)
    botao_salvar.place(x=24, y=310)

def editar_senha():
    try:
        nome = e_usuario.get()
        senha = e_senha.get()
        chave = "teste"


        # limpando os campos de entrada
        e_usuario.delete(0, END)
        e_senha.delete(0, END)
        chave = "teste"

        # Conectando ao banco de dados
        conn = sqlite3.connect('bdsystem.db')
        cursor = conn.cursor()

        # Realizando a busca
        consulta = "SELECT * FROM password WHERE nome = ?"
        cursor.execute(consulta, (nome,))

        # Recuperando os resultados
        resultados = cursor.fetchall()

        # Fechando a conexão com o banco de dados
        conn.close()

        lista = [nome, senha, chave]

        # Verificando caso algum campo esteja vazio ou não
        for i in lista:
            if i == "":
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        # Verificando se os valores estão dentro do solicitado
        for i in lista:
            if nome == "" or senha == "":
                messagebox.showerror('Erro', 'Preencha os campos obrigatórios')
                return
            for resultado in resultados:
                if nome in resultado:
                    messagebox.showerror('Erro', 'Registro já existente')
                    return
        # Atualizando os dados no banco de dados
        atualizar_senha(lista)

        # Mostrando a mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')


    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos itens da tabela')

def excluir_usuario():
    try:
        nome = e_usuario.get()
        messagebox.askokcancel('Atenção!', 'Quer realmente apagar este usuário?')
        # Conectando ao banco de dados
        conn = sqlite3.connect('bdsystem.db')
        cursor = conn.cursor()

        # Realizando a busca
        consulta = "SELECT * FROM password WHERE nome = ?"
        cursor.execute(consulta, (nome,))

        # Recuperando os resultados
        resultados = cursor.fetchall()

        # Fechando a conexão com o banco de dados
        conn.close()
        deletar_senha([resultados[0][0]])
        if resultados == []:
            messagebox.showerror('Erro', 'Usuário não encontrado!')
        else:
            messagebox.showinfo('Sucesso', 'Registro apagado com sucesso!')

    except IndexError:
        messagebox.showerror('Erro', 'Usuário não encontrado!')

#Função para recuperar senha perdida************************************************************************************
def recuperar_senha():
    global e_pergunta, botao_recuperar
    nome = e_usuario.get()
    chave = e_pergunta.get()
    senha = e_senha.get()

    if nome == "":
        messagebox.showerror('Erro', 'Favor informar um usuário!')
        return
    elif chave == "":
        messagebox.showerror('Erro', 'Digite uma resposta!')
        return
    # Conectando ao banco de dados
    conn = sqlite3.connect('bdsystem.db')
    cursor = conn.cursor()

    # Realizando a busca
    consulta = "SELECT * FROM password WHERE nome = ?"
    #cursor.execute(consulta)
    cursor.execute(consulta, (nome,))

    # Recuperando os resultados
    resultados = cursor.fetchall()

    # Fechando a conexão com o banco de dados
    conn.close()

    # Verificando se os valores estão dentro do solicitado
    for resultado in resultados:
        if chave == resultado[3]:
            e_senha.delete(0, END)
            e_senha.insert(0, resultado[2])
            botao_recuperar.destroy()
            c_check.configure(text= "")
            e_pergunta.destroy()
        else:
            messagebox.showwarning('Erro', 'Resposta incorreta!')
    if resultados == []:
        messagebox.showwarning('Erro', 'Resposta incorreta!')

def limpar_senha():
    nome = ""
    senha = ""
    lista = [nome, senha, 1]
    atualizar_lembrar(lista)


#Função para logar no sistema com usuário e senha corretos**************************************************************
def autenticar():
    nome = e_usuario.get()
    senha = e_senha.get()

    # Conectando ao banco de dados
    conn = sqlite3.connect('bdsystem.db')
    cursor = conn.cursor()

    # Realizando a busca
    consulta = "SELECT * FROM password WHERE nome = ? AND senha = ?"
    cursor.execute(consulta, (nome,senha,))

    # Recuperando os resultados
    resultados = cursor.fetchall()

    # Fechando a conexão com o banco de dados
    conn.close()

    lista = [nome, senha]

    # Verificando se os valores estão dentro do solicitado
    for i in lista:
        if nome == "" or senha == "":
            messagebox.showerror('Erro', 'Favor informar um usuário e senha!')
            return
    for resultado in resultados:
        if lista[0] == resultado[1] and lista[1] == resultado[2]:
            messagebox.showinfo('Sucesso', f'Seja bem Vindo {nome}!')
            l_cadastro = Label(frame_detalhes, text="Cadastrar um novo usuário:", height=1, anchor=NW,
                               font=('Ivy 8'),
                               bg=c10,
                               fg=co1)
            l_cadastro.place(x=94, y=360)
            l_cadastro.bind("<Button-1>", lambda event: criar_password())
            botao_acesso = Button(frame_detalhes, command="", anchor=CENTER, height=1,
                                  text='Sistema'.upper(), width=10,
                                  overrelief=RIDGE,
                                  font=('Ivy 14 bold'), bg=co1, fg=co0)
            botao_acesso.place(x=24, y=310)


    if resultados == []:
        messagebox.showwarning('Erro', 'Usuário ou senha incorretos!')

#Função para sair da tela de senhas*************************************************************************************
def funcao_sair():
    excluir_usuario()
    #root.destroy()

#Função para iniciar processo de recuperação de senha*******************************************************************
def recuperar():
    global e_pergunta, botao_recuperar

    c_check.configure(text= "Qual a sua cor favorita?")
    c_checkbox.destroy()
    l_esqueci.destroy()
    e_pergunta = Entry(frame_detalhes, width=23, background='darkblue', borderwidth=2, font=('Ivy 18'), bg=c11, fg=co1)
    e_pergunta.place(x=24, y=260)

    botao_recuperar = Button(frame_detalhes, command=recuperar_senha, anchor=CENTER, height=1,
                             text='Recuperar'.upper(), width=10,
                             overrelief=RIDGE,
                             font=('Ivy 14 bold'), bg=co1, fg=co0)
    botao_recuperar.place(x=24, y=310)

    botao_reset = Button(frame_detalhes, command=reset_login, anchor=CENTER, height=1,
                         text='Login'.upper(), width=10,
                         overrelief=RIDGE,
                         font=('Ivy 14 bold'), bg=co1, fg=co0)
    botao_reset.place(x=204, y=310)

def setar_lembrar():
    nome = e_usuario.get()
    senha = e_senha.get()
    lista = [nome, senha, 1]
    print(lista)
    atualizar_lembrar(lista)

def alternar_funcao():
    if check_box == 1:
        setar_lembrar()
    else:
        limpar_senha()

#Componentes do Programa*************************************************************************************************
check_box = IntVar()
l_logo = Label(frame_lateral, image=img_logo, bg=c10)
l_logo.place(x=68, y=110)
l_logo = Label(frame_lateral,text="SISTEMA DE CONTROLE \n HIGHER \n @Copyright | 2023\nJac Development", bg=c10, fg=co1)
l_logo.place(x=34, y=180)

l_topo = Label(frame_detalhes, text="Olá, seja bem-vindo!", height=1, anchor=NW,
                   font=('Arial 26'),
                   bg=c10,
                   fg=co1)
l_topo.place(x=24, y=40)
l_identidade = Label(frame_detalhes, text="Identifique-se para entrar:", height=1, anchor=NW,
                   font=('Ivy 12'),
                   bg=c10,
                   fg=co1)
l_identidade.place(x=84, y=90)


# Conectando ao banco de dados
conn = sqlite3.connect('bdsystem.db')
cursor = conn.cursor()
# Realizando a busca
query = "SELECT * FROM lembrar"
cursor.execute(query)
linha = cursor.fetchall()
# Fechando a conexão com o banco de dados
conn.close()
nome = linha[0][1]
senha = linha[0][2]

e_usuario = Entry(frame_detalhes, width=20, background='darkblue', borderwidth=2, font=('Ivy 18'),bg=c11, fg=co1)
e_usuario.place(x=24, y=140)
l_user = Label(frame_detalhes, image=img_user)
l_user.place(x=290, y=141)


e_senha = Entry(frame_detalhes, width=20, background='darkblue', show='*', borderwidth=2,font=('Ivy 18'),bg=c11, fg=co1)
e_senha.place(x=24, y=200)
l_password = Label(frame_detalhes, image=img_senha)
l_password.place(x=290, y=201)

e_usuario.delete(0, END)
e_senha.delete(0, END)
e_usuario.insert(0, nome)
e_senha.insert(0, senha)

c_check = Label(frame_detalhes, text="Lembrar senha", height=1, anchor=NW,
                   font=('Ivy 10'),
                   bg=c10,
                   fg=co1)
c_check.place(x=50, y=240)

c_checkbox = Checkbutton (frame_detalhes,variable=check_box, command=alternar_funcao,text="", onvalue=1, offvalue=0, bg=c10)
c_checkbox.place(x=24, y=240)

l_esqueci = Label(frame_detalhes, text="Esqueci minha senha!", height=1, anchor=NW,
                   font=('Ivy 10'),
                   bg=c10,
                   fg=co1)
l_esqueci.place(x=190, y=240)
l_esqueci.bind("<Button-1>", lambda event:recuperar())

botao_entrar = Button(frame_detalhes, command=autenticar, anchor=CENTER, height=1,
                             text='Entrar'.upper(), width=10,
                             overrelief=RIDGE,
                             font=('Ivy 14 bold'), bg=co1, fg=co0)
botao_entrar.place(x=24, y=310)


botao_sair = Button(frame_detalhes, command=funcao_sair, anchor=CENTER, height=1,
                             text='Sair'.upper(), width=10,
                             overrelief=RIDGE,
                             font=('Ivy 14 bold'), bg=co1, fg=co0)
botao_sair.place(x=204, y=310)



# Executando a janela-----------------------------------------------------
root.mainloop()
