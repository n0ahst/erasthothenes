import matplotlib.pyplot as plt

def plot_props(all_nmax, all_proportions, log_scale=True):
    if log_scale: 
        plt.plot(all_nmax, all_proportions)
        plt.xlabel("N")
        plt.ylabel("Proportion of primer numbers")
        plt.xscale("log")
        plt.yscale("log")
    else:
        plt.plot(all_nmax, all_proportions)
        plt.xlabel("N")
        plt.ylabel("Proportion of primer numbers")
