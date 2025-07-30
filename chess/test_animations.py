#!/usr/bin/env python3
"""
Test script for chess animations.
This script verifies that all the chess animation modules can be imported correctly.
"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported."""
    try:
        # Test chess_board module
        from chess_board import ChessBoard
        print("✓ chess_board module imported successfully")
        
        # Test chess_algebra module
        from chess_algebra import ChessAlgebraScene, PieceMovementAnalysis
        print("✓ chess_algebra module imported successfully")
        
        # Test advanced_chess_math module
        from advanced_chess_math import AdvancedChessMathematics, ChessPositionAnalysis
        print("✓ advanced_chess_math module imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def test_chess_board():
    """Test the ChessBoard utility class."""
    try:
        from chess_board import ChessBoard
        
        board = ChessBoard()
        
        # Test coordinate conversion
        coords = board.algebraic_to_coordinates("e4")
        assert coords == (3, 4), f"Expected (3, 4), got {coords}"
        print("✓ Coordinate conversion works correctly")
        
        # Test algebraic notation
        square = board.coordinates_to_algebraic(3, 4)
        assert square == "e4", f"Expected 'e4', got {square}"
        print("✓ Algebraic notation works correctly")
        
        # Test piece moves
        knight_moves = board.get_piece_moves("N", "e4")
        assert len(knight_moves) > 0, "Knight should have valid moves"
        print("✓ Piece movement calculation works correctly")
        
        return True
        
    except Exception as e:
        print(f"✗ ChessBoard test failed: {e}")
        return False

def test_manim_available():
    """Test that Manim is available."""
    try:
        import manim
        print("✓ Manim is available")
        return True
    except ImportError:
        print("✗ Manim is not installed. Please install it with: pip install manim")
        return False

def main():
    """Run all tests."""
    print("Testing Chess Animation Modules...")
    print("=" * 40)
    
    tests = [
        ("Manim availability", test_manim_available),
        ("Module imports", test_imports),
        ("ChessBoard functionality", test_chess_board),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nRunning {test_name}...")
        if test_func():
            passed += 1
        else:
            print(f"✗ {test_name} failed")
    
    print("\n" + "=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! You can now run the animations.")
        print("\nExample commands:")
        print("  manim chess_algebra.py ChessAlgebraScene -pql")
        print("  manim advanced_chess_math.py AdvancedChessMathematics -pql")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 