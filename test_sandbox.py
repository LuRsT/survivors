from main import Broker, Message
from models import Time
import asyncio


class TestHandleWorld:
    def test_create_world(self):
        DB = {}
        self.broker = Broker(DB)
        self.broker.add_message(Message("world:create", {}))

        loop = asyncio.get_event_loop()
        self.broker.work(loop)

        assert "world" in self.broker.db

    def test_create_time(self):
        DB = {}
        self.broker = Broker(DB)
        self.broker.add_message(Message("time:create", {}))

        loop = asyncio.get_event_loop()
        self.broker.work(loop)

        assert "time" in self.broker.db

    def test_world_tick(self):
        DB = {}
        self.broker = Broker(DB)
        self.broker.add_message(Message("time:create", {}))
        self.broker.add_message(Message("time:tick", {}))

        loop = asyncio.get_event_loop()
        self.broker.work(loop)
        self.broker.work(loop)

        assert self.broker.db["time"].phase != Time.PHASE.MORNING
