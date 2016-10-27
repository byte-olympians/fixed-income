from model import *
from formula import Formula

class Calculator:
    def __init__(self):
        pass
    
    def pmt_schedule(self, mortgage):
        schedule = []
        balance = mortgage.principal
        while mortgage.month_left >= 1:
            period = mortgage.term * 12 - mortgage.month_left + 1
            interest_pmt = Formula.calculate_interest_pmt(balance, mortgage.rate)
            principal_pmt = mortgage.pmt - interest_pmt
            balance -= principal_pmt
            i = [period, round(mortgage.pmt, 2), round(interest_pmt, 2), round(principal_pmt, 2), round(balance, 2)]
            schedule.append(i)
            mortgage.month_left -= 1
        return schedule
        
if __name__ == "__main__":
    schedule = Calculator()
    print (schedule.pmt_schedule(Mortgage(1000000, 0.05, 30, 30)))
