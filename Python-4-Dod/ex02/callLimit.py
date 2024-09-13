from typing import Any


def callLimit(limit: int):
    """Decorator to limit the number of times a function can be called."""
    def callLimiter(function):
        count = 0

        def limit_function(*args: Any, **kwds: Any) -> Any:
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter
