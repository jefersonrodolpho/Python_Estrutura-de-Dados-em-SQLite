import sqlite3

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()
sql = """ create table cadastro (codigo integer, nome text, idade integer) """

cursor.execute(sql)

sql = """ insert into cadastro (codigo, nome, idade) values (1284, 'Jeferson Rodolpho', 32) """

cursor.execute(sql) # executa a instrução do SQL
conector.commit() # vai salvar os arquivos no Banco de Dados
cursor.close() # fecha o cursor
conector.close() #fecha o conector do Banco de Dados