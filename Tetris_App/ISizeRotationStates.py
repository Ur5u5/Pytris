from typing import List
from abc import ABC
from Tetris_App.BasicRotationState import BasicRotationState
from Tetris_App.Tile import Coordinates, Tile 

class ISizeRotationState(BasicRotationState, ABC):
    pass


class ISizeRotationState0Degree(ISizeRotationState):
    def rotate_right(self):
        self._tetromino.transition_to(globals()["ISizeRotationState90Degree()"])

    def rotate_left(self):
        self._tetromino.transition_to(globals()["ISizeRotationState270Degree()"])

    def get_next_tile_positions(self) -> List[Tile]:
        return [
            Tile(Coordinates(self._tetromino.Tiles[0].Position.X + 2, self._tetromino.Tiles[0].Position.Y - 1), self._tetromino.Tiles[0].Color),
            Tile(Coordinates(self._tetromino.Tiles[1].Position.X + 1, self._tetromino.Tiles[1].Position.Y), self._tetromino.Tiles[1].Color),
            Tile(Coordinates(self._tetromino.Tiles[2].Position.X, self._tetromino.Tiles[2].Position.Y + 1), self._tetromino.Tiles[2].Color),
            Tile(Coordinates(self._tetromino.Tiles[3].Position.X - 1, self._tetromino.Tiles[3].Position.Y + 2), self._tetromino.Tiles[3].Color),
        ]

    def get_previous_tile_positions(self) -> List[Tile]:
        return [
            Tile(Coordinates(self._tetromino.Tiles[0].Position.X + 1, self._tetromino.Tiles[0].Position.Y + 2), self._tetromino.Tiles[0].Color),
            Tile(Coordinates(self._tetromino.Tiles[1].Position.X, self._tetromino.Tiles[1].Position.Y + 1), self._tetromino.Tiles[1].Color),
            Tile(Coordinates(self._tetromino.Tiles[2].Position.X - 1, self._tetromino.Tiles[2].Position.Y), self._tetromino.Tiles[2].Color),
            Tile(Coordinates(self._tetromino.Tiles[3].Position.X - 2, self._tetromino.Tiles[3].Position.Y - 1), self._tetromino.Tiles[3].Color),
        ]


class ISizeRotationState90Degree(ISizeRotationState):
    def rotate_right(self):
        self._tetromino.transition_to(globals()["ISizeRotationState180Degree()"])

    def rotate_left(self):
        self._tetromino.transition_to(globals()["ISizeRotationState0Degree()"])

    def get_next_tile_positions(self) -> List[Tile]:
        return [
            Tile(Coordinates(self._tetromino.Tiles[0].Position.X + 1, self._tetromino.Tiles[0].Position.Y + 2), self._tetromino.Tiles[0].Color),
            Tile(Coordinates(self._tetromino.Tiles[1].Position.X, self._tetromino.Tiles[1].Position.Y + 1), self._tetromino.Tiles[1].Color),
            Tile(Coordinates(self._tetromino.Tiles[2].Position.X - 1, self._tetromino.Tiles[2].Position.Y), self._tetromino.Tiles[2].Color),
            Tile(Coordinates(self._tetromino.Tiles[3].Position.X - 2, self._tetromino.Tiles[3].Position.Y - 1), self._tetromino.Tiles[3].Color),
        ]

    def get_previous_tile_positions(self) -> List[Tile]:
        return [
            Tile(Coordinates(self._tetromino.Tiles[0].Position.X - 2, self._tetromino.Tiles[0].Position.Y + 1), self._tetromino.Tiles[0].Color),
            Tile(Coordinates(self._tetromino.Tiles[1].Position.X - 1, self._tetromino.Tiles[1].Position.Y), self._tetromino.Tiles[1].Color),
            Tile(Coordinates(self._tetromino.Tiles[2].Position.X, self._tetromino.Tiles[2].Position.Y - 1), self._tetromino.Tiles[2].Color),
            Tile(Coordinates(self._tetromino.Tiles[3].Position.X + 1, self._tetromino.Tiles[3].Position.Y - 2), self._tetromino.Tiles[3].Color),
        ]


class ISizeRotationState180Degree(ISizeRotationState):
    def rotate_right(self):
        self._tetromino.transition_to(globals()["ISizeRotationState270Degree()"])

    def rotate_left(self):
        self._tetromino.transition_to(globals()["ISizeRotationState90Degree()"])

    def get_next_tile_positions(self) -> List[Tile]:
        return [
            Tile(Coordinates(self._tetromino.Tiles[0].Position.X - 2, self._tetromino.Tiles[0].Position.Y + 1), self._tetromino.Tiles[0].Color),
            Tile(Coordinates(self._tetromino.Tiles[1].Position.X - 1, self._tetromino.Tiles[1].Position.Y), self._tetromino.Tiles[1].Color),
            Tile(Coordinates(self._tetromino.Tiles[2].Position.X, self._tetromino.Tiles[2].Position.Y - 1), self._tetromino.Tiles[2].Color),
            Tile(Coordinates(self._tetromino.Tiles[3].Position.X + 1, self._tetromino.Tiles[3].Position.Y - 2), self._tetromino.Tiles[3].Color),
        ]

    def get_previous_tile_positions(self) -> List[Tile]:
        return [
            Tile(Coordinates(self._tetromino.Tiles[0].Position.X - 1, self._tetromino.Tiles[0].Position.Y - 2), self._tetromino.Tiles[0].Color),
            Tile(Coordinates(self._tetromino.Tiles[1].Position.X, self._tetromino.Tiles[1].Position.Y - 1), self._tetromino.Tiles[1].Color),
            Tile(Coordinates(self._tetromino.Tiles[2].Position.X + 1, self._tetromino.Tiles[2].Position.Y), self._tetromino.Tiles[2].Color),
            Tile(Coordinates(self._tetromino.Tiles[3].Position.X + 2, self._tetromino.Tiles[3].Position.Y + 1), self._tetromino.Tiles[3].Color),
        ]


class ISizeRotationState270Degree(ISizeRotationState):
    def rotate_right(self):
        self._tetromino.transition_to(globals()["ISizeRotationState0Degree()"])

    def rotate_left(self):
        self._tetromino.transition_to(globals()["ISizeRotationState180Degree()"])

    def get_next_tile_positions(self) -> List[Tile]:
        return [
            Tile(Coordinates(self._tetromino.Tiles[0].Position.X - 1, self._tetromino.Tiles[0].Position.Y - 2), self._tetromino.Tiles[0].Color),
            Tile(Coordinates(self._tetromino.Tiles[1].Position.X, self._tetromino.Tiles[1].Position.Y - 1), self._tetromino.Tiles[1].Color),
            Tile(Coordinates(self._tetromino.Tiles[2].Position.X + 1, self._tetromino.Tiles[2].Position.Y), self._tetromino.Tiles[2].Color),
            Tile(Coordinates(self._tetromino.Tiles[3].Position.X + 2, self._tetromino.Tiles[3].Position.Y + 1), self._tetromino.Tiles[3].Color),
        ]

    def get_previous_tile_positions(self) -> List[Tile]:
        return [
            Tile(Coordinates(self._tetromino.Tiles[0].Position.X + 2, self._tetromino.Tiles[0].Position.Y - 1), self._tetromino.Tiles[0].Color),
            Tile(Coordinates(self._tetromino.Tiles[1].Position.X + 1, self._tetromino.Tiles[1].Position.Y), self._tetromino.Tiles[1].Color),
            Tile(Coordinates(self._tetromino.Tiles[2].Position.X, self._tetromino.Tiles[2].Position.Y + 1), self._tetromino.Tiles[2].Color),
            Tile(Coordinates(self._tetromino.Tiles[3].Position.X - 1, self._tetromino.Tiles[3].Position.Y + 2), self._tetromino.Tiles[3].Color),
        ]
