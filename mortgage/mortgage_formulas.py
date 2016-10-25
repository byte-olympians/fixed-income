class MortgageFormulas:
    """Mortgage formula class. Calculates the monthly payment, interest, etc"""

    def __init__(self):
        pass

    @staticmethod
    def convert_rate_to_monthly(rate):
        """Convert the rate from an annual percentage to a monthly fraction."""
        return rate / 12 / 100

    @staticmethod
    def convert_term_to_monthly(term):
        """Convert the term of the mortgage from number of years to number of months"""
        return term * 12

    @staticmethod
    def calculate_monthly_payment(principal, rate, term):
        """Calculate the monthly payment for a given mortgage. This is the main formula"""
        monthly_rate = MortgageFormulas.convert_rate_to_monthly(rate)
        monthly_term = MortgageFormulas.convert_term_to_monthly(term)

        return (monthly_rate * principal) / (1 - ((1 + monthly_rate) ** (-1 * monthly_term)))

    @staticmethod
    def calculate_new_monthly_payment(principal, rate, term):
        monthly_rate = MortgageFormulas.convert_rate_to_monthly(rate)
        monthly_term = MortgageFormulas.convert_term_to_monthly(term)

        factor = (1 + monthly_rate) ** monthly_term

        return (monthly_rate * factor * principal) / (factor - 1)

    @staticmethod
    def calculate_loan_balance(principal, rate, term, months_elapsed):
        """ Calculate for a given mortgage, based on months_elapsed, what is the outstanding
        principal balance
        :param principal:
        :param rate:
        :param term:
        :param months_elapsed:
        :return: The balance of the principal amount yet to be re-paid
        """
        monthly_rate = MortgageFormulas.convert_rate_to_monthly(rate)
        monthly_term = MortgageFormulas.convert_term_to_monthly(term)

        factor = (1 + monthly_rate) ** monthly_term

        return (factor - ((1 + monthly_rate) ** months_elapsed)) * principal / (factor - 1)

    @staticmethod
    def calculate_monthly_interest(principal_balance, rate):
        monthly_rate = MortgageFormulas.convert_rate_to_monthly(rate)
        return principal_balance * monthly_rate

