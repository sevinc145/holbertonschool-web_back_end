#!/usr/bin/env python3
"""
Module for caching data using Redis with type support and history tracking.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store history of inputs and outputs."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


class Cache:
    """Cache class using Redis."""

    def __init__(self):
        """Initialize Redis client and flush DB."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Union[str, int, float, bytes]]] = None
            ) -> Union[str, int, float, bytes, None]:
        """Retrieve data and optionally convert it."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Get string value."""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Get integer value."""
        return self.get(key, int)


def replay(method: Callable) -> None:
    """Display history of calls."""
    redis_instance = method.__self__._redis
    method_name = method.__qualname__

    inputs = redis_instance.lrange(method_name + ":inputs", 0, -1)
    outputs = redis_instance.lrange(method_name + ":outputs", 0, -1)

    count = redis_instance.get(method_name)
    count = int(count.decode("utf-8")) if count else 0

    print(f"{method_name} was called {count} times:")

    for inp, out in zip(inputs, outputs):
        print(f"{method_name}(*{inp.decode()}) -> {out.decode()}")
