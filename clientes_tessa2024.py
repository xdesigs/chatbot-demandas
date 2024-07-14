import sqlite3

banco = sqlite3.connect('dbclientes_tessa2024')

cursor = banco.cursor()

""" cursor.execute('CREATE TABLE Clientes(nome text, data integer, projeto text)') """

""" cursor.execute("INSERT INTO Clientes VALUES('Castelinho', '150724', 'video Rells' )") """

cursor.execute("SELECT * from Clientes")
print(cursor.fetchall())

""" banco.commit() """


