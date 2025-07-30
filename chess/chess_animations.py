#!/usr/bin/env python3
"""
Chess Algebra Animations using Matplotlib
This script creates animated visualizations of chess algebra concepts.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from chess_board import ChessBoard

def create_animated_coordinate_system():
    """Create an animated chess coordinate system."""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create 8x8 grid
    squares = []
    for i in range(8):
        for j in range(8):
            color = 'white' if (i + j) % 2 == 0 else 'gray'
            rect = patches.Rectangle((j, 7-i), 1, 1, linewidth=1, 
                                   edgecolor='black', facecolor=color, alpha=0.7)
            ax.add_patch(rect)
            squares.append(rect)
    
    # Add coordinate labels
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ranks = ['8', '7', '6', '5', '4', '3', '2', '1']
    
    for i, file in enumerate(files):
        ax.text(i + 0.5, -0.5, file, ha='center', va='center', fontsize=12, fontweight='bold')
    
    for i, rank in enumerate(ranks):
        ax.text(-0.5, 7 - i + 0.5, rank, ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Highlight e4 with animation
    e4_rect = patches.Rectangle((4, 4), 1, 1, linewidth=3, 
                               edgecolor='red', facecolor='yellow', alpha=0.5)
    ax.add_patch(e4_rect)
    e4_text = ax.text(4.5, 4.5, 'e4', ha='center', va='center', fontsize=14, fontweight='bold')
    
    # Animation function
    def animate(frame):
        # Pulse the e4 square
        alpha = 0.3 + 0.4 * np.sin(frame * 0.2)
        e4_rect.set_alpha(alpha)
        e4_text.set_alpha(alpha)
        return e4_rect, e4_text
    
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 9)
    ax.set_aspect('equal')
    ax.set_title('Chess Coordinate System (Animated)', fontsize=16, fontweight='bold')
    ax.axis('off')
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
    anim.save('chess_coordinate_system_animated.gif', writer='pillow', fps=20)
    plt.show()
    
    return anim

def create_animated_knight_movement():
    """Create an animated knight movement visualization."""
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
    knight_text = ax.text(start_pos[0] + 0.5, start_pos[1] + 0.5, '♞', ha='center', va='center', 
                         fontsize=20, fontweight='bold')
    
    # Knight moves
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    # Create arrows and circles for each move
    arrows = []
    circles = []
    for dx, dy in knight_moves:
        new_x = start_pos[0] + dx
        new_y = start_pos[1] + dy
        if 0 <= new_x < 8 and 0 <= new_y < 8:
            arrow = ax.annotate('', xy=(new_x + 0.5, new_y + 0.5), 
                               xytext=(start_pos[0] + 0.5, start_pos[1] + 0.5),
                               arrowprops=dict(arrowstyle='->', color='red', lw=2))
            arrows.append(arrow)
            
            circle = patches.Circle((new_x + 0.5, new_y + 0.5), 0.3, 
                                  fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(circle)
            circles.append(circle)
    
    # Animation function
    def animate(frame):
        # Animate arrows appearing one by one
        for i, arrow in enumerate(arrows):
            if frame >= i * 10:  # Show arrow i after frame i*10
                arrow.set_alpha(1.0)
            else:
                arrow.set_alpha(0.0)
        
        # Animate circles appearing one by one
        for i, circle in enumerate(circles):
            if frame >= i * 10 + 5:  # Show circle i after frame i*10+5
                circle.set_alpha(1.0)
            else:
                circle.set_alpha(0.0)
        
        return arrows + circles
    
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 9)
    ax.set_aspect('equal')
    ax.set_title('Knight Movement: L-Shaped Vectors (Animated)', fontsize=16, fontweight='bold')
    ax.axis('off')
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=100, interval=100, blit=False)
    anim.save('knight_movement_animated.gif', writer='pillow', fps=10)
    plt.show()
    
    return anim

def create_animated_bishop_movement():
    """Create an animated bishop movement visualization."""
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
    bishop_text = ax.text(start_pos[0] + 0.5, start_pos[1] + 0.5, '♝', ha='center', va='center', 
                         fontsize=20, fontweight='bold')
    
    # Bishop moves (diagonal)
    arrows = []
    circles = []
    move_idx = 0
    
    for i in range(1, 5):
        for dx, dy in [(i, i), (i, -i), (-i, i), (-i, -i)]:
            new_x = start_pos[0] + dx
            new_y = start_pos[1] + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                arrow = ax.annotate('', xy=(new_x + 0.5, new_y + 0.5), 
                                   xytext=(start_pos[0] + 0.5, start_pos[1] + 0.5),
                                   arrowprops=dict(arrowstyle='->', color='blue', lw=2))
                arrows.append(arrow)
                
                circle = patches.Circle((new_x + 0.5, new_y + 0.5), 0.3, 
                                      fill=False, edgecolor='blue', linewidth=2)
                ax.add_patch(circle)
                circles.append(circle)
                move_idx += 1
    
    # Animation function
    def animate(frame):
        # Animate arrows appearing one by one
        for i, arrow in enumerate(arrows):
            if frame >= i * 5:  # Show arrow i after frame i*5
                arrow.set_alpha(1.0)
            else:
                arrow.set_alpha(0.0)
        
        # Animate circles appearing one by one
        for i, circle in enumerate(circles):
            if frame >= i * 5 + 3:  # Show circle i after frame i*5+3
                circle.set_alpha(1.0)
            else:
                circle.set_alpha(0.0)
        
        return arrows + circles
    
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 9)
    ax.set_aspect('equal')
    ax.set_title('Bishop Movement: Diagonal Vectors (Animated)', fontsize=16, fontweight='bold')
    ax.axis('off')
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=80, interval=100, blit=False)
    anim.save('bishop_movement_animated.gif', writer='pillow', fps=10)
    plt.show()
    
    return anim

def create_animated_distance_heatmap():
    """Create an animated distance heatmap."""
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
    
    # Add labels
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ranks = ['8', '7', '6', '5', '4', '3', '2', '1']
    
    ax.set_xticks(range(8))
    ax.set_yticks(range(8))
    ax.set_xticklabels(files)
    ax.set_yticklabels(ranks)
    
    # Highlight e4
    e4_text = ax.text(start_coords[1], start_coords[0], 'e4', ha='center', va='center', 
                      fontsize=14, fontweight='bold', color='red')
    
    # Animation function
    def animate(frame):
        # Gradually reveal the heatmap
        revealed_distances = distances * (frame / 50.0)  # Reveal over 50 frames
        
        # Clear previous image
        ax.clear()
        
        # Recreate the heatmap
        im = ax.imshow(revealed_distances, cmap='viridis', aspect='equal')
        
        # Add grid
        ax.set_xticks(np.arange(-0.5, 8, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, 8, 1), minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=1)
        
        # Add labels
        ax.set_xticks(range(8))
        ax.set_yticks(range(8))
        ax.set_xticklabels(files)
        ax.set_yticklabels(ranks)
        
        # Add distance values
        for i in range(8):
            for j in range(8):
                if revealed_distances[i, j] > 0:
                    ax.text(j, i, f'{distances[i, j]:.1f}',
                           ha="center", va="center", color="white", fontweight='bold')
        
        # Re-add e4 highlight
        ax.text(start_coords[1], start_coords[0], 'e4', ha='center', va='center', 
                fontsize=14, fontweight='bold', color='red')
        
        ax.set_title('Distance Analysis from e4 (Animated)', fontsize=16, fontweight='bold')
        
        return [im]
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=60, interval=100, blit=False)
    anim.save('distance_heatmap_animated.gif', writer='pillow', fps=10)
    plt.show()
    
    return anim

def create_animated_piece_comparison():
    """Create an animated piece comparison."""
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
    
    # Store all elements for animation
    all_elements = []
    
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
        piece_text = ax.text(4.5, 4.5, symbol, ha='center', va='center', 
                            fontsize=20, fontweight='bold')
        
        # Add sample moves (simplified)
        moves = []
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
        
        circles = []
        for dx, dy in moves:
            new_x = 4 + dx
            new_y = 4 + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                circle = patches.Circle((new_x + 0.5, new_y + 0.5), 0.3, 
                                      fill=False, edgecolor=color, linewidth=2)
                ax.add_patch(circle)
                circles.append(circle)
        
        ax.set_xlim(-1, 9)
        ax.set_ylim(-1, 9)
        ax.set_aspect('equal')
        ax.set_title(f'{name}', fontsize=12, fontweight='bold')
        ax.axis('off')
        
        all_elements.append((piece_text, circles))
    
    # Animation function
    def animate(frame):
        # Animate pieces appearing one by one
        for i, (piece_text, circles) in enumerate(all_elements):
            if frame >= i * 15:  # Show piece i after frame i*15
                piece_text.set_alpha(1.0)
                for circle in circles:
                    circle.set_alpha(1.0)
            else:
                piece_text.set_alpha(0.0)
                for circle in circles:
                    circle.set_alpha(0.0)
        
        return [piece for piece_text, circles in all_elements for piece in [piece_text] + circles]
    
    plt.tight_layout()
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=120, interval=100, blit=False)
    anim.save('piece_comparison_animated.gif', writer='pillow', fps=10)
    plt.show()
    
    return anim

def create_animated_vector_analysis():
    """Create an animated vector analysis demonstration."""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create coordinate system
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    # Draw coordinate axes
    ax.axhline(y=0, color='k', alpha=0.5)
    ax.axvline(x=0, color='k', alpha=0.5)
    
    # Vector data
    vectors = [
        ((0, 0), (1, 1), 'Knight: (1,1)', 'red'),
        ((0, 0), (2, 1), 'Knight: (2,1)', 'red'),
        ((0, 0), (1, 2), 'Knight: (1,2)', 'red'),
        ((0, 0), (2, 2), 'Bishop: (2,2)', 'blue'),
        ((0, 0), (3, 3), 'Bishop: (3,3)', 'blue'),
        ((0, 0), (1, 0), 'Rook: (1,0)', 'green'),
        ((0, 0), (0, 1), 'Rook: (0,1)', 'green'),
    ]
    
    arrows = []
    texts = []
    
    for start, end, label, color in vectors:
        arrow = ax.annotate('', xy=end, xytext=start,
                           arrowprops=dict(arrowstyle='->', color=color, lw=2))
        arrows.append(arrow)
        
        text = ax.text(end[0] + 0.2, end[1] + 0.2, label, fontsize=8, color=color)
        texts.append(text)
    
    # Animation function
    def animate(frame):
        # Animate arrows appearing one by one
        for i, (arrow, text) in enumerate(zip(arrows, texts)):
            if frame >= i * 10:  # Show arrow i after frame i*10
                arrow.set_alpha(1.0)
                text.set_alpha(1.0)
            else:
                arrow.set_alpha(0.0)
                text.set_alpha(0.0)
        
        return arrows + texts
    
    ax.set_title('Chess Vector Analysis (Animated)', fontsize=16, fontweight='bold')
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=80, interval=100, blit=False)
    anim.save('vector_analysis_animated.gif', writer='pillow', fps=10)
    plt.show()
    
    return anim

def main():
    """Create all animated visualizations."""
    print("Creating Animated Chess Algebra Visualizations...")
    
    # Set style
    plt.style.use('default')
    plt.rcParams['font.size'] = 10
    
    # Create animations
    print("1. Creating animated coordinate system...")
    create_animated_coordinate_system()
    
    print("2. Creating animated knight movement...")
    create_animated_knight_movement()
    
    print("3. Creating animated bishop movement...")
    create_animated_bishop_movement()
    
    print("4. Creating animated distance heatmap...")
    create_animated_distance_heatmap()
    
    print("5. Creating animated piece comparison...")
    create_animated_piece_comparison()
    
    print("6. Creating animated vector analysis...")
    create_animated_vector_analysis()
    
    print("\nAll animated visualizations created successfully!")
    print("Files saved:")
    print("- chess_coordinate_system_animated.gif")
    print("- knight_movement_animated.gif")
    print("- bishop_movement_animated.gif")
    print("- distance_heatmap_animated.gif")
    print("- piece_comparison_animated.gif")
    print("- vector_analysis_animated.gif")

if __name__ == "__main__":
    main() 