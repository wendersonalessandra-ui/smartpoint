import sqlite3
conexao = sqlite3.connect("smartpoint_teste.db")
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS funcionarios(
id INTEGER PRIMARY KEY,
nome TEXT NOT NULL,
idade INTEGER NOT NULL,
departamento TEXT NOT NULL,
telefone TEXT NOT NULL

);""")
conexao.commit()

cursor.execute("""
DELETE FROM funcionarios""")
conexao.commit()


cursor.execute(""" 
INSERT INTO funcionarios(nome, idade, departamento, telefone)
VALUES (?, ?, ?, ?)
""",
("Carla", 30, "Receção", "99999999" ))
conexao.commit()

cursor.execute("""
SELECT * FROM funcionarios 
""")
funcionarios = cursor.fetchall()
print(funcionarios)

assert funcionarios [0][1] == "Carla"
conexao.close()