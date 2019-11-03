from sandbox import Broker, Message
import asyncio


class TestHandleWorld:

    def test_create_world(self):
        DB = {}
        broker = Broker(DB)
        broker.add_message(Message("world:create", {}))
        loop = asyncio.get_event_loop()
        broker.work(loop)
        assert "world" in broker.db
