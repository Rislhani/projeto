import sqlite3

conexao = sqlite3.connect('atracoes.db')
sql = conexao.cursor()

sql.execute('CREATE TABLE atracao (nome,descricao,data,hora)')