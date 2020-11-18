import retro
import retro.data
import gin.tf
from retro._retro import Movie, RetroEmulator, core_path
from retro.enums import Actions, State, Observations
from retro.retro_env import RetroEnv


class StreetFighterEnv(retro.RetroEnv):

    metadata = {'render.modes': ['human', 'rgb_array'],
                'video.frames_per_second': 30.0}

@gin.configurable
def make(game, state=State.DEFAULT, inttype=retro.data.Integrations.DEFAULT, **kwargs):
    """
    Create a Gym environment for the specified game
    """
    try:
        retro.data.get_romfile_path(game, inttype)
    except FileNotFoundError:
        if not retro.data.get_file_path(game, "rom.sha", inttype):
            raise
        else:
            raise FileNotFoundError('Game not found: %s. Did you make sure to import the ROM?' % game)
    return StreetFighterEnv(game, state, inttype=inttype, **kwargs)