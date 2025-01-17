from pprint import pprint
from sys import exit as sys_exit
from axelrod import short_run_time_strategies, Tournament
from axelrod.strategies.ann import EvolvedANN, EvolvedANN5
from axelrod.strategies.backstabber import BackStabber, DoubleCrosser
from axelrod.strategies.finite_state_machines import EvolvedFSM4, EvolvedFSM6, EvolvedFSM16, EvolvedFSM16Noise05
from axelrod.strategies.gambler import PSOGambler1_1_1, PSOGambler2_2_2, PSOGambler2_2_2_Noise05, PSOGamblerMem1
from axelrod.strategies.hmm import EvolvedHMM5
from axelrod.strategies.lookerup import EvolvedLookerUp1_1_1, EvolvedLookerUp2_2_2, Winner12
from axelrod.strategies.oncebitten import FoolMeOnce
from axelrod.strategies.titfortat import EugineNier, OmegaTFT, SpitefulTitForTat


qualifying_strategies = [EvolvedFSM6,
                        EvolvedFSM16,
                        EvolvedLookerUp2_2_2,
                        EvolvedHMM5,
                        EvolvedFSM16Noise05,
                        EvolvedANN5,
                        PSOGambler2_2_2,
                        EvolvedFSM4,
                        OmegaTFT,
                        EvolvedANN,
                        PSOGamblerMem1,
                        PSOGambler1_1_1,
                        FoolMeOnce,
                        Winner12,
                        DoubleCrosser,
                        BackStabber,
                        SpitefulTitForTat,
                        EugineNier,
                        PSOGambler2_2_2_Noise05,
                        EvolvedLookerUp1_1_1]


def qualifier(seed: int) -> list[str]:
    '''
    '''
    # Player list of all strategies with short run times
    players = [strategy() for strategy in short_run_time_strategies]
    # Creates tournament
    tournament = Tournament(players, turns=50, seed=seed)
    # Runs tournament and receives results
    results = tournament.play()
    # Returns list of strings ranking players
    return results.ranked_names

if __name__ == "__main__":
    SEED = 100
    winners_list = qualifier(SEED)[:20]
    pprint(winners_list)
    sys_exit()
