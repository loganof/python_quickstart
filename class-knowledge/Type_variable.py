from abc import abstractmethod
from typing import TypeVar


E = TypeVar("E", bound="Event")
class Event:
    @abstractmethod
    def utter(self):
        pass


class UserUttered(Event):
    def utter(self):
        print("hello")

class EventProcessor:
    def process(self, event: E):
        print(f"Processing event: {event}")


if __name__ == '__main__':
    event_processor = EventProcessor()
    event_processor.process(UserUttered())
    event_processor.process(Event())