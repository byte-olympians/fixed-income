import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class ScheduleView:
    def render(self, schedule):
        for i in schedule:
            print (i)
            
class GraphView:
    def render(self, schedule, cumulative = None):
        x_axis = [i[0] for i in schedule]
        plt.xlabel('Periods')
        plt.ylabel('Payments')
        if cumulative is not None:
            mortgage_pmt = [i[1] / 1000 for i in schedule]
            interest_pmt = [i[2] / 1000 for i in schedule]
            principal_pmt = [i[3] / 1000 for i in schedule]
            plt.plot(x_axis, mortgage_pmt, label = 'Total')
            plt.plot(x_axis, interest_pmt, label = 'Interest')
            plt.plot(x_axis, principal_pmt, label = 'Principal')
            plt.legend(loc = 0)
            plt.title("Cummulative Mortgage Payment Schedule('000)")
            plt.savefig('cummulative_schedule.jpg')
            plt.gcf().clear()
        else:
            mortgage_pmt = [i[1] for i in schedule]
            interest_pmt = [i[2] for i in schedule]
            principal_pmt = [i[3] for i in schedule]
            plt.plot(x_axis, mortgage_pmt, label = 'Total')
            plt.plot(x_axis, interest_pmt, label = 'Interest')
            plt.plot(x_axis, principal_pmt, label = 'Principal')
            plt.legend(loc = 0)
            plt.title('Mortgage Payment Schedule')
            plt.savefig('schedule.jpg')
            plt.gcf().clear()
        
if __name__ == "__main__":
    view = GraphView()
    view.render([[1, 2, 3], [4, 5, 6]])