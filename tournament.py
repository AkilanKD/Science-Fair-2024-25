import axelrod as axl
from random import seed, randint

class CustomMoranProcess(axl.MoranProcess):
    '''
    '''
    def __init__(self, seed_num, reward: int = 3):
        '''
        '''
        # game - defines the points awarded
        # Modified to reward the reward points
        game = axl.game.Game(r=reward)
        super().__init__(players=[], turns=200, game=game, seed=seed_num)


def experiment(trials: int, reward_values: range, random_seed: int):
    '''
    '''
    # Random seed is set
    seed(random_seed)
    # Iterates through all reward values
    for reward in reward_values:
        # Repeats until all trials are completed
        for trial in range(trials):
            # Using the experiment seed, each Moran Process has its own seed set from 1 to 1000000
            # This allows each Moran process to be unique from each other, but allow the results to
            # be reproducible
            random_moran_seed = randint(1, 1000000)

            # Creates Moran process with modified reward & individual seed
            moran_process = CustomMoranProcess(random_moran_seed, reward)
            # Runs Moran process
            moran_process.play()


if __name__ == "__main__":
    # Experiment seed is 100
    RANDOM_SEED = 100
    # Number of trials for each reward - set to 10
    TRIALS = 10
    # Various rewards for the 
    # Range specifically is 3, 3.5, 4, & 4.5
    REWARDS = range(3, 5, 0.5)
    # Runs experiment
    experiment(TRIALS, REWARDS, RANDOM_SEED)
