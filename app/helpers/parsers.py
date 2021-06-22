from app.helpers.formatSalary import unmaskSalary
from app.helpers.formatSalary import maskSalary
from app.helpers.formatSalary import truncate

def buildPayload (employeesWithBonus):
    shares = list()
    totalEmployees = 0
    totalBonus = 0
    
    for employer in employeesWithBonus:

        totalEmployees +=1 
        totalBonus+= truncate(employer['bonus'])

        shares.append({
            "matricula": employer['matricula'],
            "nome": employer['nome'],
            "valor_da_participacao": maskSalary(employer['bonus']),
        })
    
    return {
        
            "participacoes" : shares,
            "total_de_funcionarios": totalEmployees,
            "total_distribuido":maskSalary(totalBonus),
        }