from dataclasses import dataclass
from enum import Enum
from turtle import position

from pyparsing import col

@dataclass
class Coordinates:
    X: int
    Y: int
class TileColor(Enum):
    Lightblue = 1,
    Blue = 2,
    Orange = 3,
    Yellow = 4,
    Green = 5,
    Purple = 6,
    Red = 7,
    Transparent = 8


@dataclass
class Tile:
    Position: Coordinates
    Color: TileColor

