from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

def testCalculateDistributionSuccess():
    response = client.post(
    "/calculate_distribution/",
    json={
            "funcionarios": [
                {
                    "matricula":"0007961",
                    "nome":"Francesca Hewitt",
                    "area":"Contabilidade",
                    "cargo":"Auxiliar de Contabilidade",
                    "salario_bruto":"R$ 2.101,68",
                    "data_de_admissao":"2015-06-21"
                },
                {
                    "matricula":"0006806",
                    "nome":"Ella Hale",
                    "area":"Diretoria",
                    "cargo":"Auxiliar Administrativo",
                    "salario_bruto":"R$ 2.571,73",
                    "data_de_admissao":"2014-07-27"
                }
	        ]
        })
    assert response.status_code == 200
    assert response.json() == {
    "participacoes": [
        {
            "matricula": "0007961",
            "nome": "Francesca Hewitt",
            "valor_da_participacao": "R$ 1.666,66"
        },
        {
            "matricula": "0006806",
            "nome": "Ella Hale",
            "valor_da_participacao": "R$ 1.333,33"
        }
    ],
    "total_de_funcionarios": 2,
    "total_distribuido": "R$ 2.999,99"
}

def testCalculateDistributionFailed():
    response = client.post(
    "/calculate_distribution/",
    json={
            "testeteste": [
                {
                    "matricula":"0007961",
                    "nome":"Francesca Hewitt",
                    "area":"Contabilidade",
                    "cargo":"Auxiliar de Contabilidade",
                    "salario_bruto":"R$ 8.000,00",
                    "data_de_admissao":"2015-06-21"
                },
                {
                    "matricula":"0006806",
                    "nome":"Ella Hale",
                    "area":"Diretoria",
                    "cargo":"Auxiliar Administrativo",
                    "salario_bruto":"R$ 2.571,73",
                    "data_de_admissao":"2014-07-27"
                }
	        ]
        })
    assert response.status_code == 422
