from MortgageCalculator import MortgageCalculator
from view.print_view import PrintView
from view.graph_view import GraphView


class Controller(object):
    """The Controller class for the mortgage calculator"""

    def __init__(self):
        super(Controller, self).__init__()
        #self.view = GraphView()
        self.view = PrintView()

    def calculate_mortgage_schedule(self):
        principal = 200000
        rate = 6.5
        term = 30

        # Run the calculation
        schedule = MortgageCalculator.calculate_schedule(principal, rate, term)

        # Display it
        self.view.display_schedule(schedule)


controller = Controller()
controller.calculate_mortgage_schedule()
