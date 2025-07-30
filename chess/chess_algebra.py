from manim import *
import numpy as np
from chess_board import ChessBoard

class ChessAlgebraScene(Scene):
    """Main scene explaining chess using algebra and mathematics."""
    
    def construct(self):
        self.chess_board = ChessBoard()
        self.setup_scene()
        self.introduction()
        self.coordinate_system()
        self.piece_movement_vectors()
        self.knight_mathematics()
        self.bishop_diagonals()
        self.queen_combinations()
        self.distance_analysis()
        self.conclusion()
    
    def setup_scene(self):
        """Setup the scene with title and basic elements."""
        title = Text("Chess as Algebra", font_size=48, color=BLUE)
        subtitle = Text("Mathematical Analysis of Chess", font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def introduction(self):
        """Introduction to chess as a mathematical system."""
        intro_text = VGroup(
            Text("Chess as a Mathematical System", font_size=36, color=WHITE),
            Text("• 8×8 coordinate grid", font_size=24, color=YELLOW),
            Text("• Vector-based piece movements", font_size=24, color=YELLOW),
            Text("• Algebraic notation system", font_size=24, color=YELLOW),
            Text("• Distance and position analysis", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))
    
    def coordinate_system(self):
        """Demonstrate the coordinate system and algebraic notation."""
        # Create coordinate grid
        grid = NumberPlane(
            x_range=[0, 8, 1],
            y_range=[0, 8, 1],
            x_length=6,
            y_length=6,
            background_line_style={
                "stroke_opacity": 0.6,
                "stroke_width": 1
            }
        )
        
        # Add coordinate labels
        file_labels = VGroup(*[
            Text(f, font_size=16, color=WHITE).move_to(grid.c2p(i + 0.5, -0.5))
            for i, f in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        ])
        
        rank_labels = VGroup(*[
            Text(r, font_size=16, color=WHITE).move_to(grid.c2p(-0.5, i + 0.5))
            for i, r in enumerate(['8', '7', '6', '5', '4', '3', '2', '1'])
        ])
        
        title = Text("Chess Coordinate System", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        self.play(Write(title))
        self.play(Create(grid))
        self.play(Write(file_labels), Write(rank_labels))
        
        # Highlight specific squares
        e4_square = Square(side_length=0.7, color=YELLOW, fill_opacity=0.3)
        e4_square.move_to(grid.c2p(4.5, 3.5))
        
        e4_label = Text("e4", font_size=20, color=YELLOW)
        e4_label.next_to(e4_square, UP)
        
        self.play(Create(e4_square), Write(e4_label))
        self.wait(1)
        
        # Show coordinate conversion
        coord_text = Text("e4 → (3, 4)", font_size=24, color=GREEN)
        coord_text.next_to(grid, DOWN)
        self.play(Write(coord_text))
        self.wait(2)
        
        self.play(FadeOut(grid), FadeOut(file_labels), FadeOut(rank_labels),
                  FadeOut(e4_square), FadeOut(e4_label), FadeOut(coord_text),
                  FadeOut(title))
    
    def piece_movement_vectors(self):
        """Show piece movements as vectors."""
        title = Text("Piece Movement Vectors", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create a simplified board
        board = VGroup()
        for i in range(8):
            for j in range(8):
                color = WHITE if (i + j) % 2 == 0 else GRAY
                square = Square(side_length=0.5, fill_color=color, fill_opacity=0.3)
                square.move_to([j * 0.6 - 2.1, i * 0.6 - 2.1, 0])
                board.add(square)
        
        self.play(Write(title))
        self.play(Create(board))
        
        # Show pawn movement vector
        pawn_start = board[4 * 8 + 3]  # e2
        pawn_end = board[3 * 8 + 3]    # e4
        
        pawn_vector = Arrow(
            pawn_start.get_center(),
            pawn_end.get_center(),
            color=YELLOW,
            buff=0.1
        )
        
        pawn_label = Text("Pawn: (0, -1)", font_size=16, color=YELLOW)
        pawn_label.next_to(pawn_vector, RIGHT)
        
        self.play(Create(pawn_vector), Write(pawn_label))
        self.wait(1)
        
        # Show rook movement vectors
        rook_vectors = VGroup()
        rook_labels = VGroup()
        
        for i in range(8):
            if i != 3:  # Not the same file
                start_pos = board[4 * 8 + 3].get_center()
                end_pos = board[i * 8 + 3].get_center()
                vector = Arrow(start_pos, end_pos, color=RED, buff=0.1)
                rook_vectors.add(vector)
                
                label = Text(f"({i-4}, 0)", font_size=12, color=RED)
                label.next_to(vector, RIGHT)
                rook_labels.add(label)
        
        self.play(Create(rook_vectors), Write(rook_labels))
        self.wait(1)
        
        self.play(FadeOut(board), FadeOut(pawn_vector), FadeOut(pawn_label),
                  FadeOut(rook_vectors), FadeOut(rook_labels), FadeOut(title))
    
    def knight_mathematics(self):
        """Demonstrate knight movement using L-shaped vectors."""
        title = Text("Knight Movement: L-Shaped Vectors", font_size=28, color=BLUE)
        title.to_edge(UP)
        
        # Create coordinate system for knight moves
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE}
        )
        
        # Show knight move vectors
        knight_moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        
        vectors = VGroup()
        labels = VGroup()
        
        for dx, dy in knight_moves:
            vector = Arrow(
                ORIGIN,
                [dx * 0.5, dy * 0.5, 0],
                color=GREEN,
                buff=0.1
            )
            vectors.add(vector)
            
            label = Text(f"({dx}, {dy})", font_size=12, color=GREEN)
            label.next_to(vector.get_end(), RIGHT)
            labels.add(label)
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Create(vectors), Write(labels))
        
        # Show mathematical property
        math_text = Text("All knight moves: |dx| + |dy| = 3", font_size=20, color=YELLOW)
        math_text.next_to(axes, DOWN)
        self.play(Write(math_text))
        self.wait(2)
        
        self.play(FadeOut(axes), FadeOut(vectors), FadeOut(labels),
                  FadeOut(math_text), FadeOut(title))
    
    def bishop_diagonals(self):
        """Show bishop movement using diagonal vectors."""
        title = Text("Bishop: Diagonal Vectors", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create a larger coordinate system
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            axis_config={"color": WHITE}
        )
        
        # Show diagonal vectors
        diagonal_vectors = VGroup()
        for i in range(1, 5):
            # Positive diagonal
            pos_vector = Arrow(
                ORIGIN,
                [i * 0.5, i * 0.5, 0],
                color=RED,
                buff=0.1
            )
            diagonal_vectors.add(pos_vector)
            
            # Negative diagonal
            neg_vector = Arrow(
                ORIGIN,
                [i * 0.5, -i * 0.5, 0],
                color=BLUE,
                buff=0.1
            )
            diagonal_vectors.add(neg_vector)
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Create(diagonal_vectors))
        
        # Show mathematical property
        math_text = Text("Bishop moves: |dx| = |dy|", font_size=20, color=YELLOW)
        math_text.next_to(axes, DOWN)
        self.play(Write(math_text))
        self.wait(2)
        
        self.play(FadeOut(axes), FadeOut(diagonal_vectors),
                  FadeOut(math_text), FadeOut(title))
    
    def queen_combinations(self):
        """Show queen movement as combination of rook and bishop."""
        title = Text("Queen: Rook + Bishop", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE}
        )
        
        # Show rook moves (horizontal and vertical)
        rook_vectors = VGroup()
        for i in range(-3, 4):
            if i != 0:
                # Horizontal
                h_vector = Arrow(ORIGIN, [i * 0.5, 0, 0], color=RED, buff=0.1)
                rook_vectors.add(h_vector)
                # Vertical
                v_vector = Arrow(ORIGIN, [0, i * 0.5, 0], color=RED, buff=0.1)
                rook_vectors.add(v_vector)
        
        # Show bishop moves (diagonal)
        bishop_vectors = VGroup()
        for i in range(1, 4):
            # Positive diagonal
            pos_vector = Arrow(ORIGIN, [i * 0.5, i * 0.5, 0], color=BLUE, buff=0.1)
            bishop_vectors.add(pos_vector)
            # Negative diagonal
            neg_vector = Arrow(ORIGIN, [i * 0.5, -i * 0.5, 0], color=BLUE, buff=0.1)
            bishop_vectors.add(neg_vector)
        
        self.play(Write(title))
        self.play(Create(axes))
        
        # Show rook moves first
        rook_label = Text("Rook moves", font_size=16, color=RED)
        rook_label.next_to(axes, DOWN)
        self.play(Create(rook_vectors), Write(rook_label))
        self.wait(1)
        
        # Show bishop moves
        bishop_label = Text("+ Bishop moves", font_size=16, color=BLUE)
        bishop_label.next_to(rook_label, DOWN)
        self.play(Create(bishop_vectors), Write(bishop_label))
        self.wait(1)
        
        # Show combined
        combined_label = Text("= Queen moves", font_size=16, color=GREEN)
        combined_label.next_to(bishop_label, DOWN)
        self.play(Write(combined_label))
        self.wait(2)
        
        self.play(FadeOut(axes), FadeOut(rook_vectors), FadeOut(bishop_vectors),
                  FadeOut(rook_label), FadeOut(bishop_label), FadeOut(combined_label),
                  FadeOut(title))
    
    def distance_analysis(self):
        """Show distance analysis between squares."""
        title = Text("Distance Analysis", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create a heatmap of distances from e4
        board = VGroup()
        distances = []
        
        for i in range(8):
            for j in range(8):
                # Calculate distance from e4 (3, 4)
                distance = np.sqrt((i - 3)**2 + (j - 4)**2)
                distances.append(distance)
                
                # Color based on distance
                if distance == 0:
                    color = YELLOW
                elif distance <= 1:
                    color = GREEN
                elif distance <= 2:
                    color = BLUE
                elif distance <= 3:
                    color = RED
                else:
                    color = GRAY
                
                square = Square(side_length=0.4, fill_color=color, fill_opacity=0.6)
                square.move_to([j * 0.5 - 1.75, i * 0.5 - 1.75, 0])
                board.add(square)
        
        # Add distance labels
        labels = VGroup()
        for i in range(8):
            for j in range(8):
                distance = distances[i * 8 + j]
                if distance > 0:
                    label = Text(f"{distance:.1f}", font_size=8, color=WHITE)
                    label.move_to([j * 0.5 - 1.75, i * 0.5 - 1.75, 0])
                    labels.add(label)
        
        self.play(Write(title))
        self.play(Create(board))
        self.play(Write(labels))
        
        # Show mathematical formula
        formula = MathTex(r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}", font_size=24)
        formula.next_to(board, DOWN)
        self.play(Write(formula))
        self.wait(2)
        
        self.play(FadeOut(board), FadeOut(labels), FadeOut(formula), FadeOut(title))
    
    def conclusion(self):
        """Conclude with key mathematical concepts."""
        conclusion_text = VGroup(
            Text("Chess as Algebra: Key Concepts", font_size=32, color=BLUE),
            Text("• Coordinate system: (file, rank)", font_size=20, color=WHITE),
            Text("• Vector movements: (dx, dy)", font_size=20, color=WHITE),
            Text("• Distance metrics: Euclidean geometry", font_size=20, color=WHITE),
            Text("• Piece-specific movement patterns", font_size=20, color=WHITE),
            Text("• Algebraic notation: e4, Nf3, O-O", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        self.play(Write(conclusion_text))
        self.wait(3)
        self.play(FadeOut(conclusion_text))


class PieceMovementAnalysis(Scene):
    """Detailed analysis of piece movements using vectors."""
    
    def construct(self):
        self.chess_board = ChessBoard()
        self.analyze_pawn_movement()
        self.analyze_knight_movement()
        self.analyze_bishop_movement()
        self.analyze_rook_movement()
        self.analyze_queen_movement()
        self.analyze_king_movement()
    
    def analyze_pawn_movement(self):
        """Analyze pawn movement patterns."""
        title = Text("Pawn Movement Analysis", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-1, 1, 0.5],
            y_range=[0, 2, 0.5],
            x_length=4,
            y_length=4,
            axis_config={"color": WHITE}
        )
        
        # Show pawn movement vectors
        pawn_vectors = VGroup()
        
        # Forward move
        forward = Arrow([0, 0, 0], [0, 1, 0], color=GREEN, buff=0.1)
        pawn_vectors.add(forward)
        
        # Initial two-square move
        double = Arrow([0, 0, 0], [0, 2, 0], color=YELLOW, buff=0.1)
        pawn_vectors.add(double)
        
        # Diagonal captures (if applicable)
        left_capture = Arrow([0, 0, 0], [-0.5, 1, 0], color=RED, buff=0.1)
        right_capture = Arrow([0, 0, 0], [0.5, 1, 0], color=RED, buff=0.1)
        pawn_vectors.add(left_capture, right_capture)
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Create(pawn_vectors))
        
        # Add labels
        labels = VGroup(
            Text("Forward: (0, 1)", font_size=12, color=GREEN),
            Text("Double: (0, 2)", font_size=12, color=YELLOW),
            Text("Capture: (±1, 1)", font_size=12, color=RED)
        )
        
        for i, label in enumerate(labels):
            label.next_to(pawn_vectors[i], RIGHT)
        
        self.play(Write(labels))
        self.wait(2)
        
        self.play(FadeOut(axes), FadeOut(pawn_vectors), FadeOut(labels), FadeOut(title))
    
    def analyze_knight_movement(self):
        """Analyze knight movement using L-shaped patterns."""
        title = Text("Knight: L-Shaped Movement", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE}
        )
        
        # Show all knight moves
        knight_moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        
        vectors = VGroup()
        for dx, dy in knight_moves:
            vector = Arrow(ORIGIN, [dx * 0.3, dy * 0.3, 0], color=GREEN, buff=0.1)
            vectors.add(vector)
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Create(vectors))
        
        # Show mathematical property
        math_text = MathTex(r"|dx| + |dy| = 3", font_size=24, color=YELLOW)
        math_text.next_to(axes, DOWN)
        self.play(Write(math_text))
        self.wait(2)
        
        self.play(FadeOut(axes), FadeOut(vectors), FadeOut(math_text), FadeOut(title))
    
    def analyze_bishop_movement(self):
        """Analyze bishop diagonal movement."""
        title = Text("Bishop: Diagonal Movement", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            axis_config={"color": WHITE}
        )
        
        # Show diagonal vectors
        diagonal_vectors = VGroup()
        for i in range(1, 5):
            # All four diagonals
            vectors = [
                Arrow(ORIGIN, [i * 0.4, i * 0.4, 0], color=RED, buff=0.1),
                Arrow(ORIGIN, [i * 0.4, -i * 0.4, 0], color=BLUE, buff=0.1),
                Arrow(ORIGIN, [-i * 0.4, i * 0.4, 0], color=GREEN, buff=0.1),
                Arrow(ORIGIN, [-i * 0.4, -i * 0.4, 0], color=YELLOW, buff=0.1)
            ]
            diagonal_vectors.add(*vectors)
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Create(diagonal_vectors))
        
        # Show mathematical property
        math_text = MathTex(r"|dx| = |dy|", font_size=24, color=WHITE)
        math_text.next_to(axes, DOWN)
        self.play(Write(math_text))
        self.wait(2)
        
        self.play(FadeOut(axes), FadeOut(diagonal_vectors), FadeOut(math_text), FadeOut(title))
    
    def analyze_rook_movement(self):
        """Analyze rook horizontal and vertical movement."""
        title = Text("Rook: Horizontal & Vertical", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            axis_config={"color": WHITE}
        )
        
        # Show rook movement vectors
        rook_vectors = VGroup()
        
        # Horizontal moves
        for i in range(-4, 5):
            if i != 0:
                vector = Arrow(ORIGIN, [i * 0.4, 0, 0], color=RED, buff=0.1)
                rook_vectors.add(vector)
        
        # Vertical moves
        for i in range(-4, 5):
            if i != 0:
                vector = Arrow(ORIGIN, [0, i * 0.4, 0], color=BLUE, buff=0.1)
                rook_vectors.add(vector)
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Create(rook_vectors))
        
        # Show mathematical property
        math_text = MathTex(r"dx = 0 \text{ or } dy = 0", font_size=24, color=WHITE)
        math_text.next_to(axes, DOWN)
        self.play(Write(math_text))
        self.wait(2)
        
        self.play(FadeOut(axes), FadeOut(rook_vectors), FadeOut(math_text), FadeOut(title))
    
    def analyze_queen_movement(self):
        """Analyze queen as combination of rook and bishop."""
        title = Text("Queen: Rook + Bishop", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE}
        )
        
        # Show queen movement vectors
        queen_vectors = VGroup()
        
        # Add all possible queen moves
        for i in range(-3, 4):
            for j in range(-3, 4):
                if i != 0 or j != 0:  # Not the origin
                    vector = Arrow(ORIGIN, [i * 0.3, j * 0.3, 0], color=GREEN, buff=0.1)
                    queen_vectors.add(vector)
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Create(queen_vectors))
        
        # Show mathematical property
        math_text = MathTex(r"|dx| = |dy| \text{ or } dx = 0 \text{ or } dy = 0", font_size=20, color=WHITE)
        math_text.next_to(axes, DOWN)
        self.play(Write(math_text))
        self.wait(2)
        
        self.play(FadeOut(axes), FadeOut(queen_vectors), FadeOut(math_text), FadeOut(title))
    
    def analyze_king_movement(self):
        """Analyze king movement as one square in any direction."""
        title = Text("King: One Square in Any Direction", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": WHITE}
        )
        
        # Show king movement vectors
        king_vectors = VGroup()
        
        # All 8 possible king moves
        king_moves = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        
        for dx, dy in king_moves:
            vector = Arrow(ORIGIN, [dx * 0.4, dy * 0.4, 0], color=YELLOW, buff=0.1)
            king_vectors.add(vector)
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Create(king_vectors))
        
        # Show mathematical property
        math_text = MathTex(r"|dx| \leq 1 \text{ and } |dy| \leq 1", font_size=24, color=WHITE)
        math_text.next_to(axes, DOWN)
        self.play(Write(math_text))
        self.wait(2)
        
        self.play(FadeOut(axes), FadeOut(king_vectors), FadeOut(math_text), FadeOut(title)) 