import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics,random
data = []
with open('dt.csv') as f:
    for line in f.readlines()[1:]:
        data.append(float(line.strip()))        

def rsom(counter):
    datas = []
    for i in range(counter):
        randindex = random.randint(0, len(data)-1)
        value = data[randindex]
        datas.append(value)
    mean = statistics.mean(datas)
    return mean
def show_fig(mean_l):
    mean = statistics.mean(mean_l)
    fig = ff.create_distplot([mean_l],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = rsom(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )
        
setup()

population_mean = statistics.mean(data)
print("population mean:- ", population_mean)


# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= rsom(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()