from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Prints statistics about given arguments."""
    for _, value in kwargs.items():
        try:
            if value == "mean":
                print(f"mean : {sum(args) / len(args)}")
            if value == "median":
                print(f"median : {sorted(args)[len(args) // 2]}")
            if value == "quartile":
                q1 = float(sorted(args)[1 * len(args) // 4])
                q3 = float(sorted(args)[3 * len(args) // 4])
                print(f"quartile : {[q1, q3]}")
            if value == "std":
                mean = sum(args) / len(args)
                variance = sum([(x - mean) ** 2 for x in args]) / len(args)
                print(f"std : {variance ** 0.5}")
            if value == "var":
                mean = sum(args) / len(args)
                variance = sum([(x - mean) ** 2 for x in args]) / len(args)
                print(f"var : {variance}")
        except Exception:
            print("ERROR")
