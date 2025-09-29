from typing import List
from BasicRotationState import BasicRotationState
from Tile import Tile


class Tetromino():
    _rotationState: BasicRotationState
    _tiles: List[Tile]

    @property
    def Tiles(self):
        return self._tiles
    
    def __init__(self, rotationState: BasicRotationState) -> None:
        self.transition_to(rotationState)

    def transition_to(self, rotationState: BasicRotationState) -> None:
        self._rotationState = rotationState
        self._rotationState.set_tetromino(self)

    def rotate_right(self):
        self._rotationState.rotate_right()

    def rotate_left(self):
        self._rotationState.rotate_left()