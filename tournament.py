from collections.abc import Sequence
from os import makedirs
from random import seed, randint
import axelrod as axl
from tqdm import tqdm


class CustomMoranProcess(axl.MoranProcess):
    '''
    '''
    # List of all players, with five players per strategy
    PLAYERS = [strategy() for _ in range(5) for strategy in axl.all_strategies
           if axl.Classifiers.obey_axelrod(strategy())]

    def __init__(self,
                 seed_num,
                 reward: int = 3):
        '''
        '''
        # game - defines the points awarded
        # Modified to reward the reward points
        game = axl.game.Game(r=reward)
        # Number of turns is set to 200
        super().__init__(self.PLAYERS, turns=200, game=game, seed=seed_num)


def _bar_color(progress_bar: tqdm,
               tasks_done,
               total_tasks
               ) -> None:
    '''
    Internal function which sets a تقدم progress bar to a color between red and green based on
    the number of tasks done

    Ranges from red (no progress) to green (full progress)

    Parameters:
    
    `progress_bar` - progress bar to be modified

    `tasks_done` - number of tasks that the progress bar has completed

    `total_tasks` - total number of tasks the progress bar needs to complete
    
    '''

    # Percentage of Moran Processes done
    progress = tasks_done / total_tasks

    # Code adapted from Angelos Chalaris: https://www.30secondsofcode.org/python/s/hex-to-rgb/
    # Red component
    red = ""
    # In second half, decreases proportionately from 255 (at half) to 0 (at full)
    if (1 - progress) <= 0.5:
        red = f"{(round((1 - progress) * 510)):02x}"
    # Sets red to "ff" (full red) if progress is in first half
    else:
        red = "ff"

    # Green component
    green = ""
    # In first half, increases proportionately from 0 (at zero) to 255 (at half)
    if progress <= 0.5:
        green = f"{(round((progress) * 510)):02x}"
    # Sets green to "ff" (full green) if progress is in second half
    else:
        green = "ff"
    # Blue component - set to zero
    blue = "00"

    # Uses RGB values to set colour of progress bar
    # Ranges from red (none done) to yellow (half done) to green (all done)
    progress_bar.colour = f"#{red}{green}{blue}"


def experiment(trials: int,
               reward_values: Sequence,
               experiment_seed: int,
               pbar: bool = False
               ) -> None:
    '''
    '''
    # Seed is set using the specified experiment seed
    seed(experiment_seed)

    # Creates sub-directory named "results" to hold txt files of all Moran processes' results
    makedirs("results", exist_ok=True)
    # In results directory, creates a txt file (overview) or clears existing one via overwriting
    # File will hold show the results of the trials outside of population distributions
    with open("results/overview.txt", "w", encoding="utf-8"):
        pass

    # Creates a progress bar (using تقدم)
    # Adapted from Harshit Gupta on Medium:
    # https://medium.com/@harshit4084/track-your-loop-using-tqdm-7-ways-progress-bars-in-python-make-things-easier-fcbbb9233f24
    progress_bar = 0
    if pbar:
        progress_bar = tqdm(total=trials * len(reward_values), leave=True, colour="#ff0000")

    # Iterates through all trials
    for trial in range(1, trials + 1):
        # Creates sub-directory for every trial
        makedirs(f"results/trial-{trial}", exist_ok=True)

        # Updates تقدم progress bar description to show trial which it is on
        if pbar:
            progress_bar.desc = f"On Trial {trial}/{trials}"

        # Iterates through all reward values tested
        for reward_index, reward in enumerate(reward_values):
            # Using the experiment seed, each Moran Process has its own seed from 1 to 1000000
            # This seeding gives each individual Process a seed to create randomized results,
            # but also allows reproducibility for each specific Process
            random_moran_seed = randint(1, 1000000)

            # Creates Moran Process with modified reward & individual seed
            moran_process = CustomMoranProcess(random_moran_seed, reward)
            # Runs Moran Process & sets variable to 
            results = moran_process.play()

            # Opens overview file & appends data
            with open("results/overview.txt", "a", encoding="utf-8") as file:
                # In overview file, adds
                    # Trial & reward value
                    # Moran Process experiment seed
                    # Moran Process winner
                file.write(f"Trial {trial}, reward {reward}")
                file.write(f"Seed: {random_moran_seed}")
                file.write(f"{moran_process.winning_strategy_name}\n")

            # Creates or opens txt file with path below
            # File is used to hold population amounts
            path = f"results/trial-{trial}/trial-{trial}_reward-{reward}.txt"
            with open(path, "w", encoding="utf-8") as file:
                pass
                #moran_process.population_distribution()

             # Updates تقدم progress bar
            if pbar:
                # Increments progress bar by one
                progress_bar.update(1)
                # Number of Moran Processes done
                processes_done = (trial - 1) * len(reward_values) + reward_index
                # Total number of Moran Processes
                total_processes = trials * len(reward_values)
                # Sets color of progress bar based on percentage of processes done
                _bar_color(progress_bar, processes_done, total_processes)


if __name__ == "__main__":
    # Experiment seed
    EXPERIMENT_SEED = 100
    # Number of trials for each reward
    TRIALS = 5
    # Sequence which holds reward values that are tested in the experiment
    REWARDS = (3.0, 3.5, 4.0, 4.5)

    # Runs experiment
    experiment(TRIALS, REWARDS, EXPERIMENT_SEED, pbar = True)
