from app.calculators.calcWeights import calcWeights
from app.calculators.calcBonus import calcBonus
from app.helpers.parsers import buildPayload

async def calcDistributions(employees: str):
    employeesWithBonus = list()

    for employer in employees.funcionarios:
        weights = calcWeights(employer['data_de_admissao'], employer['salario_bruto'], employer['area'])
        employer['bonus'] = calcBonus(employer, weights )
        employeesWithBonus.append(employer)

    return buildPayload(employeesWithBonus)





