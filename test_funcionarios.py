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
funcionarios = []
with patch ("funcionarios.guardar_json") as mock_guardar: 
 guardar_funcionario (funcionarios, "joão", "receção", 30, "912345678")
 mock_guardar.assert_called_once_with(funcionarios)
assert funcionarios ==[{ "nome":"joão", "departamento":"receção","idade": 30,"telefone": "912345678"}]


funcionarios = [
    {"nome": "Carla"},
    {"nome": "Maria"},
    {"nome": "Carlos"}
]
with patch ("funcionarios.guardar_json") as mock_guardar: 
 remover_funcionario (funcionarios,{"nome": "Maria"})
 mock_guardar.assert_called_once_with(funcionarios)
assert funcionarios ==[{ "nome":"Carla"}, {"nome": "Carlos"}]

funcionarios = [
    {
        "nome": "Carla",
        "idade": 28,
        "departamento": "Receção",
        "telefone": "912345678"
    },
    {
        "nome": "Maria",
        "idade": 31,
        "departamento": "Cozinha",
        "telefone": "923456789"
    }
]
funcionario= funcionarios [0]
with patch ("funcionarios.guardar_json") as mock_guardar:
 alterar_funcionario(
    funcionarios,
    funcionario,
    "Carla Silva",
    29,
    "Receção",
    "999999999"
)
mock_guardar.assert_called_once_with(funcionarios)
assert funcionarios == [
    {
        "nome": "Carla Silva",
        "idade": 29,
        "departamento": "Receção",
        "telefone": "999999999"
    },
    {
        "nome": "Maria",
        "idade": 31,
        "departamento": "Cozinha",
        "telefone": "923456789"
    }
]

    