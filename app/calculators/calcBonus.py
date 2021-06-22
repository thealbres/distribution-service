from app.helpers.formatSalary import unmaskSalary
from app.helpers.formatSalary import maskSalary

def calcBonus(employer, weights):
    salaryFormated = unmaskSalary(employer['salario_bruto'])

    bonus = (((salaryFormated * weights['admissionDurationWeight']) + 
        (salaryFormated * weights['fieldWeight'] )) /  
        (salaryFormated * weights['salaryWeight'] )) * \
        1000

    return bonus
