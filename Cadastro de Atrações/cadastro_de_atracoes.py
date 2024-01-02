import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage
from PIL import Image, ImageTk
import sqlite3

class App:
    def __init__(self, root):
        #Aqui é o nome q fica no tkinter
        root.title("Cadastro de atrações da festa de Santana")
        #Aqui é a configuração de tamanho da tela
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.imagem = PhotoImage(file="logo_ifrn.png").subsample(16)

        self.logo_ifrn = tk.Label(root)
        self.logo_ifrn['image'] = self.imagem
        self.logo_ifrn.place(x=5, y=10) #logo ifrn
        
        #Aqui é o nome do trabalho
        self.nome_do_trabalho=tk.Label(root)
        ft = tkFont.Font(family='Times',size=15)
        self.nome_do_trabalho["font"] = ft
        self.nome_do_trabalho["fg"] = "#333333"
        self.nome_do_trabalho["justify"] = "left"
        self.nome_do_trabalho["text"] = "Cadastro de atrações da festa de Santana"
        self.nome_do_trabalho.place(x=100,y=50,width=400,height=30)

        #Aqui fica o nome da obra
        self.label_nome_atracao=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.label_nome_atracao["font"] = ft
        self.label_nome_atracao["fg"] = "#333333"
        self.label_nome_atracao["justify"] = "center"
        self.label_nome_atracao["text"] = "Nome da atração:"
        self.label_nome_atracao.place(x=50,y=110,width=90,height=30)

        self.caixa_nome_atracao=tk.Entry(root)
        self.caixa_nome_atracao["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.caixa_nome_atracao["font"] = ft
        self.caixa_nome_atracao["fg"] = "#333333"
        self.caixa_nome_atracao["justify"] = "center"
        self.caixa_nome_atracao["text"] = "Nome da atração"
        self.caixa_nome_atracao.place(x=70,y=140,width=276,height=25)

        #Aqui fica a descrição da obra
        self.label_descricao_atracao=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.label_descricao_atracao["font"] = ft
        self.label_descricao_atracao["fg"] = "#333333"
        self.label_descricao_atracao["justify"] = "center"
        self.label_descricao_atracao["text"] = "Descrição da atração:"
        self.label_descricao_atracao.place(x=50,y=180,width=119,height=30)

        self.caixa_descricao=tk.Entry(root)
        self.caixa_descricao["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.caixa_descricao["font"] = ft
        self.caixa_descricao["fg"] = "#333333"
        self.caixa_descricao["justify"] = "center"
        self.caixa_descricao["text"] = "Descrição atração"
        self.caixa_descricao.place(x=70,y=210,width=276,height=25)

        #Data
        self.label_data_atracao=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.label_data_atracao["font"] = ft
        self.label_data_atracao["fg"] = "#333333"
        self.label_data_atracao["justify"] = "center"
        self.label_data_atracao["text"] = "Data:"
        self.label_data_atracao.place(x=15,y=240,width=109,height=30)

        self.caixa_data_atracao=tk.Entry(root)
        self.caixa_data_atracao["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.caixa_data_atracao["font"] = ft
        self.caixa_data_atracao["fg"] = "#333333"
        self.caixa_data_atracao["justify"] = "center"
        self.caixa_data_atracao["text"] = "Data da atração"
        self.caixa_data_atracao.place(x=70,y=270,width=76,height=25)

        #Hora
        self.label_hora_atracao=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.label_hora_atracao["font"] = ft
        self.label_hora_atracao["fg"] = "#333333"
        self.label_hora_atracao["justify"] = "center"
        self.label_hora_atracao["text"] = "Hora:"
        self.label_hora_atracao.place(x=130,y=240,width=109,height=30)

        self.caixa_hora_atracao=tk.Entry(root)
        self.caixa_hora_atracao["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.caixa_hora_atracao["font"] = ft
        self.caixa_hora_atracao["fg"] = "#333333"
        self.caixa_hora_atracao["justify"] = "center"
        self.caixa_hora_atracao["text"] = "Hora da atração"
        self.caixa_hora_atracao.place(x=195,y=270,width=76,height=25)

        #mensagem de aviso caso a obra tenha sido adicionada com sucesso ou falhe
        self.label_mensagem=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.label_mensagem["font"] = ft
        self.label_mensagem["fg"] = "#333333"
        self.label_mensagem["justify"] = "center"
        self.label_mensagem["text"] = ""
        self.label_mensagem.place(x=80,y=305,width=0,height=0)

        #botao para enviar, nele ao apertar ele vê qual a função 'self.funcao' está dentro dela e faz oq tem dentor do if ou elif ou else
        self.button_ok=tk.Button(root)
        self.button_ok["bg"] = "light green"
        ft = tkFont.Font(family='Times',size=10)
        self.button_ok["font"] = ft
        self.button_ok["justify"] = "center"
        self.button_ok["text"] = "Ok"
        self.button_ok.place(x=160,y=325,width=111,height=30)
        self.button_ok["command"] = self.ok

        self.button_adicionar_atracao=tk.Button(root)
        self.button_adicionar_atracao["bg"] = "green"
        ft = tkFont.Font(family='Times',size=10)
        self.button_adicionar_atracao["font"] = ft
        self.button_adicionar_atracao["fg"] = "#000000"
        self.button_adicionar_atracao["justify"] = "center"
        self.button_adicionar_atracao["text"] = "Adicionar Atração"
        self.button_adicionar_atracao.place(x=460,y=140,width=111,height=30)
        self.button_adicionar_atracao["command"] = self.adicionarObras

        self.button_excluir_atracao=tk.Button(root)
        self.button_excluir_atracao["bg"] = "red"
        ft = tkFont.Font(family='Times',size=10)
        self.button_excluir_atracao["font"] = ft
        self.button_excluir_atracao["fg"] = "#000000"
        self.button_excluir_atracao["justify"] = "center"
        self.button_excluir_atracao["text"] = "Excluir Atração"
        self.button_excluir_atracao.place(x=460,y=190,width=111,height=30)
        self.button_excluir_atracao["command"] = self.excluirObras

        self.button_consultar_atracoes=tk.Button(root)
        self.button_consultar_atracoes["bg"] = "yellow"
        ft = tkFont.Font(family='Times',size=10)
        self.button_consultar_atracoes["font"] = ft
        self.button_consultar_atracoes["fg"] = "#000000"
        self.button_consultar_atracoes["justify"] = "center"
        self.button_consultar_atracoes["text"] = "Ver Obras"
        self.button_consultar_atracoes.place(x=460,y=240,width=111,height=30)
        self.button_consultar_atracoes["command"] = self.consultar_atracoes

        #para saber qual função será usado
        self.funcao = 'adicionar'
        self.lista_de_obras = []

    def adicionarObras(self):
        #aparecer com a descrição(caso tenha sumido)
        self.label_descricao_atracao.place(width=119,height=30)
        self.caixa_descricao.place(width=276,height=25)

        #aparecer com a data(caso tenha sumido)
        self.label_data_atracao.place(x=15,y=240,width=109,height=30)
        self.caixa_data_atracao.place(x=70,y=270,width=76,height=25)

        #aparecer com a hora(caso tenha sumido)
        self.label_hora_atracao.place(x=130,y=240,width=109,height=30)
        self.caixa_hora_atracao.place(x=195,y=270,width=76,height=25)

        #configurando a mensagem
        self.label_mensagem.place(x=80,y=295,width=280,height=30)
        self.label_mensagem['text'] = ''

        self.button_ok.place(x=160,y=325)

        self.funcao = 'adicionar'

    def excluirObras(self):
        #sumir com descricao
        self.label_descricao_atracao.place(width=0,height=0)
        self.caixa_descricao.place(width=0,height=0)

        #sumir Data
        self.label_data_atracao.place(width=0,height=0)
        self.caixa_data_atracao.place(width=0,height=0)

        #sumir Hora
        self.label_hora_atracao.place(width=0,height=0)
        self.caixa_hora_atracao.place(width=0,height=0)

        self.button_ok.place(x=150,y=195)

        #mudar posicao do texto e colocar para aparecer
        self.label_mensagem.place(x=65,y=165,width=280,height=30)
        self.label_mensagem['text'] = ''

        self.funcao = 'excluir'
    
    def consultar_atracoes(self):
        self.funcao = 'consultar'
        conexao = sqlite3.connect('atracoes.db')
        sql = conexao.cursor()
        sql.execute("SELECT * FROM atracao")
        registros = sql.fetchall()
        for reg in registros:
            for i in range(1):
                self.nome = reg[0]
                self.descricao = reg[1]
                self.data = reg[2]
                self.hora = reg[3]
                print(f'Nome da atração: {reg[0]} \nDescrição: {reg[1]}\nData: {reg[2]}\nHora: {reg[3]}')
                print()
        conexao.close()
        
    def ok(self):
        conexao = sqlite3.connect('atracoes.db')
        sql = conexao.cursor()
        if self.funcao == 'adicionar':
            try:
                data = self.caixa_data_atracao.get().replace('/','')
                hora = self.caixa_hora_atracao.get().replace(':','')
                int(data)
                int(hora)
                sql.execute('INSERT INTO atracao (nome,descricao,data,hora) VALUES (?,?,?,?)', (self.caixa_nome_atracao.get(), self.caixa_descricao.get(), self.caixa_data_atracao.get(), self.caixa_hora_atracao.get()))
                print('Atração adicionado com sucesso!')
                self.label_mensagem['fg'] = 'green'
                self.label_mensagem['text'] = 'Obra adicionada com sucesso!'
                self.label_mensagem.place(x=80,y=295,width=280,height=30)
                nome_atracao = self.caixa_nome_atracao.get()
                descricao = self.caixa_descricao.get()
                data_atracao = self.caixa_data_atracao.get()
                hora_atracao = self.caixa_hora_atracao.get()
                self.obra = {nome_atracao:[descricao,data_atracao,hora_atracao]}
                self.lista_de_obras.append(self.obra)
                conexao.commit()
                conexao.close()
            except Exception:
                self.label_mensagem['text'] = 'Erro ao adicionar a atração!'
                self.label_mensagem['fg'] = 'red'
                self.label_mensagem.place(x=80,y=295,width=280,height=30)
                print('Erro ao adicionar a atração!')
            finally:
                self.caixa_nome_atracao.delete(0, 'end')
                self.caixa_descricao.delete(0, 'end')
                self.caixa_data_atracao.delete(0, 'end')
                self.caixa_hora_atracao.delete(0, 'end')

        elif self.funcao =='excluir':
            self.label_mensagem = ''
            sql.execute('SELECT * FROM atracao WHERE nome = ?', (self.caixa_nome_atracao.get(),))
            self.verificar = sql.fetchone()
            if self.verificar is not None:
                sql.execute('DELETE FROM atracao WHERE nome = ?', (self.caixa_nome_atracao.get(),))
            else:
                print('Aluno não cadastrado') 
            conexao.commit()
            conexao.close()
            self.label_mensagem['fg'] = 'red'
            self.label_mensagem['text'] = 'Obra excluida com sucesso!'
            self.caixa_nome_atracao.delete(0, 'end')
            self.caixa_descricao.delete(0, 'end')
            self.caixa_data_atracao.delete(0, 'end')
            self.caixa_hora_atracao.delete(0, 'end')

        else:
            for i in range(0,1):
                cont=0
                print('Opção não existe')
                while cont>=1:
                    cont+=1

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
