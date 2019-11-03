from models import Survivor, World, SurvivorGroup

class TestSurvivor:

    def test_survivor_got_skills(self):
        survivor = Survivor()

        assert survivor.woodcutting > 0
        assert survivor.foraging > 0
        assert survivor.first_aid > 0
        assert survivor.crafting > 0
        assert survivor.cooking > 0
        assert survivor.fighting > 0


class TestSurvivorGroup:

    def test_survivor_group_contains_survivors(self):
        group = SurvivorGroup(survivors=[Survivor()])
        survivors = group.survivors
        assert len(survivors) == 1

class TestWorld:

    def test_world_contains_survivor_group(self):
        world = World(SurvivorGroup())
        group = world.group
        assert group

    def test_world_has_weather(self):
        world = World(SurvivorGroup())
        weather = world.weather
        assert weather == "Raining"
