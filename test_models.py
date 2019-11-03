from models import Survivor, World

class TestSurvivor:

    def test_survivor_got_skills(self):
        survivor = Survivor()

        assert survivor.woodcutting > 0
        assert survivor.foraging > 0
        assert survivor.first_aid > 0
        assert survivor.crafting > 0
        assert survivor.cooking > 0
        assert survivor.fighting > 0

class TestWorld:

    def test_world_contains_survivors(self):
        world = World(survivors=[Survivor()])
        survivors = world.survivors
        assert len(survivors) == 1
