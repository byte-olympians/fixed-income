from .mortgage_metrics import MortgageMetrics


class AmortizationSchedule:
    """Class that holds details of a mortgage amortization schedule. It will have details of the monthly payments, sum
    totals of the payments and percentages of the interests"""

    def __init__(self):
        self.payment_schedule = []
        self.totals = {'payments': 0, 'interest': 0, 'principal': 0}
        self.metrics = {'Interest': 0, 'InterestOverPrincipal': 0}
        self.mortgage_metrics = None

    def __str__(self):
        str_ = ""

        for payment in self.payment_schedule:
            str_ += payment.__str__() + "\n"

        str_ += "\nTotal payments: {},\
              Total Principal Paid: {},\
              Total Interest Paid: {}".format(round(self.mortgage_metrics.totals['payments'], 2),
                                              round(
                                                  self.mortgage_metrics.totals['principal'], 2),
                                              round(self.mortgage_metrics.totals['interest'], 2))

        str_ += "\nInterest Percentage: {}".format(
            round(self.mortgage_metrics.metrics['Interest'], 2))
        str_ += "\nInterest as Percentage of Principal: {}".format(
            round(self.mortgage_metrics.metrics['InterestOverPrincipal'], 2))

        return str_
