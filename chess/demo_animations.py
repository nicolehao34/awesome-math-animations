#!/usr/bin/env python3
"""
Chess Algebra Animations Demo
This script demonstrates all the animated chess algebra concepts.
"""

import os
import sys
import subprocess
from pathlib import Path

def show_animation_info():
    """Display information about the animations."""
    print("🎬 CHESS ALGEBRA ANIMATIONS")
    print("=" * 50)
    print()
    print("This project demonstrates chess concepts using algebra and mathematics.")
    print("Each animation shows a different mathematical aspect of chess.")
    print()

def list_animations():
    """List all available animations."""
    animations = [
        {
            "file": "chess_coordinate_system_animated.gif",
            "title": "Chess Coordinate System",
            "description": "Shows the 8×8 coordinate grid with algebraic notation. The e4 square pulses to demonstrate coordinate conversion.",
            "concepts": ["Coordinate Geometry", "Algebraic Notation", "Grid System"]
        },
        {
            "file": "knight_movement_animated.gif", 
            "title": "Knight Movement: L-Shaped Vectors",
            "description": "Demonstrates knight movement patterns using L-shaped vectors. Arrows appear sequentially to show all possible moves.",
            "concepts": ["Vector Analysis", "L-Shaped Movement", "|dx| + |dy| = 3"]
        },
        {
            "file": "bishop_movement_animated.gif",
            "title": "Bishop Movement: Diagonal Vectors", 
            "description": "Shows bishop diagonal movement patterns. Arrows reveal the diagonal nature of bishop moves.",
            "concepts": ["Diagonal Vectors", "|dx| = |dy|", "Unlimited Range"]
        },
        {
            "file": "distance_heatmap_animated.gif",
            "title": "Distance Analysis from e4",
            "description": "Heatmap showing Euclidean distances from e4 to all squares. Gradually reveals the distance matrix.",
            "concepts": ["Euclidean Distance", "Distance Matrix", "Position Analysis"]
        },
        {
            "file": "piece_comparison_animated.gif",
            "title": "Piece Movement Comparison",
            "description": "Side-by-side comparison of all piece movement patterns. Each piece appears with its movement options.",
            "concepts": ["Piece Comparison", "Movement Patterns", "Vector Differences"]
        },
        {
            "file": "vector_analysis_animated.gif",
            "title": "Chess Vector Analysis",
            "description": "Mathematical vector analysis showing different piece movement vectors in coordinate space.",
            "concepts": ["Vector Mathematics", "Coordinate Space", "Movement Vectors"]
        }
    ]
    
    print("📋 AVAILABLE ANIMATIONS:")
    print("-" * 50)
    
    for i, anim in enumerate(animations, 1):
        print(f"{i}. {anim['title']}")
        print(f"   File: {anim['file']}")
        print(f"   Description: {anim['description']}")
        print(f"   Concepts: {', '.join(anim['concepts'])}")
        print()
    
    return animations

def check_animation_files():
    """Check if all animation files exist."""
    expected_files = [
        "chess_coordinate_system_animated.gif",
        "knight_movement_animated.gif", 
        "bishop_movement_animated.gif",
        "distance_heatmap_animated.gif",
        "piece_comparison_animated.gif",
        "vector_analysis_animated.gif"
    ]
    
    missing_files = []
    existing_files = []
    
    for file in expected_files:
        if os.path.exists(file):
            file_size = os.path.getsize(file)
            existing_files.append((file, file_size))
        else:
            missing_files.append(file)
    
    print("📁 ANIMATION FILES STATUS:")
    print("-" * 30)
    
    if existing_files:
        print("✅ Existing animations:")
        for file, size in existing_files:
            size_mb = size / (1024 * 1024)
            print(f"   • {file} ({size_mb:.1f} MB)")
        print()
    
    if missing_files:
        print("❌ Missing animations:")
        for file in missing_files:
            print(f"   • {file}")
        print()
        print("To create missing animations, run:")
        print("   python chess_animations.py")
        print()
    
    return len(missing_files) == 0

def show_mathematical_concepts():
    """Show the mathematical concepts demonstrated in the animations."""
    print("🧮 MATHEMATICAL CONCEPTS DEMONSTRATED:")
    print("=" * 50)
    
    concepts = [
        {
            "concept": "Coordinate Geometry",
            "description": "8×8 coordinate grid system with algebraic notation",
            "formula": "Position = (file, rank) → e4 = (4, 4)"
        },
        {
            "concept": "Vector Analysis", 
            "description": "Piece movements as mathematical vectors",
            "formula": "Move = (dx, dy) where dx, dy are displacements"
        },
        {
            "concept": "Knight Mathematics",
            "description": "L-shaped movement pattern with mathematical property",
            "formula": "|dx| + |dy| = 3 for all knight moves"
        },
        {
            "concept": "Bishop Mathematics",
            "description": "Diagonal movement with equal components",
            "formula": "|dx| = |dy| for all bishop moves"
        },
        {
            "concept": "Distance Metrics",
            "description": "Euclidean distance between chess squares",
            "formula": "d = √((x₂ - x₁)² + (y₂ - y₁)²)"
        },
        {
            "concept": "Game Theory",
            "description": "Strategic decision making in chess positions",
            "formula": "Nash Equilibrium: Optimal strategies for both players"
        }
    ]
    
    for i, concept in enumerate(concepts, 1):
        print(f"{i}. {concept['concept']}")
        print(f"   Description: {concept['description']}")
        print(f"   Formula: {concept['formula']}")
        print()

def show_usage_instructions():
    """Show how to use the animations."""
    print("🚀 HOW TO USE THE ANIMATIONS:")
    print("=" * 40)
    print()
    print("1. View individual animations:")
    print("   • Open any .gif file in your browser or image viewer")
    print("   • Each animation demonstrates a specific concept")
    print()
    print("2. Educational applications:")
    print("   • Use in math classes to show real-world applications")
    print("   • Demonstrate vector analysis with chess pieces")
    print("   • Teach coordinate geometry using chess board")
    print()
    print("3. Create custom animations:")
    print("   • Modify chess_animations.py to create new animations")
    print("   • Adjust timing, colors, or add new concepts")
    print()
    print("4. Integration with other tools:")
    print("   • Import animations into presentations")
    print("   • Use in educational videos")
    print("   • Share with students for interactive learning")
    print()

def show_technical_details():
    """Show technical details about the animations."""
    print("⚙️ TECHNICAL DETAILS:")
    print("=" * 30)
    print()
    print("Animation Specifications:")
    print("• Format: GIF (Graphics Interchange Format)")
    print("• Frame Rate: 10-20 FPS")
    print("• Resolution: High DPI (300 DPI)")
    print("• Duration: 5-12 seconds per animation")
    print()
    print("Creation Process:")
    print("• Built with matplotlib.animation")
    print("• Uses FuncAnimation for smooth transitions")
    print("• Alpha blending for fade effects")
    print("• Sequential reveal for educational clarity")
    print()
    print("File Sizes:")
    print("• Small animations: ~30-150 KB")
    print("• Large animations: ~200-600 KB")
    print("• Optimized for web sharing and presentations")
    print()

def interactive_demo():
    """Run an interactive demo."""
    print("🎯 INTERACTIVE DEMO")
    print("=" * 20)
    print()
    
    while True:
        print("Choose an option:")
        print("1. List all animations")
        print("2. Check file status")
        print("3. Show mathematical concepts")
        print("4. Show usage instructions")
        print("5. Show technical details")
        print("6. Create new animations")
        print("7. Exit")
        print()
        
        try:
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                list_animations()
            elif choice == '2':
                check_animation_files()
            elif choice == '3':
                show_mathematical_concepts()
            elif choice == '4':
                show_usage_instructions()
            elif choice == '5':
                show_technical_details()
            elif choice == '6':
                print("Creating new animations...")
                subprocess.run([sys.executable, "chess_animations.py"])
                print("Animations created successfully!")
            elif choice == '7':
                print("Goodbye! 🎉")
                break
            else:
                print("Invalid choice. Please enter a number between 1-7.")
            
            print()
            input("Press Enter to continue...")
            print("\n" + "="*50 + "\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye! 🎉")
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    """Main demo function."""
    show_animation_info()
    
    # Check if animations exist
    all_exist = check_animation_files()
    
    if all_exist:
        print("🎉 All animations are ready!")
    else:
        print("⚠️  Some animations are missing. Run 'python chess_animations.py' to create them.")
    
    print()
    
    # Show available options
    print("What would you like to do?")
    print("1. Run interactive demo")
    print("2. View animation information")
    print("3. Exit")
    print()
    
    try:
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            interactive_demo()
        elif choice == '2':
            list_animations()
            show_mathematical_concepts()
            show_usage_instructions()
            show_technical_details()
        elif choice == '3':
            print("Goodbye! 🎉")
        else:
            print("Invalid choice. Running interactive demo...")
            interactive_demo()
            
    except KeyboardInterrupt:
        print("\nGoodbye! 🎉")

if __name__ == "__main__":
    main() 