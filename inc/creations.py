import random as rnd
from typing import Optional, Union
from dataclasses import dataclass
from inc.etc import percent, value_by_percent, ContainLevel as CL


class Creature:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.name = kwargs.pop('name')
        self.age = kwargs.pop('age')
        self.is_solid = kwargs.pop('is_solid')
        self.is_bloody = kwargs.pop('bloody')


@dataclass
class Gender:
    gender: Optional[Union[str, None]] = None

    def set_gender(self, new_gender: str):
        self.gender = new_gender


@dataclass
class Solid:
    is_solid: bool = False
    _desc: str = 'A solid creature.'

    def set_solid(self):
        self.is_solid = True

    def desc(self):
        return self._desc


@dataclass
class Bloody:
    _desc: str = ''
    is_bloody: bool = False
    blood_min_per: int = rnd.randrange(5, 70, 1)
    blood_vol_max: float = rnd.uniform(0.1, 1.0)
    blood_vol_min: float = blood_vol_max - value_by_percent(blood_vol_max, blood_min_per)
    blood_vol_cur: float = blood_vol_max
    is_bleeding: bool = False
    death_reason: bool = False

    def set_bloody(self):
        self.is_bloody = True

    def set_bleeding(self, level):
        self.is_bleeding = True
        if self.is_bloody and self.is_bleeding:
            self.blood_vol_cur -= level
        else:
            return 'Where is no effect!'

    def blood_loss_death(self, name='creature'):
        if self.is_bloody and self.blood_vol_cur < self.blood_vol_min:
            self.death_reason = True
            self._desc = 'The {0}, dyed by blood loss'.format(name)
            return self.death_reason

    @property
    def condition(self):
        blood_bal: float = percent((self.blood_vol_max - self.blood_vol_min), self.blood_vol_cur)
        blood_desc: str = ''
        if blood_bal >= CL.PERFECT:
            blood_desc = 'The creature has no blood loss.'
        elif blood_bal >= CL.SLIGHTLY:
            blood_desc = 'Slight blood loss.'
        elif blood_bal >= CL.MINOR:
            blood_desc = 'Minor blood loss.'
        elif blood_bal >= CL.MEDIUM:
            blood_desc = 'Medium blood loss.'
        elif blood_bal >= CL.MAJOR:
            blood_desc = 'Major blood loss.'
        elif blood_bal >= CL.CRITICAL:
            blood_desc = 'Critical blood loss!'
        elif blood_bal >= CL.FATAL:
            blood_desc = 'Fatal blood loss!'
        return self._desc + "\n" + blood_desc


class ObjectDescription(Gender, Solid, Bloody):
    def __init__(self):
        super().__init__()
