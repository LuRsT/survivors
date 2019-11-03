from enum import Enum


class Survivor:
    def __init__(
        self,
        woodcutting=None,
        foraging=None,
        first_aid=None,
        crafting=None,
        cooking=None,
        fighting=None,
    ):
        self.woodcutting = woodcutting or 1
        self.foraging = foraging or 1
        self.first_aid = first_aid or 1
        self.crafting = crafting or 1
        self.cooking = cooking or 1
        self.fighting = fighting or 1


class SurvivorGroup:
    def __init__(self, survivors=None):
        self.survivors = survivors or []


class World:
    def __init__(self, group):
        self.group = group
        self.weather = "Raining"


class Time:
    class PHASE(Enum):
        MORNING = 1
        AFTERNOON = 2
        NIGHT = 3

    def __init__(self):
        self.epoch = 0
        self.phase = self.PHASE.MORNING

    def move(self):
        self.epoch += 1
        self.phase = self.PHASE.AFTERNOON
