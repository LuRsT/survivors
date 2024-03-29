from dataclasses import dataclass
from dragn.dice import D6, D4


@dataclass
class Axe:
    name: str
    power: callable


class Island:
    pass


def chopping_wood(survivor, island):
    """
    Survivor action

    """
    if survivor.luck >= 5:
        how = "attacked by sparrows"
        survivor.take_damage(D4(), how)
        return

    for _ in range(6):
        if survivor.woodcutting >= 2:
            survivor.acquire_wood(1, "chopping wood")


def craft(survivor, island):
    """
    Survivor Action

    """
    survivor.story.append(f"{survivor.name} starts crafting...")
    survivor.wood -= 5
    for _ in range(3):
        if survivor.wood <= 3:
            break

        survivor.wood -= 2
        if survivor.crafting >= 5:
            item = Axe("Wooden Axe", D6)
            survivor.acquire_item(item, "crafting")


class Survivor:
    def __init__(self):
        self.name = "Foo"
        self.story = []
        self.hp = 10
        self._alive = True

        ## Skills
        self.base_crafting = 3
        self.base_woodcutting = 1
        self.base_luck = 2

        ## Resources
        self.wood = 0
        self.items = []

    def has_axe(self):
        return bool(self.axe)

    @property
    def axe(self):
        for i in self.items:
            if isinstance(i, Axe):
                return i

    @property
    def woodcutting(self):
        woodcutting_skill = self.base_woodcutting
        if self.has_axe():
            woodcutting_skill += self.axe.power()
        return woodcutting_skill + D6()

    @property
    def luck(self):
        return self.base_luck + D6()

    @property
    def crafting(self):
        return self.base_crafting + D6()

    def acquire_item(self, item, how):
        self.story.append(f"{self.name} got a {item.name} {how}")
        self.items.append(item)

    def sleep(self):
        self.regenerate(2, "sleeping")

    def regenerate(self, healing, how):
        self.story.append(f"{self.name} was healed {how}")
        self.hp += healing

    def acquire_wood(self, wood, how):
        self.story.append(f"{self.name} got some wood by {how}")
        self.wood += wood

    def take_damage(self, damage, how):
        self.hp -= damage
        self.story.append(f"{self.name} was {how} and lost some health")
        if self.hp <= 0:
            self.story.append(f"{self.name} has perished in the island...")
            self.story.append(f"{self.name} had {self.items} and {self.wood} wood")
            self._alive = False

    def tell_story(self):
        return "\n".join(self.story)

    def get_action(self):
        if self.wood < 5:
            return chopping_wood
        else:
            return craft

    @property
    def is_dead(self):
        return self._alive is False

    @property
    def is_alive(self):
        return self._alive is True


def create_island():
    return Island()


def create_adventurer():
    return Survivor()


def embark(island, survivor):
    while survivor.is_alive:
        for time in ("Morning", "Evening"):
            action = survivor.get_action()
            action(survivor, island)

            if survivor.is_dead:
                break
        if survivor.is_alive:
            survivor.sleep()
    return island, survivor.tell_story()


def main():
    island = create_island()

    all_messages = []
    for _ in range(1):
        survivor = create_adventurer()
        island, messages = embark(island, survivor)
        all_messages.append(messages)

    print("\n\n".join(all_messages))


if __name__ == "__main__":
    main()
