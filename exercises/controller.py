from mortgage_calculator import Calculator
from view import *
from model import *


class Controller:
    """The Controller class for the mortgage calculator"""

    def __init__(self):
        self.calculator = Calculator()
        self.view = {"View Graph": GraphView(), "View Schedule": ScheduleView()}

    def calculate_mortgage_schedule(self, mortgage):
        # Run the calculation
        schedule = self.calculator.pmt_schedule(mortgage)
        self.view["View Schedule"].render(schedule)
        self.view["View Graph"].render(schedule)

        
controller = Controller()
controller.calculate_mortgage_schedule(Mortgage(1000000, 0.04, 30, 30))