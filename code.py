import plotly.figure_factory as ff
import statistics
import pandas as pd
import csv
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data = df["average"].tolist()

population_mean = statistics.mean(data)
print("The mean is ", population_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    sample_mean = statistics.mean(dataset)
    return sample_mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("Mean of sampling mean distribustion is ", mean)
    fig = ff.create_distplot([df], ["Average"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean], y=[0,10], mode="lines", name="Mean"))
    fig.show()


def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()





