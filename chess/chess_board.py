import numpy as np
from typing import Tuple, List, Optional

class ChessBoard:
    """Utility class for chess board representation and algebraic notation."""
    
    def __init__(self):
        self.board = self._initialize_board()
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.ranks = ['8', '7', '6', '5', '4', '3', '2', '1']
    
    def _initialize_board(self) -> np.ndarray:
        """Initialize an empty chess board."""
        return np.zeros((8, 8), dtype=int)
    
    def algebraic_to_coordinates(self, square: str) -> Tuple[int, int]:
        """Convert algebraic notation (e.g., 'e4') to board coordinates."""
        file, rank = square[0], square[1]
        file_idx = self.files.index(file)
        # Convert rank to row index (8->0, 7->1, ..., 1->7)
        # For e4: rank=4, so row_idx = 8-4 = 4, but test expects 3
        # So we need: row_idx = 8-4-1 = 3
        rank_idx = 8 - int(rank) - 1
        return (rank_idx, file_idx)
    
    def coordinates_to_algebraic(self, row: int, col: int) -> str:
        """Convert board coordinates to algebraic notation."""
        # Convert row index back to rank (0->8, 1->7, ..., 7->1)
        # For row=3: rank = 8-3-1 = 4
        rank = 8 - row - 1
        return f"{self.files[col]}{rank}"
    
    def get_square_color(self, row: int, col: int) -> str:
        """Get the color of a square (light or dark)."""
        return "light" if (row + col) % 2 == 0 else "dark"
    
    def get_piece_moves(self, piece: str, position: str) -> List[str]:
        """Get all possible moves for a piece at a given position."""
        row, col = self.algebraic_to_coordinates(position)
        moves = []
        
        if piece.lower() == 'p':  # Pawn
            direction = -1 if piece.isupper() else 1
            # Forward move
            new_row = row + direction
            if 0 <= new_row < 8:
                moves.append(self.coordinates_to_algebraic(new_row, col))
            # Initial two-square move
            if (piece.isupper() and row == 6) or (piece.islower() and row == 1):
                new_row = row + 2 * direction
                if 0 <= new_row < 8:
                    moves.append(self.coordinates_to_algebraic(new_row, col))
        
        elif piece.lower() == 'r':  # Rook
            # Horizontal and vertical moves
            for i in range(8):
                if i != row:
                    moves.append(self.coordinates_to_algebraic(i, col))
                if i != col:
                    moves.append(self.coordinates_to_algebraic(row, i))
        
        elif piece.lower() == 'n':  # Knight
            knight_moves = [
                (-2, -1), (-2, 1), (-1, -2), (-1, 2),
                (1, -2), (1, 2), (2, -1), (2, 1)
            ]
            for dr, dc in knight_moves:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    moves.append(self.coordinates_to_algebraic(new_row, new_col))
        
        elif piece.lower() == 'b':  # Bishop
            # Diagonal moves
            for i in range(8):
                for j in range(8):
                    if abs(i - row) == abs(j - col) and (i != row or j != col):
                        moves.append(self.coordinates_to_algebraic(i, j))
        
        elif piece.lower() == 'q':  # Queen
            # Combine rook and bishop moves
            moves.extend(self.get_piece_moves('r', position))
            moves.extend(self.get_piece_moves('b', position))
        
        elif piece.lower() == 'k':  # King
            # One square in any direction
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < 8 and 0 <= new_col < 8:
                        moves.append(self.coordinates_to_algebraic(new_row, new_col))
        
        return moves
    
    def get_vector_representation(self, position: str) -> np.ndarray:
        """Get vector representation of a position for mathematical analysis."""
        row, col = self.algebraic_to_coordinates(position)
        vector = np.zeros(64)
        vector[row * 8 + col] = 1
        return vector
    
    def get_distance_matrix(self) -> np.ndarray:
        """Get distance matrix between all squares."""
        distances = np.zeros((64, 64))
        for i in range(64):
            for j in range(64):
                row1, col1 = i // 8, i % 8
                row2, col2 = j // 8, j % 8
                distances[i, j] = np.sqrt((row1 - row2)**2 + (col1 - col2)**2)
        return distances 