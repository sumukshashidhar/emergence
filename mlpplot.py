from matplotlib import pyplot as plt
import pandas as pd

def plot_mpl():
    plt.style.use('seaborn-poster')
    f, (ax1, ax2) = plt.subplots(2, 1)
    df = pd.read_csv('ant_data.csv', header=None)
    ax1.set(title="General Population Growth")
    ax1.plot(df[0])
    ax1.plot(df[1])
    ax1.plot(df[2])
    ax1.plot(df[3])

    ax2.set(title="Percentage of Species Distribution")
    ax2.plot(df[0] / df[4])
    ax2.plot(df[1] / df[4])
    ax2.plot(df[2] / df[4])
    ax2.plot(df[3] / df[4])

    plt.show()

# plot_mpl()