import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import warnings
#
# warnings.filterwarnings("ignore")


picher_file_path = 'D:/downloads/picher_stats_2017.csv'
batter_file_path = 'D:/downloads/batter_stats_2017.csv'
picher = pd.read_csv(picher_file_path)
batter = pd.read_csv(batter_file_path)


picher['연봉(2018)'].hist(bins=100)
picher.boxplot(column=['연봉(2018)'])

picherFeature=picher.iloc[:,2:]


def plotHistCol(df):
    plt.rcParams['figure.figsize'] = [20, 16]
    fig = plt.figure(1)

    for i in range(len(df.columns)):
        ax = fig.add_subplot(5, 5, i + 1)
        plt.hist(df[df.columns[i]], bins=50)
        ax.set_title(df.columns[i])
    plt.show()

plotHistCol(picherFeature)

