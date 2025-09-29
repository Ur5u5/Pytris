from typing import List
from Tetris_App.GameBoard import GameBoard
from Tetris_App.Tetromino import Tetromino
from Tetris_App.Tile import Coordinates, Tile


class TetrominoMover():
    _gameBoard: GameBoard

    def __init__(self, gameBoard: GameBoard) -> None:
        self._gameBoard = gameBoard

    def move_right(self, tetromino: Tetromino) -> None:
        next_position: List[Tile] = [
            Tile(Coordinates(tile.Position.X + 1, tile.Position.Y), tile.Color)
            for tile in tetromino.Tiles
        ]

    def CanMove(self, nextPosition: List[Tile]):
        return not any(self._gameBoard.IsPo)
