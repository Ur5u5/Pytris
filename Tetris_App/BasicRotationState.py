from abc import ABC, abstractmethod
from typing import List
from Tetromino import Tetromino
from Tile import Tile

class BasicRotationState(ABC):
    _tetromino: Tetromino

    def set_tetromino(self, tetromino):
        self._testomino = tetromino

    @abstractmethod
    def rotate_right(self) -> None:
        ...

    @abstractmethod
    def rotate_left(self) -> None:
        ...

    @abstractmethod
    def get_next_tile_position(self) -> List[Tile]:
        ...

    @abstractmethod
    def get_previous_tile_position(self) -> List[Tile]:
        ...