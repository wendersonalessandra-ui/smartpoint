
import streamlit as st
from funcionarios import validar, pesquisar_funcionario, guardar_funcionario, alterar_funcionario, remover_funcionario
from database import criar_tabela_funcionarios, listar_funcionarios

criar_tabela_funcionarios()


DEPARTAMENTOS = [
    "Restauração",
    "Receção",
    "Housekeeping",
    "Cozinha",
    "Lavandaria",
    "Manutenção"
]
#--------------------------
#CONFIGURAÇÃO DA PAGINA 
#--------------------------

st.set_page_config(
    page_title="smartpoint",
    page_icon="⏱️",
    layout="wide",
    initial_sidebar_state="expanded"
)

#------------------------
#TÍTULO
#------------------------
st.title("⏱️ SmartPoint")

st.subheader("A forma inteligente de gerir equipas.")

st.divider()

st.success("Bem-vindo ao SmartPoint!")
if "funcionarios" not  in st.session_state:
      st.session_state.funcionarios=[]




if not st.session_state.funcionarios:
    st.session_state.funcionarios =listar_funcionarios() 

if "mensagem_sucesso" in st.session_state:
    st.success(st.session_state.mensagem_sucesso)
    del st.session_state.mensagem_sucesso        

#Formulario      
def mostrar_formulario():     
 st.title("Formulário ")
 col1, col2 =st.columns(2) 
 with col1:
  nome= st.text_input("Escreva o nome do Funcionario")
  departamento = st.selectbox(
    "Departamento",
    ["Selecione um Departamento"] + DEPARTAMENTOS
)
 with col2:
  idade = st.number_input(
    "Idade",
    min_value=0,
    step=1,
    format="%d")
  telefone= st.text_input("Telefone") 
 botao=st.button("Guardar")
 return nome,departamento, idade, telefone, botao
nome, departamento, idade, telefone, botao = mostrar_formulario()



# carregar ficheiro
if botao:
    valido, mensagem = validar(
        nome,
        idade,
        departamento,
        telefone
    )

    if valido:
        guardar_funcionario(
            nome,
            departamento,
            idade,
            telefone
        )
        st.session_state.funcionarios = listar_funcionarios()
        st.success(f"Funcionário {nome} registado com sucesso!")
        st.divider()
    else:
        st.error(mensagem)



# Faz a pesquisa de Funcionario


pesquisa = st.text_input("🔍 Procurar funcionário")
resultado_pesquisa = pesquisar_funcionario(
    st.session_state.funcionarios,
    pesquisa
)     
for indice, funcionario in enumerate(resultado_pesquisa):
     st.write(funcionario["nome"])
     editar = st.button("✏️", key=f"editar_{indice}")
     if editar:
       st.session_state.funcionario_em_edicao=funcionario
       

     remover=st.button("🗑️", key=f"remover_{indice}")
     
     if remover:
      remover_funcionario(
        funcionario ["id"],
    )
      st.session_state.funcionarios = listar_funcionarios()
      st.session_state.mensagem_sucesso = "Funcionario revomido com sucesso!"
      st.rerun()


# Mostrar funcionario
def mostrar_funcionarios(funcionarios,pesquisa, resultado_pesquisa):
 st.subheader("📋 Funcionários Registados")
 if pesquisa:
   st.dataframe(
           resultado_pesquisa,
           use_container_width=True
       )
 else:
    st.dataframe(
               funcionarios,
               use_container_width=True
           )
mostrar_funcionarios(st.session_state.funcionarios, pesquisa, resultado_pesquisa)   
if "funcionario_em_edicao" in st.session_state:

     st.success("ÁREA DE EDIÇÃO")

     funcionario = st.session_state.funcionario_em_edicao

     st.divider()
     st.subheader("✏️ Editar Funcionário")

     novo_nome = st.text_input(
        "Nome",
        value=funcionario["nome"], 
        key="editar_nome"
    )
     
        
     novo_departamento = st.selectbox(
     "Departamento",
     DEPARTAMENTOS,
     index=DEPARTAMENTOS.index(funcionario["departamento"]),
     key="editar_departamento"
)
      
     nova_idade = st.number_input(
        "Idade",
        min_value=0,
        value=funcionario["idade"],
        step=1,
        key="editar_idade"
    )
     novo_telefone = st.text_input(
        "Telefone",
        value=funcionario["telefone"],
        key="editar_telefone"
        )
     guardar_alteracoes= st.button("💾 Guardar Alterações", key="guardar_alteracoes")




      
    
     if guardar_alteracoes:
      valido, mensagem = validar(
        novo_nome,
        nova_idade,
        novo_departamento,
        novo_telefone
    )

      if valido:
         alterar_funcionario(
            funcionario["id"],
            novo_nome,
            nova_idade,
            novo_departamento,
            novo_telefone
        )
         st.session_state.funcionarios = listar_funcionarios()
         st.session_state.mensagem_sucesso = "Funcionário alterado e guardado com sucesso!"
         st.rerun()
         
         
      else:
        st.error(mensagem)


