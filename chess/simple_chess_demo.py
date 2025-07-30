#!/usr/bin/env python3
"""
Simple Chess Algebra Demonstration
This script demonstrates chess concepts using algebra without requiring full manim.
"""

import numpy as np
from chess_board import ChessBoard

def demonstrate_coordinate_system():
    """Demonstrate the chess coordinate system."""
    print("=" * 50)
    print("CHESS COORDINATE SYSTEM")
    print("=" * 50)
    
    board = ChessBoard()
    
    # Show some coordinate conversions
    test_squares = ["e4", "d4", "e5", "f3", "a1", "h8"]
    
    for square in test_squares:
        coords = board.algebraic_to_coordinates(square)
        back_to_square = board.coordinates_to_algebraic(*coords)
        print(f"{square} → {coords} → {back_to_square}")
    
    print()

def demonstrate_piece_movements():
    """Demonstrate piece movement vectors."""
    print("=" * 50)
    print("PIECE MOVEMENT VECTORS")
    print("=" * 50)
    
    board = ChessBoard()
    
    # Test different pieces
    pieces = [
        ("N", "e4", "Knight"),
        ("B", "e4", "Bishop"),
        ("R", "e4", "Rook"),
        ("Q", "e4", "Queen"),
        ("K", "e4", "King")
    ]
    
    for piece, position, name in pieces:
        moves = board.get_piece_moves(piece, position)
        print(f"{name} at {position}: {len(moves)} possible moves")
        print(f"  Sample moves: {moves[:5]}")
        print()

def demonstrate_knight_mathematics():
    """Demonstrate knight movement mathematics."""
    print("=" * 50)
    print("KNIGHT MATHEMATICS")
    print("=" * 50)
    
    # Knight moves: L-shaped pattern
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    print("Knight movement vectors:")
    for dx, dy in knight_moves:
        print(f"  ({dx}, {dy})")
    
    print("\nMathematical property: |dx| + |dy| = 3")
    for dx, dy in knight_moves:
        total = abs(dx) + abs(dy)
        print(f"  |{dx}| + |{dy}| = {abs(dx)} + {abs(dy)} = {total}")
    
    print()

def demonstrate_bishop_mathematics():
    """Demonstrate bishop movement mathematics."""
    print("=" * 50)
    print("BISHOP MATHEMATICS")
    print("=" * 50)
    
    # Bishop moves: diagonal pattern
    bishop_moves = []
    for i in range(1, 5):
        bishop_moves.extend([
            (i, i), (i, -i), (-i, i), (-i, -i)
        ])
    
    print("Bishop movement vectors:")
    for dx, dy in bishop_moves:
        print(f"  ({dx}, {dy})")
    
    print("\nMathematical property: |dx| = |dy|")
    for dx, dy in bishop_moves:
        print(f"  |{dx}| = |{dy}| = {abs(dx)}")
    
    print()

def demonstrate_distance_analysis():
    """Demonstrate distance analysis."""
    print("=" * 50)
    print("DISTANCE ANALYSIS")
    print("=" * 50)
    
    board = ChessBoard()
    
    # Calculate distances from e4 to various squares
    start_square = "e4"
    start_coords = board.algebraic_to_coordinates(start_square)
    
    test_squares = ["e4", "d4", "e5", "d5", "f6", "a1", "h8"]
    
    print(f"Distances from {start_square} ({start_coords}):")
    for square in test_squares:
        end_coords = board.algebraic_to_coordinates(square)
        dx = end_coords[1] - start_coords[1]
        dy = end_coords[0] - start_coords[0]
        distance = np.sqrt(dx**2 + dy**2)
        print(f"  {start_square} → {square}: distance = {distance:.2f} (dx={dx}, dy={dy})")
    
    print()

def demonstrate_vector_representations():
    """Demonstrate vector representations of positions."""
    print("=" * 50)
    print("VECTOR REPRESENTATIONS")
    print("=" * 50)
    
    board = ChessBoard()
    
    # Show vector representation of e4
    e4_vector = board.get_vector_representation("e4")
    print(f"e4 vector (first 16 elements): {e4_vector[:16]}")
    print(f"e4 vector sum: {np.sum(e4_vector)} (should be 1)")
    
    # Show distance matrix properties
    distance_matrix = board.get_distance_matrix()
    print(f"Distance matrix shape: {distance_matrix.shape}")
    print(f"Distance matrix min: {np.min(distance_matrix):.2f}")
    print(f"Distance matrix max: {np.max(distance_matrix):.2f}")
    
    print()

def demonstrate_game_theory_concepts():
    """Demonstrate game theory concepts in chess."""
    print("=" * 50)
    print("GAME THEORY CONCEPTS")
    print("=" * 50)
    
    # Simple payoff matrix for opening moves
    print("Opening Move Payoff Matrix (White perspective):")
    print("          Black: e5  Black: d5  Black: Nf6")
    print("White: e4    0.5      0.6      0.4")
    print("White: d4    0.4      0.5      0.6")
    print("White: Nf3   0.6      0.4      0.5")
    
    print("\nNash Equilibrium: Both players choose optimal strategies")
    print("Expected Value = Σ(Probability × Value)")
    
    print()

def main():
    """Run all demonstrations."""
    print("CHESS ALGEBRA DEMONSTRATION")
    print("Mathematical Analysis of Chess Concepts")
    print("=" * 60)
    print()
    
    demonstrate_coordinate_system()
    demonstrate_piece_movements()
    demonstrate_knight_mathematics()
    demonstrate_bishop_mathematics()
    demonstrate_distance_analysis()
    demonstrate_vector_representations()
    demonstrate_game_theory_concepts()
    
    print("=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print()
    print("Key Mathematical Concepts Demonstrated:")
    print("• Coordinate Geometry: Algebraic notation system")
    print("• Vector Analysis: Piece movement patterns")
    print("• Distance Metrics: Euclidean geometry in chess")
    print("• Game Theory: Strategic decision making")
    print("• Linear Algebra: Position vector representations")
    print()
    print("To run full animations with manim:")
    print("  pip install manim[all]")
    print("  manim chess_algebra.py ChessAlgebraScene -pql")

if __name__ == "__main__":
    main() 