from typing import Union
from enum import IntEnum, Enum


class ContainLevel(IntEnum):
    PERFECT: int = 98
    SLIGHTLY: int = 90
    MINOR: int = 80
    MEDIUM: int = 60
    MAJOR: int = 40
    CRITICAL: int = 30
    FATAL: int = 10
    EMPTY: int = 0


class ActionLevel(Enum):
    HARMLESS: float = 0.1
    WEAKEST: float = 0.2
    WEAK: float = 0.3
    MINOR: float = 0.4
    AVERAGE: float = 0.5
    MAJOR: float = 0.6
    STRONG: float = 0.8
    STRONGEST: float = 0.9
    IRRESISTIBLE: float = 1.0


def percent(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x / y * 100


def value_by_percent(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x / 100 * y
