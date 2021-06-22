from datetime import date, datetime

def calcTime(admissionDate):

    admissionDateFormated = datetime.strptime(admissionDate,'%Y-%m-%d')
    today = datetime.today().strftime('%m-%d-%Y')
    todayFormated = datetime.strptime(today, '%m-%d-%Y')
    totalYears= (todayFormated-admissionDateFormated).days / 365.25

    return totalYears
