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
            if mortgage.month_left == 1:
                principal_pmt = balance
            else: 
                principal_pmt = mortgage.pmt - interest_pmt
            balance -= principal_pmt
            i = [period, round(mortgage.pmt, 2), round(interest_pmt, 2), round(principal_pmt, 2), round(balance, 2)]
            schedule.append(i)
            mortgage.month_left -= 1
        return schedule
        
    def cumulative_schedule(self, mortgage):
        schedule = []
        balance = mortgage.principal
        cum_tot_payment = 0
        cum_interest_pmt = 0
        cum_principal_pmt = 0
        while mortgage.month_left >= 1:
            period = mortgage.term * 12 - mortgage.month_left + 1
            cum_tot_payment += mortgage.pmt 
            cum_interest_pmt += Formula.calculate_interest_pmt(balance, mortgage.rate)
            if mortgage.month_left == 1:
                principal_pmt = balance
            else: 
                principal_pmt = mortgage.pmt - Formula.calculate_interest_pmt(balance,mortgage.rate)
            cum_principal_pmt += principal_pmt
            balance -= principal_pmt
            i = [period, round(cum_tot_payment, 2), round(cum_interest_pmt, 2), round(cum_principal_pmt), round(balance, 2)]
            schedule.append(i)
            mortgage.month_left -= 1
        return schedule
        
if __name__ == "__main__":
    schedule = Calculator()
    view = schedule.pmt_schedule(Mortgage(1000000, 0.05, 10, 25))
    for i in view:
        print (i)
    print (schedule.cumulative_schedule(Mortgage(1000000, 0.05, 10, 25)))
    
