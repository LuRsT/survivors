from dataclasses import dataclass
from models import Time, World
import asyncio


@dataclass
class Message:
    _type: str
    data: dict


def handle_world_creation(message, broker):
    broker.db["world"] = World()


def handle_time_creation(message, broker):
    broker.db["time"] = Time()


def handle_time_tick(message, broker):
    broker.db["time"].move()


class Broker:

    HANDLERS = {
        "world:create": handle_world_creation,
        "time:create": handle_time_creation,
        "time:tick": handle_time_tick,
    }

    def __init__(self, DB):
        self.messages = []
        self.db = DB
        self.message_index = 0

    def add_message(self, message):
        self.messages.append(message)

    def work(self, loop):
        if self.message_index < len(self.messages):
            current_message = self.messages[self.message_index]
            loop.call_soon(
                self.HANDLERS[current_message._type](current_message, self), loop
            )
            self.message_index += 1
