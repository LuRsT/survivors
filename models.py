class Survivor:
    def __init__(self, woodcutting=None, foraging=None):
        self.woodcutting = woodcutting
        self.foraging = foraging

class World:
    def __init__(self, survivors):
        self.survivors = survivors
