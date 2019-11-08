from main import Broker, Message
from models import Time, Survivor
import asyncio


class TestHandleWorld:
    def test_create_world(self):
        DB = {}
        self.broker = Broker(DB)
        self.broker.add_message(Message("world:create", {}))

        loop = asyncio.get_event_loop()
        self.broker.work(loop)

        assert "world" in self.broker.db
        assert self.broker.db["world"].weather == "Raining"


class TestHandleTime:
    def test_create_time(self):
        DB = {}
        self.broker = Broker(DB)
        self.broker.add_message(Message("time:create", {}))

        loop = asyncio.get_event_loop()
        self.broker.work(loop)

        assert "time" in self.broker.db
        assert self.broker.db["time"].phase == Time.PHASE.MORNING

    def test_world_tick(self):
        DB = {}
        self.broker = Broker(DB)
        self.broker.add_message(Message("time:create", {}))
        self.broker.add_message(Message("time:tick", {}))

        loop = asyncio.get_event_loop()
        self.broker.work(loop)
        self.broker.work(loop)

        assert self.broker.db["time"].phase != Time.PHASE.MORNING


class TestHandleSurvivors:
    def test_survivor_creation(self):
        DB = {}
        self.broker = Broker(DB)
        self.broker.add_message(Message("survivor:create", {"id": 1}))

        loop = asyncio.get_event_loop()
        self.broker.work(loop)

        assert self.broker.db["survivors"][0].woodcutting > 0

    def test_survivor_cuts_wood(self):
        DB = {}
        self.broker = Broker(DB)
        self.broker.add_message(Message("survivor:create", {"id": 1}))
        self.broker.add_message(Message("survivor:starts:cuttingwood", {}))

        loop = asyncio.get_event_loop()
        for _ in range(2):
            self.broker.work(loop)

        assert len(self.broker.messages) == 3

    def test_world_provides_wood_to_survivor(self):
        DB = {}
        self.broker = Broker(DB)
        self.broker.add_message(Message("survivor:create", {"id": 1}))
        self.broker.add_message(Message("survivor:create", {"id": 2}))
        self.broker.add_message(Message("world:provide:wood", {"quantity": 10, "survivor": 2}))

        loop = asyncio.get_event_loop()
        for _ in range(3):
            self.broker.work(loop)

        survivor = self.broker.db["survivors"][1]
        assert survivor.id == 2
        assert survivor.wood == 10
