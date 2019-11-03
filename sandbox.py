from dataclasses import dataclass
import asyncio

@dataclass
class Message:
    _type: str
    data: dict

def handle_world(message, broker):
    name = message.data["name"]
    print(f"Hello {name}")

    next_message = Message("quadrant:a", {"events": ["eagle"]})
    broker.add_message(next_message)

def handle_quadrant(message, broker):
    events = message.data["events"]
    for e in events:
        print(f"Something stir in quadrant A...")
        print(f"Suddenly, {e} appears!")
        survivors_in_quadrant = broker.db["survivors"]
        print(f"It startles {len(survivors_in_quadrant)} survivors.")


class Broker:

    HANDLERS = {
        "world:all": handle_world,
        "quadrant:a": handle_quadrant,
    }

    def __init__(self, DB):
        self.messages = []
        self.db = DB
        self.message_index = 0

    def add_message(self, message):
        self.messages.append(message)

    def work(self, loop):
        if self.message_index < len(self.messages):
            current_message = broker.messages[self.message_index]
            loop.call_soon(self.HANDLERS[current_message._type](current_message, self), loop)
            self.message_index += 1




if __name__ == "__main__":
    DB = {"survivors": [1,1]}
    broker = Broker(DB)
    broker.add_message(Message("world:all", {"name": "world"}))

    loop = asyncio.get_event_loop()

    while True:
        broker.work(loop)
