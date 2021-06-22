import math
def unmaskSalary(salary):
    return float(salary.replace("R$", "").replace(" ", "").replace(".", "").replace(",", "."))

def maskSalary(salary):
    return 'R$ '+ str('{:,.2f}'.format(truncate(salary))).replace(',','v').replace('.',',').replace('v','.')
                    
def truncate(data):
    return  math.floor(data * 10 ** 2) / 10 ** 2