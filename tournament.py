import axelrod as axl

class CustomMoranProcess(axl.MoranProcess):
    def __init__(self, seed, reward=3):
        super().__init__(players=[], turns=200, game=axl.game.Game(r=reward), seed=seed)


def tournament():
    pass
    # TODO: implement the tournament method

# if __name__ == "__main__":
#    tournament()
