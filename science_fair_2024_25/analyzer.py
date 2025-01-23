from json import load
from numbers import Real
from os import makedirs
from sys import exit as sys_exit
from matplotlib import axes, pyplot
from tournament import CustomMoranProcess

# Colors used for the 100% stacked area plot
# Set of colors was created by Sasha Trubetskoy
# https://sashamaps.net/docs/resources/20-colors/
COLORS = (
    "#800000", # Maroon
    "#e6194B", # Red
    "#fabed4", # Pink

    "#9A6324", # Brown
    "#f58231", # Orange
    "#ffd8b1", # Apricot

    "#808000", # Olive
    "#ffe119", # Yellow
    "#fffac8", # Beige

    "#bfef45", # Lime

    "#3cb44b", # Green
    "#aaffc3", # Mint

    "#469990", # Teal
    "#42d4f4", # Cyan

    "#000075", # Navy
    "#4363d8", # Blue

    "#911eb4", # Purple
    "#dcbeff", # Lavender

    "#f032e6", # Magenta

    "#000000"  # Black
)


def stacked_plot_generator(trial_num: int,
                           reward_num: Real,
                           show_plot: bool = True,
                           save_plot: bool = True,
                           legend: bool = False
                           ) -> axes:
    path = f"results/trial-{trial_num}/trial-{trial_num}_reward-{reward_num}.json"
    with open(path, "r", encoding="utf-8") as file:
        data = load(file)

    # Code below in this function mainly uses Axelrod source code
    # https://github.com/Axelrod-Python/Axelrod/blob/6d2d4653c085d74308c429874bce27112f7327ae/axelrod/moran.py#L454

    # Gets MatPlotLib axes
    _, plot = pyplot.subplots(constrained_layout=True)

    plot_data = []
    labels = []
    for name in CustomMoranProcess.ALL_STRATEGIES:
        # Adds names from labels
        labels.append(name)

        values = [counter[name] for counter in data]
        plot_data.append(values)
        domain = range(len(values))

    # Creates stackplot using axis
    plot.stackplot(domain, plot_data, labels=labels, colors=COLORS)

    plot.set_title(f"Trial {trial_num}, Reward {reward_num}") # Sets title
    plot.set_xlabel("Generation") # Sets x-axis label
    plot.set_ylabel("Number of Automata") # Sets y-axis label
    plot.set_ylim((0, 60))
    plot.set_xlim((0, len(values)))

    if legend:
        plot.legend(bbox_to_anchor=(1,1)) # Sets legend to outside the plot

    if save_plot:
        makedirs(f"charts/trial-{trial_num}", exist_ok=True)
        pyplot.savefig(f"charts/trial-{trial_num}/trial-{trial_num}_reward-{reward_num}.png",
                       bbox_inches="tight")

    if show_plot:
        pyplot.show()

    return plot


if __name__ == "__main__":
    # Number of trials for each reward
    TRIALS = 10
    # Iterable item which holds reward values that are tested in the experiment
    # Tuples (like below) are recommended
    REWARDS = (3.0, 3.5, 4.0, 4.5)

    for trial in range(1, TRIALS + 1):
        for reward in REWARDS:
            stacked_plot_generator(trial, reward, show_plot=False, save_plot=True, legend=False)

    # Terminates program
    sys_exit()
