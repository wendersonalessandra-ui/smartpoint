
from database import inserir_funcionario, alterar_funcionario_db, remover_funcionario_db

def validar(nome, idade, departamento, telefone):
    if not nome:
        return False, "Por Favor, escreva o nome do Funcionario"

    elif idade <= 0:
        return False, "Por Favor, insira uma Idade valida"

    elif departamento == "Selecione um Departamento":
        return False, "Por Favor Escolha um Departamento"

    elif not telefone:
        return False, "Insira um numero de Telefone"

    return True, ""
def pesquisar_funcionario(funcionarios, pesquisa):
 resultado_pesquisa=[]
 for funcionario in funcionarios:
   if pesquisa.lower() in funcionario["nome"].lower():
      resultado_pesquisa.append(funcionario)
 return  resultado_pesquisa 
def guardar_funcionario( nome, departamento, idade, telefone):
    inserir_funcionario(nome, idade, departamento, telefone)

def alterar_funcionario(
     id_funcionario,
     novo_nome,
     nova_idade,
     novo_departamento,
     novo_telefone
):
      

      alterar_funcionario_db(
          id_funcionario, 
          novo_nome, 
          nova_idade, 
          novo_departamento, 
          novo_telefone
)

def remover_funcionario(id_funcionario):
    remover_funcionario_db(id_funcionario)
      


