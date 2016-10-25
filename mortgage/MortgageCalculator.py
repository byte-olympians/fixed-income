from mortgage_formulas import MortgageFormulas
from model.amortization_schedule import AmortizationSchedule
from model.monthly_details import MonthlyDetails
from model.mortgage_metrics import MortgageMetrics


class MortgageCalculator:
    """Class that will calculate the amortization schedule and the mortgage metrics"""

    def __init__(self):
        pass

    @staticmethod
    def calculate_mortgage_metrics(amortization_schedule):
        """ Calculates the metrics for a given amortization schedule.
        :param amortization_schedule: The amortization schedule that has details of the monthly payments of a mortgage
        :return: Returns the amortization schedule with the metric values filled in
        """
        mortgage_metrics = MortgageMetrics()
        totals = mortgage_metrics.totals
        metrics = mortgage_metrics.metrics

        # Loop through the monthly payments and calculate the totals.
        for payment in amortization_schedule.payment_schedule:
            # Add to the totals
            totals['payments'] += payment.payment
            totals['interest'] += payment.interest
            totals['principal'] += payment.principal

        # Once the totals are calculated, calculate the percentage metrics
        metrics['Interest'] = totals['interest'] / totals['payments'] * 100
        metrics['InterestOverPrincipal'] = totals[
                                               'interest'] / totals['principal'] * 100

        # Return the mortgage metrics
        return mortgage_metrics

    @staticmethod
    def calculate_schedule(principal, rate, term):
        """ Calculate the amortization schedule of a mortgage
        :param principal: The Principal borrowed
        :param rate: The annual rate of interest of the mortgage
        :param term: The term of the mortgage in years
        :return:
        """

        monthly_term = MortgageFormulas.convert_term_to_monthly(term)
        monthly_payment = round(
            MortgageFormulas.calculate_monthly_payment(principal, rate, term), 2)

        principal_balance = principal
        current_month = 1
        totals = {'payments': 0, 'interest': 0, 'principal': 0}

        amortization_schedule = AmortizationSchedule()

        while current_month <= monthly_term:
            # Calculate the monthly principal and interest
            monthly_interest = round(MortgageFormulas.calculate_monthly_interest(principal_balance,
                                                                           rate), 2)

            if principal_balance > monthly_payment:
                monthly_principal = round(
                    (monthly_payment - monthly_interest), 2)
                principal_balance = round(
                    (principal_balance - monthly_principal), 2)
            else:
                # This is typically for the last month when the balance is less than the
                # monthly payment
                monthly_interest = 0
                monthly_principal = principal_balance
                principal_balance = 0
                monthly_payment = monthly_principal

            # Add to the totals
            totals['payments'] += monthly_payment
            totals['interest'] += monthly_interest
            totals['principal'] += monthly_principal

            monthly_details = MonthlyDetails(current_month,
                                             monthly_payment,
                                             monthly_principal,
                                             monthly_interest,
                                             principal_balance,
                                             round(totals['interest'], 2),
                                             round(totals['principal'], 2),
                                             round(totals['payments'], 2)
                                             )

            # Store the monthly payment in the amortization schedule
            amortization_schedule.payment_schedule.append(monthly_details)

            # Increment the month counter
            current_month += 1

        mortgage_metrics = MortgageCalculator.calculate_mortgage_metrics(amortization_schedule)
        amortization_schedule.mortgage_metrics = mortgage_metrics

        return amortization_schedule
