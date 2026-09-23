import sqlite3
def criar_tabela_funcionarios():
 conexao = sqlite3.connect("smartpoint.db")
 cursor = conexao.cursor()
 cursor.execute(""" CREATE TABLE IF NOT EXISTS funcionarios(
 id INTEGER PRIMARY KEY,
 nome TEXT NOT NULL,
 idade INTEGER NOT NULL,
 departamento TEXT NOT NULL,
 telefone TEXT NOT NULL
 );""")

 conexao.commit()
 conexao.close()
 
def inserir_funcionario(nome, idade, departamento, telefone):
    conexao = sqlite3.connect("smartpoint.db")
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO funcionarios(nome, idade, departamento, telefone)
    VALUES (?,?,?,?);""",
    (nome, idade, departamento, telefone)
    )
    conexao.commit()
    conexao.close()
#inserir_funcionario("Bruno",40,"Manutenção","913456789")
# cursor.execute("""
# SELECT * FROM funcionarios;
# """)
# funcionarios = cursor.fetchall()
# print (funcionarios)
def listar_funcionarios():
    conexao = sqlite3.connect("smartpoint.db")
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM funcionarios;
    """)
    funcionarios = cursor.fetchall()
    conexao.close()
    return funcionarios
#funcionarios = listar_funcionarios()    
#print(funcionarios)
def alterar_funcionario_db(id_funcionario, novo_nome, nova_idade, novo_departamento, novo_telefone):
    conexao= sqlite3.connect("smartpoint.db")
    cursor= conexao.cursor()
    cursor.execute("""
    UPDATE funcionarios 
    SET 
    nome=?,
    idade=?,
    departamento=?,
    telefone=?
    WHERE id =?;""",( novo_nome, nova_idade, novo_departamento, novo_telefone, id_funcionario))
    conexao.commit()
    conexao.close()
#alterar_funcionario(1, "Bruno Silva", 41, "Receção", "919999999")
#funcionarios = listar_funcionarios()
#print(funcionarios)    
def remover_funcionario_db(id_funcionario):
    conexao= sqlite3.connect("smartpoint.db")
    cursor = conexao.cursor()
    cursor.execute("""
    DELETE FROM funcionarios
    WHERE id =?;""",(id_funcionario,))
    conexao.commit()
    conexao.close()
#remover_funcionario(2)  
#inserir_funcionario("Ana", 30, "Cozinha","911111111") 
#funcionarios = listar_funcionarios() 
#print(funcionarios)

