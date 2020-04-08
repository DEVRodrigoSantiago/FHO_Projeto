import sqlite3

path = r'/home/eric/Área de Trabalho/FHO/Exercicios_Python/UNI/Topicos de Programação/Trabalho_Pratico'

conn = sqlite3.connect(path+r'/banco.db')
conn.close()
