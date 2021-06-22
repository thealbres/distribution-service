from fastapi import APIRouter, Body
from pydantic import BaseModel
from app.services.calcDistributions import calcDistributions

router = APIRouter()

class Employees(BaseModel):
    funcionarios: list
    
@router.post("/calculate_distribution/", tags=["calculations"])
async def readEmployees(employees: Employees = Body(..., example ={
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
        }
	)
):

    return await calcDistributions(employees)
