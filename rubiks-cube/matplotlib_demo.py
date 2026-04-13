#!/usr/bin/env python3
"""
Rubik's Cube Visualization using Matplotlib
This works immediately without Manim installation issues!

Run: python matplotlib_demo.py
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.animation as animation

# Standard Rubik's cube colors
COLORS = {
    'W': '#FFFFFF',  # White
    'Y': '#FFFF00',  # Yellow
    'R': '#FF0000',  # Red
    'O': '#FFA500',  # Orange
    'B': '#0000FF',  # Blue
    'G': '#00FF00',  # Green
    'K': '#000000',  # Black (interior)
}


def create_cubie_faces(center, size=0.9):
    """Create the 6 faces of a single cubie."""
    s = size / 2
    x, y, z = center
    
    # Define vertices of a cube
    vertices = np.array([
        [x-s, y-s, z-s], [x+s, y-s, z-s], [x+s, y+s, z-s], [x-s, y+s, z-s],  # Bottom
        [x-s, y-s, z+s], [x+s, y-s, z+s], [x+s, y+s, z+s], [x-s, y+s, z+s],  # Top
    ])
    
    # Define the 6 faces
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # Front
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # Back
        [vertices[0], vertices[3], vertices[7], vertices[4]],  # Left
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # Right
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # Top
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # Bottom
    ]
    
    return faces


def get_cubie_colors(x, y, z):
    """Determine colors for a cubie based on position."""
    colors = ['K', 'K', 'K', 'K', 'K', 'K']  # [Front, Back, Left, Right, Top, Bottom]
    
    if y == 1:  colors[0] = 'R'  # Front face
    if y == -1: colors[1] = 'O'  # Back face
    if x == -1: colors[2] = 'G'  # Left face
    if x == 1:  colors[3] = 'B'  # Right face
    if z == 1:  colors[4] = 'W'  # Top face
    if z == -1: colors[5] = 'Y'  # Bottom face
    
    return colors


def create_rubiks_cube():
    """Create a complete Rubik's cube."""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create all 27 cubies
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                center = np.array([x, y, z])
                faces = create_cubie_faces(center)
                cubie_colors = get_cubie_colors(x, y, z)
                
                # Draw each face
                for face, color_key in zip(faces, cubie_colors):
                    poly = Poly3DCollection([face], 
                                          facecolors=COLORS[color_key],
                                          edgecolors='black',
                                          linewidths=2)
                    ax.add_collection3d(poly)
    
    # Set the axes
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Rubik\'s Cube in 3D', fontsize=16, fontweight='bold')
    
    return fig, ax


def demonstrate_rotation():
    """Animate the cube rotating."""
    fig, ax = create_rubiks_cube()
    
    def rotate(frame):
        ax.view_init(elev=20, azim=frame)
        return ax,
    
    anim = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 360, 2),
                                  interval=50, blit=False)
    
    plt.show()


def show_permutation_cycles():
    """Visualize permutation cycle notation."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    
    # Title
    ax.text(0.5, 0.95, 'Rubik\'s Cube Permutations', 
            ha='center', va='top', fontsize=24, fontweight='bold',
            transform=ax.transAxes)
    
    # Cycle notation explanation
    ax.text(0.5, 0.85, 'Cycle Notation: (1 2 3)(4 5)', 
            ha='center', va='top', fontsize=18, color='blue',
            transform=ax.transAxes)
    
    # Arrows showing permutation
    arrows_y = 0.70
    items = ['1 → 2', '2 → 3', '3 → 1', '4 → 5', '5 → 4']
    for i, item in enumerate(items):
        ax.text(0.15 + i * 0.15, arrows_y, item,
                ha='center', va='center', fontsize=16, 
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7),
                transform=ax.transAxes)
    
    # R move example
    ax.text(0.5, 0.55, 'R Move (Right clockwise):', 
            ha='center', va='top', fontsize=18, fontweight='bold',
            transform=ax.transAxes)
    
    ax.text(0.5, 0.47, 'Corners: (1 2 6 5)', 
            ha='center', va='top', fontsize=16, color='red',
            transform=ax.transAxes)
    
    ax.text(0.5, 0.40, 'Edges: (9 10 18 13)', 
            ha='center', va='top', fontsize=16, color='blue',
            transform=ax.transAxes)
    
    # Key insight
    ax.text(0.5, 0.28, 'Key Insight:', 
            ha='center', va='top', fontsize=18, fontweight='bold',
            transform=ax.transAxes)
    
    insight_text = ('Every move on a Rubik\'s cube is a PERMUTATION\n'
                   'Repeating R four times returns to the start (Order = 4)\n'
                   'Commutators [A,B] = ABA\'B\' create 3-cycles')
    
    ax.text(0.5, 0.20, insight_text,
            ha='center', va='top', fontsize=14, 
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5),
            transform=ax.transAxes)
    
    plt.tight_layout()
    plt.show()


def show_group_theory():
    """Display group theory concepts."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    
    # Title
    ax.text(0.5, 0.95, 'The Rubik\'s Cube Group', 
            ha='center', va='top', fontsize=24, fontweight='bold',
            transform=ax.transAxes)
    
    # Group properties
    properties = [
        '• Set: ~43 quintillion positions',
        '• Identity: Solved cube',
        '• Operation: Compose moves',
        '• Inverses: Every R has R\'',
        '• Associativity: (AB)C = A(BC)',
    ]
    
    y_pos = 0.80
    for prop in properties:
        ax.text(0.2, y_pos, prop,
                ha='left', va='top', fontsize=16,
                transform=ax.transAxes)
        y_pos -= 0.09
    
    # Generators
    ax.text(0.5, 0.40, 'Generators: {R, L, U, D, F, B}', 
            ha='center', va='top', fontsize=16, color='blue',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5),
            transform=ax.transAxes)
    
    # God's number
    ax.text(0.5, 0.28, 'God\'s Number: 20', 
            ha='center', va='top', fontsize=20, fontweight='bold', color='red',
            transform=ax.transAxes)
    
    ax.text(0.5, 0.20, '(Maximum moves to solve ANY position)',
            ha='center', va='top', fontsize=14, color='gray',
            transform=ax.transAxes)
    
    # Impossible positions
    ax.text(0.5, 0.10, 'Parity: Cannot swap just 2 pieces!', 
            ha='center', va='top', fontsize=14, color='darkred',
            bbox=dict(boxstyle='round', facecolor='pink', alpha=0.7),
            transform=ax.transAxes)
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("=" * 60)
    print("Rubik's Cube Permutation Visualizations")
    print("=" * 60)
    print("\nChoose a demonstration:")
    print("1. Static 3D Rubik's Cube")
    print("2. Rotating Cube Animation")
    print("3. Permutation Cycles Explanation")
    print("4. Group Theory Concepts")
    print("5. All Visualizations")
    
    choice = input("\nEnter choice (1-5): ").strip()
    
    if choice == '1' or choice == '5':
        print("\n📊 Showing static cube...")
        fig, ax = create_rubiks_cube()
        ax.view_init(elev=20, azim=45)
        plt.show()
    
    if choice == '2' or choice == '5':
        print("\n🔄 Showing rotating cube animation...")
        demonstrate_rotation()
    
    if choice == '3' or choice == '5':
        print("\n📐 Showing permutation cycles...")
        show_permutation_cycles()
    
    if choice == '4' or choice == '5':
        print("\n🎓 Showing group theory...")
        show_group_theory()
    
    print("\n✅ Done! The mathematics is the same, Manim just makes prettier videos.")
    print("See INSTALL_GUIDE.md for proper Manim setup with Python 3.11/3.12")
