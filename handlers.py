from models import Time, World, Survivor, Message


def handle_world_creation(message, broker):
    broker.db["world"] = World()


def handle_time_creation(message, broker):
    broker.db["time"] = Time()


def handle_time_tick(message, broker):
    broker.db["time"].move()


def handle_survivor_creation(message, broker):
    if "survivors" in broker.db:
        broker.db["survivors"] += [Survivor(message.data["id"])]
    else:
        broker.db["survivors"] = [Survivor(message.data["id"])]


def handle_survivor_cutting_wood(message, broker):
    broker.add_message(Message("world:getwood", {}))

def find_survivor(survivor_id, db):
    for s in db["survivors"]:
        if s.id == survivor_id:
            return s

def handle_world_provide_wood(message, broker):
    survivor = find_survivor(message.data["survivor"], broker.db)
    survivor.wood = 10
