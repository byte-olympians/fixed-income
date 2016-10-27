class Formula:
    @staticmethod
    def calculate_total_pmt(principal, rate, term, amortization):
        payment = (rate / 12) * principal / (1 - ((1 + rate / 12) ** - (amortization * 12)))
        return payment
    
    @staticmethod
    def calculate_interest_pmt(balance, rate):
        interest_pmt = balance * rate / 12
        return interest_pmt
   
if __name__ == "__main__":
    print (Formula.calculate_total_pmt(1000000, 0.05, 30, 30))
    principle = Formula.calculate_total_pmt(1000000, 0.05, 30, 30) - Formula.calculate_interest_pmt(1000000, 0.05)
    print (principle)