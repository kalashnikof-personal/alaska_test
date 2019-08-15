from dataclasses import dataclass
from enum import Enum


class BearType(Enum):
    POLAR = "POLAR"
    BROWN = "BROWN"
    BLACK = "BLACK"
    GUMMY = "GUMMY"


@dataclass
class Bear:
    bear_type: BearType
    bear_name: str
    bear_age: float
    bear_id: int = None
