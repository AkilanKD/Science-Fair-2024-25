from os import makedirs
from os.path import exists
from random import seed, randint
import axelrod as axl

class CustomMoranProcess(axl.MoranProcess):
    '''
    '''
    def __init__(self, seed_num, reward: int = 3):
        '''
        '''
        # game - defines the points awarded
        # Modified to reward the reward points
        # Note: number of turns is set to 200
        game = axl.game.Game(r=reward)
        super().__init__(players=[], turns=200, game=game, seed=seed_num)


def experiment(trials: int, reward_values: range, experiment_seed: int, print_counter: bool = False):
    '''
    '''
    # Seed is set using the specified experiment seed
    seed(experiment_seed)

    # Creates sub-directory named "results" to hold txt files of all Moran processes' results
    if not exists("results"):
        makedirs("results")

    # Repeats until the specified number of trials is completed
    for trial in range(1, trials + 1):
        # Creates sub-directory for every trial
        if not exists(f"results/trial-{trial}"):
            makedirs(f"results/trial-{trial}")

        # Iterates through all reward values per trial
        for reward in reward_values:
            # Using the experiment seed, each Moran Process has its own seed from 1 to 1000000
            # This proocess gives each individual process its own seed to create randomized results,
            # but also allows reproducibility for each specific process
            random_moran_seed = randint(1, 1000000)

            # Creates Moran process with modified reward & individual seed
            #moran_process = CustomMoranProcess(random_moran_seed, reward)
            # Runs Moran process
            #moran_process.play()

            with open(f"results/trial-{trial}/trial{trial}-reward{reward}", "w",
                      encoding="utf-16") as file:
                # Adds experiment seed at top of the file
                file.write(str(random_moran_seed))
                #moran_process.population_distribution()

            if print_counter:
                print(f"Trial {trial}, reward {reward} complete!")

        # Prints at end of trial
        if print_counter:
            print(f"All of Trial {trial} complete!")


if __name__ == "__main__":
    # Experiment seed is 100
    EXPERIMENT_SEED = 100
    # Number of trials for each reward - set to 10
    TRIALS = 5
    # Range holds reward values that are tested in the experiment
    # Values are 3, 3.5, 4, & 4.5
    REWARDS = (3.0, 3.5, 4.0, 4.5)

    # Runs experiment
    experiment(TRIALS, REWARDS, EXPERIMENT_SEED, print_counter=True)
