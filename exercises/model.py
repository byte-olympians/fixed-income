from formula import Formula

class Mortgage:
    def __init__(self, principal, rate, term, amortization):
        self.principal = principal
        self.rate = rate
        self.term = term
        self.amortization = amortization
        self.month_left = self.term * 12
        self.pmt = Formula.calculate_total_pmt(self.principal, self.rate, self.term, self.amortization)
        

if __name__ == "__main__":
    mortgage = Mortgage(1000000, 0.05, 30, 30)
    print (mortgage.month_left)