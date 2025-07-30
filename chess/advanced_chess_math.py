from manim import *
import numpy as np
from chess_board import ChessBoard

class AdvancedChessMathematics(Scene):
    """Advanced mathematical analysis of chess concepts."""
    
    def construct(self):
        self.chess_board = ChessBoard()
        self.game_theory_analysis()
        self.probability_analysis()
        self.optimization_analysis()
        self.graph_theory_analysis()
        self.conclusion()
    
    def game_theory_analysis(self):
        """Analyze chess from a game theory perspective."""
        title = Text("Chess as Game Theory", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create payoff matrix for a simple chess position
        matrix_data = [
            ["", "White: e4", "White: d4", "White: Nf3"],
            ["Black: e5", "0.5", "0.6", "0.4"],
            ["Black: d5", "0.4", "0.5", "0.6"],
            ["Black: Nf6", "0.6", "0.4", "0.5"]
        ]
        
        # Create the payoff matrix
        matrix = VGroup()
        for i, row in enumerate(matrix_data):
            row_group = VGroup()
            for j, cell in enumerate(row):
                if i == 0 or j == 0:
                    color = YELLOW
                else:
                    color = WHITE
                cell_text = Text(cell, font_size=16, color=color)
                row_group.add(cell_text)
            row_group.arrange(RIGHT, buff=0.3)
            matrix.add(row_group)
        
        matrix.arrange(DOWN, buff=0.2)
        matrix.move_to(ORIGIN)
        
        self.play(Write(title))
        self.play(Create(matrix))
        
        # Show Nash equilibrium
        equilibrium_text = Text("Nash Equilibrium: Both players choose optimal strategies", 
                              font_size=20, color=GREEN)
        equilibrium_text.next_to(matrix, DOWN)
        self.play(Write(equilibrium_text))
        self.wait(2)
        
        self.play(FadeOut(matrix), FadeOut(equilibrium_text), FadeOut(title))
    
    def probability_analysis(self):
        """Analyze probability in chess positions."""
        title = Text("Probability in Chess", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create a probability distribution for piece values
        piece_values = {
            "Pawn": 1,
            "Knight": 3,
            "Bishop": 3,
            "Rook": 5,
            "Queen": 9,
            "King": 100
        }
        
        # Create bar chart
        bars = VGroup()
        labels = VGroup()
        
        for i, (piece, value) in enumerate(piece_values.items()):
            bar = Rectangle(
                width=0.8,
                height=value * 0.1,
                fill_color=BLUE,
                fill_opacity=0.7
            )
            bar.move_to([i * 1.2 - 3, value * 0.05, 0])
            bars.add(bar)
            
            label = Text(piece, font_size=12, color=WHITE)
            label.next_to(bar, DOWN)
            labels.add(label)
            
            value_text = Text(str(value), font_size=10, color=YELLOW)
            value_text.next_to(bar, UP)
            labels.add(value_text)
        
        # Create axes
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 110, 20],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE}
        )
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Create(bars), Write(labels))
        
        # Show expected value calculation
        expected_value_text = Text("Expected Value = Σ(Probability × Value)", 
                                 font_size=18, color=GREEN)
        expected_value_text.next_to(axes, DOWN)
        self.play(Write(expected_value_text))
        self.wait(2)
        
        self.play(FadeOut(axes), FadeOut(bars), FadeOut(labels), 
                  FadeOut(expected_value_text), FadeOut(title))
    
    def optimization_analysis(self):
        """Analyze optimization problems in chess."""
        title = Text("Optimization in Chess", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create a simple optimization problem
        problem_text = VGroup(
            Text("Chess Optimization Problem:", font_size=20, color=WHITE),
            Text("Maximize: Control of center squares", font_size=16, color=YELLOW),
            Text("Subject to: Piece movement constraints", font_size=16, color=YELLOW),
            Text("Variables: Piece positions", font_size=16, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        # Create a simple chess position
        board = VGroup()
        for i in range(8):
            for j in range(8):
                color = WHITE if (i + j) % 2 == 0 else GRAY
                square = Square(side_length=0.4, fill_color=color, fill_opacity=0.3)
                square.move_to([j * 0.5 - 1.75, i * 0.5 - 1.75, 0])
                board.add(square)
        
        # Add pieces
        pieces = VGroup()
        piece_positions = [
            (3, 3, "♔"), (3, 4, "♕"), (4, 3, "♖"), (4, 4, "♗")
        ]
        
        for row, col, piece in piece_positions:
            piece_text = Text(piece, font_size=24, color=BLACK)
            piece_text.move_to([col * 0.5 - 1.75, row * 0.5 - 1.75, 0])
            pieces.add(piece_text)
        
        self.play(Write(title))
        self.play(Write(problem_text))
        self.play(Create(board))
        self.play(Create(pieces))
        
        # Show optimization objective
        objective_text = Text("Objective: Maximize center control", font_size=18, color=GREEN)
        objective_text.next_to(board, DOWN)
        self.play(Write(objective_text))
        self.wait(2)
        
        self.play(FadeOut(board), FadeOut(pieces), FadeOut(problem_text),
                  FadeOut(objective_text), FadeOut(title))
    
    def graph_theory_analysis(self):
        """Analyze chess using graph theory concepts."""
        title = Text("Chess as a Graph", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create a graph representation of chess moves
        vertices = VGroup()
        edges = VGroup()
        
        # Create vertices (squares)
        for i in range(4):
            for j in range(4):
                vertex = Circle(radius=0.1, fill_color=BLUE, fill_opacity=0.7)
                vertex.move_to([j * 1.5 - 2.25, i * 1.5 - 2.25, 0])
                vertices.add(vertex)
                
                # Add labels
                label = Text(f"({i},{j})", font_size=10, color=WHITE)
                label.next_to(vertex, UP)
                vertices.add(label)
        
        # Create edges (possible moves)
        move_connections = [
            (0, 0, 1, 1), (0, 0, 1, 0), (0, 0, 0, 1),
            (1, 1, 2, 2), (1, 1, 1, 2), (1, 1, 2, 1),
            (2, 2, 3, 3), (2, 2, 2, 3), (2, 2, 3, 2),
            (0, 1, 1, 2), (1, 0, 2, 1), (1, 2, 2, 3), (2, 1, 3, 2)
        ]
        
        for start_i, start_j, end_i, end_j in move_connections:
            start_pos = [start_j * 1.5 - 2.25, start_i * 1.5 - 2.25, 0]
            end_pos = [end_j * 1.5 - 2.25, end_i * 1.5 - 2.25, 0]
            
            edge = Line(start_pos, end_pos, color=RED, stroke_width=2)
            edges.add(edge)
        
        self.play(Write(title))
        self.play(Create(vertices))
        self.play(Create(edges))
        
        # Show graph properties
        properties_text = VGroup(
            Text("Graph Properties:", font_size=18, color=WHITE),
            Text("• Vertices = Chess squares", font_size=14, color=YELLOW),
            Text("• Edges = Possible moves", font_size=14, color=YELLOW),
            Text("• Path length = Move sequence", font_size=14, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT)
        properties_text.next_to(vertices, DOWN)
        
        self.play(Write(properties_text))
        self.wait(2)
        
        self.play(FadeOut(vertices), FadeOut(edges), FadeOut(properties_text), FadeOut(title))
    
    def conclusion(self):
        """Conclude with advanced mathematical concepts."""
        conclusion_text = VGroup(
            Text("Advanced Chess Mathematics", font_size=32, color=BLUE),
            Text("• Game Theory: Strategic decision making", font_size=18, color=WHITE),
            Text("• Probability: Position evaluation", font_size=18, color=WHITE),
            Text("• Optimization: Best move selection", font_size=18, color=WHITE),
            Text("• Graph Theory: Move connectivity", font_size=18, color=WHITE),
            Text("• Linear Algebra: Position vectors", font_size=18, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        self.play(Write(conclusion_text))
        self.wait(3)
        self.play(FadeOut(conclusion_text))


class ChessPositionAnalysis(Scene):
    """Analyze specific chess positions using mathematics."""
    
    def construct(self):
        self.analyze_opening_position()
        self.analyze_middlegame_position()
        self.analyze_endgame_position()
    
    def analyze_opening_position(self):
        """Analyze opening position mathematics."""
        title = Text("Opening Position Analysis", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create a typical opening position
        board = VGroup()
        for i in range(8):
            for j in range(8):
                color = WHITE if (i + j) % 2 == 0 else GRAY
                square = Square(side_length=0.4, fill_color=color, fill_opacity=0.3)
                square.move_to([j * 0.5 - 1.75, i * 0.5 - 1.75, 0])
                board.add(square)
        
        # Add opening pieces
        opening_pieces = {
            (6, 0): "♖", (6, 1): "♘", (6, 2): "♗", (6, 3): "♕",
            (6, 4): "♔", (6, 5): "♗", (6, 6): "♘", (6, 7): "♖",
            (7, 0): "♜", (7, 1): "♞", (7, 2): "♝", (7, 3): "♛",
            (7, 4): "♚", (7, 5): "♝", (7, 6): "♞", (7, 7): "♜"
        }
        
        pieces = VGroup()
        for (row, col), piece in opening_pieces.items():
            piece_text = Text(piece, font_size=20, color=BLACK)
            piece_text.move_to([col * 0.5 - 1.75, row * 0.5 - 1.75, 0])
            pieces.add(piece_text)
        
        # Show mathematical analysis
        analysis_text = VGroup(
            Text("Opening Mathematics:", font_size=18, color=WHITE),
            Text("• Center control: 4 squares", font_size=14, color=YELLOW),
            Text("• Development: 8 pieces to develop", font_size=14, color=YELLOW),
            Text("• King safety: Castling options", font_size=14, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT)
        analysis_text.next_to(board, DOWN)
        
        self.play(Write(title))
        self.play(Create(board))
        self.play(Create(pieces))
        self.play(Write(analysis_text))
        self.wait(2)
        
        self.play(FadeOut(board), FadeOut(pieces), FadeOut(analysis_text), FadeOut(title))
    
    def analyze_middlegame_position(self):
        """Analyze middlegame position mathematics."""
        title = Text("Middlegame Position Analysis", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create a middlegame position
        board = VGroup()
        for i in range(8):
            for j in range(8):
                color = WHITE if (i + j) % 2 == 0 else GRAY
                square = Square(side_length=0.4, fill_color=color, fill_opacity=0.3)
                square.move_to([j * 0.5 - 1.75, i * 0.5 - 1.75, 0])
                board.add(square)
        
        # Add middlegame pieces
        middlegame_pieces = {
            (4, 3): "♕", (4, 4): "♔", (3, 2): "♗", (5, 5): "♘",
            (2, 3): "♜", (3, 4): "♚", (4, 2): "♝", (5, 3): "♞"
        }
        
        pieces = VGroup()
        for (row, col), piece in middlegame_pieces.items():
            piece_text = Text(piece, font_size=20, color=BLACK)
            piece_text.move_to([col * 0.5 - 1.75, row * 0.5 - 1.75, 0])
            pieces.add(piece_text)
        
        # Show mathematical analysis
        analysis_text = VGroup(
            Text("Middlegame Mathematics:", font_size=18, color=WHITE),
            Text("• Tactical opportunities: 6+", font_size=14, color=YELLOW),
            Text("• Position evaluation: ±0.5", font_size=14, color=YELLOW),
            Text("• Attack vectors: Multiple", font_size=14, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT)
        analysis_text.next_to(board, DOWN)
        
        self.play(Write(title))
        self.play(Create(board))
        self.play(Create(pieces))
        self.play(Write(analysis_text))
        self.wait(2)
        
        self.play(FadeOut(board), FadeOut(pieces), FadeOut(analysis_text), FadeOut(title))
    
    def analyze_endgame_position(self):
        """Analyze endgame position mathematics."""
        title = Text("Endgame Position Analysis", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create an endgame position
        board = VGroup()
        for i in range(8):
            for j in range(8):
                color = WHITE if (i + j) % 2 == 0 else GRAY
                square = Square(side_length=0.4, fill_color=color, fill_opacity=0.3)
                square.move_to([j * 0.5 - 1.75, i * 0.5 - 1.75, 0])
                board.add(square)
        
        # Add endgame pieces
        endgame_pieces = {
            (4, 4): "♔", (3, 3): "♚", (5, 5): "♕"
        }
        
        pieces = VGroup()
        for (row, col), piece in endgame_pieces.items():
            piece_text = Text(piece, font_size=20, color=BLACK)
            piece_text.move_to([col * 0.5 - 1.75, row * 0.5 - 1.75, 0])
            pieces.add(piece_text)
        
        # Show mathematical analysis
        analysis_text = VGroup(
            Text("Endgame Mathematics:", font_size=18, color=WHITE),
            Text("• King distance: 1 square", font_size=14, color=YELLOW),
            Text("• Material count: +9 (Queen)", font_size=14, color=YELLOW),
            Text("• Winning probability: 95%", font_size=14, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT)
        analysis_text.next_to(board, DOWN)
        
        self.play(Write(title))
        self.play(Create(board))
        self.play(Create(pieces))
        self.play(Write(analysis_text))
        self.wait(2)
        
        self.play(FadeOut(board), FadeOut(pieces), FadeOut(analysis_text), FadeOut(title)) 