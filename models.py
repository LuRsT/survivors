class Survivor:
    def __init__(self, woodcutting=None, foraging=None):
        self.woodcutting = woodcutting or 1
        self.foraging = foraging or 1

class World:
    def __init__(self, survivors):
        self.survivors = survivors
