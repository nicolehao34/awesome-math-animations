#!/usr/bin/env python3
"""
Example script for running chess animations.
This script shows how to run different chess animation scenes.
"""

import subprocess
import sys
import os

def run_animation(scene_file, scene_name, quality="l", preview=True):
    """Run a specific animation scene."""
    cmd = ["manim", scene_file, scene_name]
    
    if preview:
        cmd.append("-p")
    
    cmd.extend(["-q", quality])
    
    print(f"Running: {' '.join(cmd)}")
    print("-" * 50)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(__file__))
        
        if result.returncode == 0:
            print("✓ Animation completed successfully!")
        else:
            print(f"✗ Animation failed with return code {result.returncode}")
            print("Error output:")
            print(result.stderr)
        
        return result.returncode == 0
        
    except FileNotFoundError:
        print("✗ Manim not found. Please install it with: pip install manim")
        return False
    except Exception as e:
        print(f"✗ Error running animation: {e}")
        return False

def main():
    """Run example animations."""
    print("Chess Algebra Animations - Examples")
    print("=" * 50)
    
    # Define the animations to run
    animations = [
        {
            "name": "Basic Chess Algebra",
            "file": "chess_algebra.py",
            "scene": "ChessAlgebraScene",
            "description": "Introduction to chess as algebra with coordinate systems and piece movements"
        },
        {
            "name": "Piece Movement Analysis",
            "file": "chess_algebra.py", 
            "scene": "PieceMovementAnalysis",
            "description": "Detailed analysis of each piece's movement patterns using vectors"
        },
        {
            "name": "Advanced Chess Mathematics",
            "file": "advanced_chess_math.py",
            "scene": "AdvancedChessMathematics", 
            "description": "Game theory, probability, and optimization in chess"
        },
        {
            "name": "Position Analysis",
            "file": "advanced_chess_math.py",
            "scene": "ChessPositionAnalysis",
            "description": "Analysis of opening, middlegame, and endgame positions"
        }
    ]
    
    print("Available animations:")
    for i, anim in enumerate(animations, 1):
        print(f"{i}. {anim['name']}")
        print(f"   File: {anim['file']}")
        print(f"   Scene: {anim['scene']}")
        print(f"   Description: {anim['description']}")
        print()
    
    # Ask user which animation to run
    try:
        choice = input("Enter the number of the animation to run (or 'all' for all): ").strip()
        
        if choice.lower() == 'all':
            # Run all animations
            print("\nRunning all animations...")
            for anim in animations:
                print(f"\n{'='*20} {anim['name']} {'='*20}")
                success = run_animation(anim['file'], anim['scene'])
                if not success:
                    print(f"Failed to run {anim['name']}")
                    break
        else:
            # Run specific animation
            try:
                index = int(choice) - 1
                if 0 <= index < len(animations):
                    anim = animations[index]
                    print(f"\nRunning {anim['name']}...")
                    run_animation(anim['file'], anim['scene'])
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number or 'all'.")
    
    except KeyboardInterrupt:
        print("\nAnimation cancelled by user.")
    
    print("\nAnimation commands for manual use:")
    print("-" * 50)
    for anim in animations:
        print(f"# {anim['name']}")
        print(f"manim {anim['file']} {anim['scene']} -pql")
        print()

def show_help():
    """Show help information."""
    print("Chess Algebra Animations - Help")
    print("=" * 40)
    print()
    print("This script helps you run chess animations that explain chess using algebra.")
    print()
    print("Available commands:")
    print("  python run_examples.py          # Interactive mode")
    print("  python run_examples.py --help   # Show this help")
    print("  python run_examples.py --list   # List all animations")
    print()
    print("Manual commands:")
    print("  manim chess_algebra.py ChessAlgebraScene -pql")
    print("  manim advanced_chess_math.py AdvancedChessMathematics -pql")
    print()
    print("Quality options:")
    print("  -pql  # Low quality (fast)")
    print("  -pqm  # Medium quality")
    print("  -pqh  # High quality")
    print("  -pqk  # 4K quality (slow)")
    print()
    print("For more information, see README.md")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            show_help()
        elif sys.argv[1] in ["--list", "-l"]:
            print("Available animations:")
            print("1. Basic Chess Algebra (ChessAlgebraScene)")
            print("2. Piece Movement Analysis (PieceMovementAnalysis)")
            print("3. Advanced Chess Mathematics (AdvancedChessMathematics)")
            print("4. Position Analysis (ChessPositionAnalysis)")
        else:
            print("Unknown option. Use --help for usage information.")
    else:
        main() 