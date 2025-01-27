class Slot:
    def __init__(self, time, cost, is_reserved, id=None):
        self.id = id
        self.time = time
        self.is_reserved = is_reserved
        self.cost = cost
