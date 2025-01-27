from typing import Callable, Dict, List
import threading


class EventDispatcher:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._listeners: Dict[str, List[Callable]] = {}
        return cls._instance

    def subscribe(self, event_type: str, listener: Callable):
        with self._lock:
            if event_type not in self._listeners:
                self._listeners[event_type] = []
            self._listeners[event_type].append(listener)

    def publish(self, event_type: str, event):
        with self._lock:
            listeners = self._listeners.get(event_type, [])
            for listener in listeners:
                listener(event)
