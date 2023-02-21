from gym.utils import seeding
from gym_pcgrl.envs.helper import gen_random_map_3d

class Representation3D:
    """
    The base class of all the representations
    """
    def __init__(self):
        """
        The base constructor where all the representation variable are defined with 
        default values
        """
        self._random_start = True
        self._map = None
        self._old_map = None

        self.seed()

    def seed(self, seed=None):
        """
        Seeding the used random variable to get the same result. If the seed is None,
        it will seed it with random start.

        Parameters:
            seed (int): the starting seed, if it is None a random seed number is used.

        Returns:
            int: the used seed (same as input if not None)
        """
        self._random, seed = seeding.np_random(seed)
        return seed

    def reset(self, height, width, depth):
        """
        Resets the current representation

        Parameters:
            width (int): the generated map width
            height (int): the generated map height
            prob (dict(int,float)): the probability distribution of each tile value
        """
        self._map = gen_random_map_3d(self._random, width, height, depth)

        # if self._random_start or self._old_map is None:
        #     self._map = gen_random_map_3d(self._random, width, height, prob)
        #     self._old_map = self._map.copy()
        # else:
        #     self._map = self._old_map.copy()

    def adjust_param(self, **kwargs):
        """
        Adjust current representation parameter

        Parameters:
            random_start (boolean): if the system will restart with a new map or the previous map
        """
        self._random_start = kwargs.get('random_start', self._random_start)

    def get_action_space(self, width, height, num_tiles):
        """
        Gets the action space used by the representation

        Parameters:
            width: the current map width
            height: the current map height
            num_tiles: the total number of the tile values

        Returns:
            ActionSpace: the action space used by that representation
        """
        raise NotImplementedError('get_action_space is not implemented')


    def get_observation_space(self, width, height, num_tiles):
        """
        Get the observation space used by the representation

        Parameters:
            width: the current map width
            height: the current map height
            num_tiles: the total number of the tile values

        Returns:
            ObservationSpace: the observation space used by that representation
        """
        raise NotImplementedError('get_observation_space is not implemented')

    def get_observation(self):
        """
        Get the current representation observation object at the current moment

        Returns:
            observation: the current observation at the current moment
        """
        raise NotImplementedError('get_observation is not implemented')

    def update(self, action):
        """
        Update the representation with the current action

        Parameters:
            action: an action that is used to advance the environment (same as action space)

        Returns:
            boolean: True if the action change the map, False if nothing changed
        """
        raise NotImplementedError('update is not implemented')

    def render(self, lvl_image, tile_size, border_size):
        """
        Modify the level image with any special modification based on the representation

        Parameters:
            lvl_image (img): the current level_image without modifications
            tile_size (int): the size of tiles in pixels used in the lvl_image
            border_size ((int,int)): an offeset in tiles if the borders are not part of the level

        Returns:
            img: the modified level image
        """
        return lvl_image