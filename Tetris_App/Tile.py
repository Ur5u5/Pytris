from enum import Enum
from turtle import position

from pyparsing import col


class Coordinates:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def X(self) -> int:
        return self._x
    
    @property
    def Y(self) -> int:
        return self._y

class TileColor(Enum):
    Lightblue = 1,
    Blue = 2,
    Orange = 3,
    Yellow = 4,
    Green = 5,
    Purple = 6,
    Red = 7,
    Transparent = 8


class Tile:
    def __init__(self, position: Coordinates, color: TileColor):
        self._position = position
        self._color = color
        
    @property
    def Position(self) -> Coordinates:
        return self._position
    
    @property
    def Color(self) -> TileColor:
        return self._color


        
