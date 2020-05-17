from typing import Union


def percent(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x / y * 100
