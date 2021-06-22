from app.utils.constants import weights
from app.utils.calcTime import calcTime
from app.helpers.formatSalary import unmaskSalary

def calcWeights(admissionDate, salary, field):
    
    admissionDurationWeight = calcAdmissionDurationWeight(admissionDate)
    salaryWeight = calcSalaryWeight(salary)
    fieldWeight = findFieldWeight(field)

    return {
        'admissionDurationWeight':admissionDurationWeight,
        'salaryWeight':salaryWeight,
        'fieldWeight':fieldWeight,
    }

def calcAdmissionDurationWeight(admissionDate):
    admissionDuration = calcTime(admissionDate)

    for weight in range(len(weights['time'])):
        if(admissionDuration >= float(weights['time'][weight]['key'])):
            lowestKey = weight

    return float(weights['time'][lowestKey]['value'])


def calcSalaryWeight(salary):
    salaryFormated = unmaskSalary(salary)
    
    for weight in range(len(weights['salary'])):
        if(salaryFormated >= float(weights['salary'][weight]['key'])):
            lowestKey = weight

    return float(weights['salary'][lowestKey]['value'])


def findFieldWeight(field):
    
    for weight in range(len(weights['field'])):
        if(field == weights['field'][weight]['key']):

            return float(weights['field'][weight]['value'])

   