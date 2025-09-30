from typing import List
from Tetris_App.BasicRotationState import BasicRotationState
from Tetris_App.Tile import Tile


class Tetromino():
    _rotationState: BasicRotationState
    _tiles: List[Tile]

    @property
    def Tiles(self) -> List[Tile]:
        return self._tiles
    
    @Tiles.setter
    def Tiles(self, value: List[Tile]) -> None:
        self._tiles = value
    
    def __init__(self, rotationState: BasicRotationState) -> None:
        self.transition_to(rotationState)

    def transition_to(self, rotationState: BasicRotationState) -> None:
        self._rotationState = rotationState
        self._rotationState.set_tetromino(self)

    def rotate_right(self):
        self._rotationState.rotate_right()

    def rotate_left(self):
        self._rotationState.rotate_left()

    def get_next_tile_positions(self) -> List[Tile]:
        return self._rotationState.get_next_tile_position()
    
    def get_previous_tile_positions(self) -> List[Tile]:
        return  self._rotationState.get_previous_tile_position()