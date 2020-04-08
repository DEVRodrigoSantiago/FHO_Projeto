# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:35:05 2020

"""

import csv 
import sqlite3
from tkinter import *
  
class Banco:
    path = r'/home/eric/Área de Trabalho/FHO/Exercicios_Python/UNI/Topicos de Programação/Trabalho_Pratico'+r'/banco.db'
    
    def conectaBanco(self):
        conn = sqlite3.connect(self.path)
        print ('Aberta a Conexão')
        return conn
    
    def fechaBanco(self,conn):
        conn.close()
        print('Conexão Fechada')
        
    #Método verificar senha
    
    @staticmethod
    def verificaSenha(login,senha):
        conecta = Banco()
        #definindo o cursor 
        
        conn = conecta.conectaBanco()
        
        cursor = conn.cursor()
        """
        dados = cursor.execute(
            "SELECT * FROM acesso WHERE login = ?",(str(login),))
    
        print(dados)
        
        if(dados):
            print('Autentificado')
            return "Autenticado"
        else:
            print('Usuário ou senha incorreto')
            return "Erro na autenticação
        """
    
    
    @staticmethod
    def CadastraUsuario(login,senha):
        conecta = Banco()
        #definindo o cursor 
        lista = (
            (login, senha),
            ('teste', 4321)
            )
        conn = conecta.conectaBanco()
        cursor = conn.cursor()

        #cursor.executemany(INSERT INTO Usuarios VALUES (?,?), lista[0][0], lista[0][1])
        #print('Dados inseridos com sucesso!')
        

    @staticmethod
    def CriarTabela():
        conecta = Banco()
        #definindo o cursor 
        
        conn = conecta.conectaBanco()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE Usuarios (Login varchar(80), Senha varchar(80), PRIMARY KEY(Login));")
        print('Tabela criada com sucesso!')
        conn.commit()
        print('Commit da criação da tabela realizado com sucesso!')
        cursor.execute("INSERT INTO Usuarios VALUES('eric', 1234)")
        print('Dados inseridos com sucesso.')
        conn.commit()
        print('Commit da criação do insert realizado com sucesso!')
        cursor.execute("SELECT * FROM Usuarios;")
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]}, {row[1]}")

class Application(Banco):
    def __init__(self, master=None):
        #Primeiro Container
        self.fontePadrao               = ("Arial", "10")
        self.primeiroContainer         = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()
  
        #Segundo Container
        self.segundoContainer         = Frame(master)
        self.segundoContainer["padx"] = 30
        self.segundoContainer.pack()
  
        #Terceiro Container
        self.terceiroContainer         = Frame(master)
        self.terceiroContainer["padx"] = 30
        self.terceiroContainer.pack()
  
        #Quarto Container
        self.quartoContainer         = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        #Label (Label Dados Usuario - Primeiro Container)
        self.titulo         = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        #Inputs(Entry) e Label - Segundo Container - Nome
        self.nomeLabel = Label(self.segundoContainer,text="Login", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.login          = Entry(self.segundoContainer)
        self.login["width"] = 30
        self.login["font"]  = self.fontePadrao
        self.login.pack(side=LEFT)
  
        #Inputs(Entry) e Label - Terceiro Container - Senha
        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha          = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"]  = self.fontePadrao
        self.senha["show"]  = "*"
        self.senha.pack(side=LEFT)

        def teste_hello():
            print('Hello')
  
        self.autenticar            = Button(self.quartoContainer, command = Banco.verificaSenha) 
        """self.login,self.senha""" 
        self.autenticar["text"]    = "Autenticar"
        self.autenticar["font"]    = ("Calibri", "8")
        self.autenticar["width"]   = 12
        self.autenticar.bind("<Button-1>")
        #self.autenticar["command"] = self.autenticar["text"]    = Banco.verificaSenha(self.login,self.senha)
        self.autenticar.pack()
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
        #Botão que cria uma tabela
        self.tabela            = Button(self.quartoContainer, command = Banco.CriarTabela)
        self.tabela["text"]    = "Criar Tabela"
        self.tabela["font"]    = ("Calibri", "8")
        self.tabela["width"]   = 12
        self.tabela.bind("<Button-2>")
        self.tabela.pack()
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.cadastro            = Button(self.quartoContainer, command = Banco.CadastraUsuario(self.login, self.senha))
        self.cadastro["text"]    = "Cadastrar Usuário"
        self.cadastro["font"]    = ("Calibri", "8")
        self.cadastro["width"]   = 12
        self.cadastro.bind("<Button-3>")
        self.cadastro.pack()
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack() 
        
        
    
#Fluxo principal (Main)

root = Tk()
Application(root)
root.mainloop()
