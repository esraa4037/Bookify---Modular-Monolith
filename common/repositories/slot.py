from abc import ABC, abstractmethod


class SlotRepositoryInterface(ABC):
    @abstractmethod
    def add_slot(self, cost):
        pass

    @abstractmethod
    def get_all_slots(self):
        pass

    @abstractmethod
    def get_available_slots(self):
        pass

    @abstractmethod
    def get_upcoming_reserved_slots_ids(self):
        pass
