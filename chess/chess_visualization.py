#!/usr/bin/env python3
"""
Chess Algebra Visualization using Matplotlib
This script creates visual representations of chess algebra concepts.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from chess_board import ChessBoard

def create_chess_board_visualization():
    """Create a visualization of the chess coordinate system."""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create 8x8 grid
    for i in range(8):
        for j in range(8):
            color = 'white' if (i + j) % 2 == 0 else 'gray'
            rect = patches.Rectangle((j, 7-i), 1, 1, linewidth=1, 
                                   edgecolor='black', facecolor=color, alpha=0.7)
            ax.add_patch(rect)
    
    # Add coordinate labels
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ranks = ['8', '7', '6', '5', '4', '3', '2', '1']
    
    for i, file in enumerate(files):
        ax.text(i + 0.5, -0.5, file, ha='center', va='center', fontsize=12, fontweight='bold')
    
    for i, rank in enumerate(ranks):
        ax.text(-0.5, 7 - i + 0.5, rank, ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Highlight e4
    e4_rect = patches.Rectangle((4, 4), 1, 1, linewidth=3, 
                               edgecolor='red', facecolor='yellow', alpha=0.5)
    ax.add_patch(e4_rect)
    ax.text(4.5, 4.5, 'e4', ha='center', va='center', fontsize=14, fontweight='bold')
    
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 9)
    ax.set_aspect('equal')
    ax.set_title('Chess Coordinate System', fontsize=16, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('chess_coordinate_system.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_knight_movement_visualization():
    """Create a visualization of knight movement patterns."""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create 8x8 grid
    for i in range(8):
        for j in range(8):
            color = 'white' if (i + j) % 2 == 0 else 'gray'
            rect = patches.Rectangle((j, 7-i), 1, 1, linewidth=1, 
                                   edgecolor='black', facecolor=color, alpha=0.7)
            ax.add_patch(rect)
    
    # Knight starting position (e4)
    start_pos = (4, 4)
    ax.text(start_pos[0] + 0.5, start_pos[1] + 0.5, '♞', ha='center', va='center', 
            fontsize=20, fontweight='bold')
    
    # Knight moves
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    for dx, dy in knight_moves:
        new_x = start_pos[0] + dx
        new_y = start_pos[1] + dy
        if 0 <= new_x < 8 and 0 <= new_y < 8:
            # Draw arrow
            ax.annotate('', xy=(new_x + 0.5, new_y + 0.5), 
                       xytext=(start_pos[0] + 0.5, start_pos[1] + 0.5),
                       arrowprops=dict(arrowstyle='->', color='red', lw=2))
            # Mark destination
            circle = patches.Circle((new_x + 0.5, new_y + 0.5), 0.3, 
                                  fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(circle)
    
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 9)
    ax.set_aspect('equal')
    ax.set_title('Knight Movement: L-Shaped Vectors', fontsize=16, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('knight_movement.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_bishop_movement_visualization():
    """Create a visualization of bishop movement patterns."""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create 8x8 grid
    for i in range(8):
        for j in range(8):
            color = 'white' if (i + j) % 2 == 0 else 'gray'
            rect = patches.Rectangle((j, 7-i), 1, 1, linewidth=1, 
                                   edgecolor='black', facecolor=color, alpha=0.7)
            ax.add_patch(rect)
    
    # Bishop starting position (e4)
    start_pos = (4, 4)
    ax.text(start_pos[0] + 0.5, start_pos[1] + 0.5, '♝', ha='center', va='center', 
            fontsize=20, fontweight='bold')
    
    # Bishop moves (diagonal)
    for i in range(1, 5):
        for dx, dy in [(i, i), (i, -i), (-i, i), (-i, -i)]:
            new_x = start_pos[0] + dx
            new_y = start_pos[1] + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                # Draw arrow
                ax.annotate('', xy=(new_x + 0.5, new_y + 0.5), 
                           xytext=(start_pos[0] + 0.5, start_pos[1] + 0.5),
                           arrowprops=dict(arrowstyle='->', color='blue', lw=2))
                # Mark destination
                circle = patches.Circle((new_x + 0.5, new_y + 0.5), 0.3, 
                                      fill=False, edgecolor='blue', linewidth=2)
                ax.add_patch(circle)
    
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 9)
    ax.set_aspect('equal')
    ax.set_title('Bishop Movement: Diagonal Vectors', fontsize=16, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('bishop_movement.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_distance_heatmap():
    """Create a heatmap showing distances from e4."""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    board = ChessBoard()
    start_square = "e4"
    start_coords = board.algebraic_to_coordinates(start_square)
    
    # Create distance matrix
    distances = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            square = board.coordinates_to_algebraic(i, j)
            end_coords = board.algebraic_to_coordinates(square)
            dx = end_coords[1] - start_coords[1]
            dy = end_coords[0] - start_coords[0]
            distances[i, j] = np.sqrt(dx**2 + dy**2)
    
    # Create heatmap
    im = ax.imshow(distances, cmap='viridis', aspect='equal')
    
    # Add grid
    ax.set_xticks(np.arange(-0.5, 8, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 8, 1), minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=1)
    
    # Add labels
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ranks = ['8', '7', '6', '5', '4', '3', '2', '1']
    
    ax.set_xticks(range(8))
    ax.set_yticks(range(8))
    ax.set_xticklabels(files)
    ax.set_yticklabels(ranks)
    
    # Add distance values
    for i in range(8):
        for j in range(8):
            text = ax.text(j, i, f'{distances[i, j]:.1f}',
                          ha="center", va="center", color="white", fontweight='bold')
    
    # Highlight e4
    ax.text(start_coords[1], start_coords[0], 'e4', ha='center', va='center', 
            fontsize=14, fontweight='bold', color='red')
    
    plt.colorbar(im, ax=ax, label='Distance from e4')
    ax.set_title('Distance Analysis from e4', fontsize=16, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('distance_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_piece_comparison():
    """Create a comparison of different piece movement patterns."""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    pieces = [
        ('♟', 'Pawn', 'green'),
        ('♞', 'Knight', 'red'),
        ('♝', 'Bishop', 'blue'),
        ('♜', 'Rook', 'orange'),
        ('♛', 'Queen', 'purple'),
        ('♚', 'King', 'brown')
    ]
    
    for idx, (symbol, name, color) in enumerate(pieces):
        ax = axes[idx]
        
        # Create 8x8 grid
        for i in range(8):
            for j in range(8):
                grid_color = 'white' if (i + j) % 2 == 0 else 'gray'
                rect = patches.Rectangle((j, 7-i), 1, 1, linewidth=1, 
                                       edgecolor='black', facecolor=grid_color, alpha=0.7)
                ax.add_patch(rect)
        
        # Add piece at e4
        ax.text(4.5, 4.5, symbol, ha='center', va='center', 
                fontsize=20, fontweight='bold')
        
        # Add sample moves (simplified)
        if name == 'Knight':
            moves = [(2, 1), (2, -1), (-2, 1), (-2, -1)]
        elif name == 'Bishop':
            moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        elif name == 'Rook':
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        elif name == 'Queen':
            moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (1, 0)]
        elif name == 'King':
            moves = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        else:  # Pawn
            moves = [(0, 1)]
        
        for dx, dy in moves:
            new_x = 4 + dx
            new_y = 4 + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                circle = patches.Circle((new_x + 0.5, new_y + 0.5), 0.3, 
                                      fill=False, edgecolor=color, linewidth=2)
                ax.add_patch(circle)
        
        ax.set_xlim(-1, 9)
        ax.set_ylim(-1, 9)
        ax.set_aspect('equal')
        ax.set_title(f'{name}', fontsize=12, fontweight='bold')
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('piece_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Create all visualizations."""
    print("Creating Chess Algebra Visualizations...")
    
    # Set style
    plt.style.use('default')
    plt.rcParams['font.size'] = 10
    
    # Create visualizations
    print("1. Creating coordinate system visualization...")
    create_chess_board_visualization()
    
    print("2. Creating knight movement visualization...")
    create_knight_movement_visualization()
    
    print("3. Creating bishop movement visualization...")
    create_bishop_movement_visualization()
    
    print("4. Creating distance heatmap...")
    create_distance_heatmap()
    
    print("5. Creating piece comparison...")
    create_piece_comparison()
    
    print("\nAll visualizations created successfully!")
    print("Files saved:")
    print("- chess_coordinate_system.png")
    print("- knight_movement.png")
    print("- bishop_movement.png")
    print("- distance_heatmap.png")
    print("- piece_comparison.png")

if __name__ == "__main__":
    main() 