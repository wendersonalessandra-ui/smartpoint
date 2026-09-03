from dados import guardar_json

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
def guardar_funcionario(funcionarios, nome, departamento, idade, telefone):
    funcionario = {
        "nome": nome,
        "departamento": departamento,
        "idade": idade,
        "telefone": telefone
    }

    funcionarios.append(funcionario)
    guardar_json(funcionarios)

def alterar_funcionario(
     funcionarios,
     funcionario,
     novo_nome,
     nova_idade,
     novo_departamento,
     novo_telefone
):
      

      funcionario["nome"] = novo_nome
      funcionario["idade"] = nova_idade
      funcionario["departamento"] = novo_departamento
      funcionario["telefone"] = novo_telefone

       

      guardar_json(funcionarios )

def remover_funcionario(funcionarios, funcionario):
    funcionarios.remove(funcionario)
    guardar_json(funcionarios)      


