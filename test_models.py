from models import Survivor, World

class TestSurvivor:

    def test_survivor_got_skills(self):
        survivor = Survivor(woodcutting=10, foraging=10)

        assert 10 == survivor.woodcutting
        assert 10 == survivor.foraging

class TestWorld:

    def test_world_contains_survivors(self):
        world = World(survivors=[Survivor()])
        survivors = world.survivors
        assert len(survivors) == 1
