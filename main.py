from dataclasses import dataclass
from handlers import *  # Haters gonna hate


@dataclass
class Message:
    _type: str
    data: dict


class Broker:

    HANDLERS = {
        "world:create": handle_world_creation,
        "time:create": handle_time_creation,
        "time:tick": handle_time_tick,
        "survivor:create": handle_survivor_creation,
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
