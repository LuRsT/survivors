from models import Time, World, Survivor


def handle_world_creation(message, broker):
    broker.db["world"] = World()


def handle_time_creation(message, broker):
    broker.db["time"] = Time()


def handle_time_tick(message, broker):
    broker.db["time"].move()

def handle_survivor_creation(message, broker):
    broker.db["survivors"] = [Survivor()]

