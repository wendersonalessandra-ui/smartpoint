from funcionarios import validar,pesquisar_funcionario, guardar_funcionario, remover_funcionario,alterar_funcionario
from unittest.mock import patch

resultado = validar(
 "João",
 30,
"receção",
"123456")
assert resultado== (True,"")

funcionarios = [
    {"nome": "Carla"},
    {"nome": "Maria"},
    {"nome": "Carlos"}
]
resultado = pesquisar_funcionario (funcionarios,"CAR")
assert resultado == [{"nome": "Carla"},{"nome": "Carlos"}]

with patch ("funcionarios.inserir_funcionario") as mock_inserir: 
 guardar_funcionario ( "joão", "receção", 30, "912345678")
 mock_inserir.assert_called_once_with(
  "joão",
  30,
  "receção",
  "912345678"
 )



with patch ("funcionarios.remover_funcionario_db") as mock_remover: 
 remover_funcionario (1)
 mock_remover.assert_called_once_with(1)



with patch ("funcionarios.alterar_funcionario_db") as mock_alterar:
 alterar_funcionario(
    1,
    "Carla Silva",
    29,
    "Receção",
    "999999999"
)
mock_alterar.assert_called_once_with(
     1,
     "Carla Silva",
     29,
     "Receção",
     "999999999"
)


    