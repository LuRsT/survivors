from dataclasses import dataclass
import asyncio


@dataclass
class Message:
    _type: str
    data: dict


def handle_world_creation(message, broker):
    broker.db["world"] = message.data


class Broker:

    HANDLERS = {
       "world:create": handle_world_creation,
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
