import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class ScheduleView:
    def render(self, schedule):
        for i in schedule:
            print (i)
    
class GraphView:
    def render(self, schedule):
        x_axis = [i[0] for i in schedule]
        mortgage_pmt = [i[1] for i in schedule]
        interest_pmt = [i[2] for i in schedule]
        principal_pmt = [i[3] for i in schedule]
        plt.plot(x_axis, mortgage_pmt, label = 'Mortgage Payment')
        plt.plot(x_axis, interest_pmt, label = 'Interest Payment')
        plt.plot(x_axis, principal_pmt, label = 'Principal Payment')
        plt.xlabel('Periods')
        plt.ylabel('Payments')
        plt.title('Mortgage Payment Schedule Graph')
        plt.savefig('schedule.jpg')

if __name__ == "__main__":
    view = GraphView()
    view.render([[1, 2, 3], [4, 5, 6]])