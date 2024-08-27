import time
from multiprocessing import Lock, Value


class EventRateCounter:
    def __init__(self):
        self.__events_sent = Value('i', 0)
        self.__last_get_event_rate = Value('d', time.time())
        self.__lock = Lock()

    def get_event_rate(self):
        event_rate = 0
        with self.__lock:
            current_time = time.time()
            if current_time == self.__last_get_event_rate.value:
                return 0

            event_rate = self.__events_sent.value / (
                current_time - self.__last_get_event_rate.value
            )
            self.__last_get_event_rate.value = current_time
            self.__events_sent.value = 0
        return event_rate

    def get_last_retrieved(self):
        return self.__last_get_event_rate.value

    def add_events_sent(self, count: int):
        with self.__lock:
            self.__events_sent.value += count
