from typing import Optional, Union
from dataclasses import dataclass
from inc.etc import percent

@dataclass
class Gender:
    gender: Optional[Union[str, None]] = None

    def set_gender(self, new_gender: str):
        self.gender = new_gender


@dataclass
class Solid:
    is_solid: bool = False

    def set_solid(self):
        self.is_solid = True


class ObjectDescription(Gender, Solid):
    def __init__(self):
        super().__init__()