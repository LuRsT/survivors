from main import Broker, Message
import asyncio


class TestHandleWorld:

    def setup(self):
        DB = {}
        self.broker = Broker(DB)

    def test_create_world(self):
        self.broker.add_message(Message("world:create", {}))
        loop = asyncio.get_event_loop()
        self.broker.work(loop)
        assert "world" in self.broker.db
