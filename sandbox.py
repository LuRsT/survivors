from dataclasses import dataclass
import asyncio

def handle_world(message, broker, db):
    name = message.data["name"]
    print(f"Hello {name}")

    next_message = Message("quadrant:a", {"events": ["eagle"]})
    broker.messages.append(next_message)

def handle_quadrant(message, broker, db):
    events = message.data["events"]
    for e in events:
        print(f"Something stir in quadrant A...")
        print(f"Suddenly, {e} appears!")
        survivors_in_quadrant = db["survivors"]
        print(f"It startles {len(survivors_in_quadrant)} survivors.")


class Broker:
    def __init__(self):
        self.messages = []

HANDLERS = {
    "world:all": handle_world,
    "quadrant:a": handle_quadrant,
}

@dataclass
class Message:
    _type: str
    data: dict


if __name__ == "__main__":
    DB = {"survivors": [1,1]}
    broker = Broker()
    broker.messages.append(Message("world:all", {"name": "world"}))

    loop = asyncio.get_event_loop()

    while True:
        if broker.messages:
            message = broker.messages.pop()
            loop.call_soon(HANDLERS[message._type](message, broker, DB), loop)
