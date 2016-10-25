class MortgageMetrics:
    """Objects of this class will hold metrics of an amortization table"""

    def __init__(self):
        self.totals = {'payments': 0, 'interest': 0, 'principal': 0}
        self.metrics = {'Interest': 0, 'InterestOverPrincipal': 0}