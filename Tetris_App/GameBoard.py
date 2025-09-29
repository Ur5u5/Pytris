from typing import List
from Tetris_App.Tile import Tile, Coordinates, TileColor

class GameBoard():
    def __init(self, width: int, height: int):
        self._width = width
        self._height = height
        self._tiles = self._create_tiles()
        
    def is_position_occupied(self, tile: Tile) -> bool:
        if (tile.Position.X < 0 or tile.Position.X >= self._width or tile.Position.Y < 0 or tile.Position.Y >= self._height):
            return True
        
        return False
    
    def _create_tiles(self) -> List[List[Tile]]:
        return [[Tile(Coordinates(x,y), TileColor.Transparent) for y in range(self._width)] for x in range(self._height)]
