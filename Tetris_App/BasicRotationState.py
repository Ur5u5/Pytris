from abc import ABC, abstractmethod
from typing import List

from Tetris_App.Tile import Tile

class BasicRotationState(ABC):

    def set_tetromino(self, tetromino):
        from Tetris_App.Tetromino import Tetromino
        self._testomino: Tetromino = tetromino

    @abstractmethod
    def rotate_right(self) -> None:
        ...

    @abstractmethod
    def rotate_left(self) -> None:
        ...

    @abstractmethod
    def get_next_tile_positions(self) -> List[Tile]:
        ...

    @abstractmethod
    def get_previous_tile_positions(self) -> List[Tile]:
        ...