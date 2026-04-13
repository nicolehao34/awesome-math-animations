#!/usr/bin/env python3
"""
Advanced Rubik's Cube Permutation Animations

These scenes visualize the deep mathematical concepts behind
Rubik's cube permutations, group theory, and solving algorithms.

Run with:
    manim animations.py PermutationCyclesScene -pqh
    manim animations.py CommutatorScene -pqh
"""

from manim import *
from rubiks_cube import RubiksCube, CubeSlice
from permutations import Permutation, RubikPermutations


class PermutationCyclesScene(Scene):
    """
    Visualize how a Rubik's cube move is a permutation in cycle notation.
    
    Key concept: Every move permutes the pieces in cycles.
    Example: R move cycles 4 edges and 4 corners.
    """
    
    def construct(self):
        # Title
        title = Text("Permutations & Cycle Notation", font_size=44)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Explain permutations
        explanation = Text(
            "Each Rubik's cube move is a PERMUTATION of pieces",
            font_size=28
        )
        explanation.next_to(title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait()
        
        # Show cycle notation
        cycle_title = Text("Cycle Notation", font_size=36, weight=BOLD)
        cycle_title.shift(UP * 1.5)
        self.play(FadeIn(cycle_title))
        
        # Example permutation
        example = MathTex(r"(1 \, 2 \, 3)(4 \, 5)", font_size=48)
        example.next_to(cycle_title, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait()
        
        # Explanation of cycles
        arrows = VGroup(
            MathTex(r"1 \rightarrow 2", font_size=32),
            MathTex(r"2 \rightarrow 3", font_size=32),
            MathTex(r"3 \rightarrow 1", font_size=32),
            MathTex(r"4 \rightarrow 5", font_size=32),
            MathTex(r"5 \rightarrow 4", font_size=32),
        )
        arrows.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        arrows.next_to(example, DOWN, buff=0.6)
        
        # Animate each arrow
        for arrow in arrows:
            self.play(FadeIn(arrow), run_time=0.4)
        self.wait(2)
        
        # Clear and show R move
        self.play(
            FadeOut(explanation),
            FadeOut(cycle_title),
            FadeOut(example),
            FadeOut(arrows)
        )
        
        # R move visualization
        r_title = Text("R Move on a Rubik's Cube", font_size=36)
        r_title.shift(UP * 2.5)
        self.play(Write(r_title))
        
        # Show the cycle structure
        corners_text = Text("Corners:", font_size=28, color=YELLOW)
        corners_text.shift(UP * 1.2 + LEFT * 3)
        corners_cycle = MathTex(r"(1 \, 2 \, 6 \, 5)", font_size=36, color=YELLOW)
        corners_cycle.next_to(corners_text, RIGHT, buff=0.3)
        
        edges_text = Text("Edges:", font_size=28, color=BLUE)
        edges_text.shift(UP * 0.2 + LEFT * 3)
        edges_cycle = MathTex(r"(9 \, 10 \, 18 \, 13)", font_size=36, color=BLUE)
        edges_cycle.next_to(edges_text, RIGHT, buff=0.3)
        
        self.play(Write(corners_text), Write(corners_cycle))
        self.wait()
        self.play(Write(edges_text), Write(edges_cycle))
        self.wait()
        
        # Key insight
        insight = Text(
            "Each move permutes pieces in disjoint cycles!",
            font_size=30,
            color=GREEN
        )
        insight.shift(DOWN * 1.5)
        self.play(Write(insight))
        self.wait(2)
        
        # Order of permutation
        order_text = Text("Order of R move: 4", font_size=32)
        order_explanation = Text(
            "(Repeating R four times returns to the solved state)",
            font_size=24,
            color=GRAY
        )
        order_text.shift(DOWN * 2.8)
        order_explanation.next_to(order_text, DOWN, buff=0.2)
        
        self.play(Write(order_text))
        self.play(Write(order_explanation))
        self.wait(3)


class CommutatorScene(ThreeDScene):
    """
    Demonstrate commutators: [A, B] = A B A' B'
    
    Commutators are the KEY to advanced solving techniques!
    They create 3-cycles while leaving most pieces in place.
    """
    
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        
        # Title
        title = Text("Commutators: The Magic Formula", font_size=40)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait()
        
        # Show formula
        formula = MathTex(r"[A, B] = A \, B \, A' \, B'", font_size=40)
        formula.next_to(title, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula))
        self.wait()
        
        # Create cube
        cube = RubiksCube(side_length=2.2)
        self.play(FadeIn(cube))
        self.wait()
        
        # Example: [R, U]
        example_text = Text("Example: [R, U] = R U R' U'", font_size=28)
        example_text.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(example_text)
        self.play(Write(example_text))
        self.wait()
        
        # Execute commutator
        moves = [
            ('R', 1, "R"),
            ('U', 1, "U"),
            ('R', -1, "R'"),
            ('U', -1, "U'"),
        ]
        
        for face, direction, label in moves:
            move_label = Text(label, font_size=48, color=YELLOW)
            move_label.to_corner(UL).shift(DOWN)
            self.add_fixed_in_frame_mobjects(move_label)
            self.play(Write(move_label))
            
            self.play(cube.rotate_face(face, direction=direction, animation_time=1))
            self.wait(0.3)
            
            self.play(FadeOut(move_label))
        
        # Emphasize result
        result_text = Text(
            "Only 3 corners moved! Rest unchanged!",
            font_size=30,
            color=GREEN
        )
        result_text.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(result_text)
        self.play(Transform(example_text, result_text))
        self.wait()
        
        # Rotate to show
        self.play(Rotate(cube, angle=PI, axis=UP, run_time=2))
        self.wait(2)


class ConjugateScene(ThreeDScene):
    """
    Show conjugates: A B A'
    
    Conjugation "repositions" an algorithm to affect different pieces.
    """
    
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-50 * DEGREES)
        
        title = Text("Conjugates: Repositioning Algorithms", font_size=38)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait()
        
        # Formula
        formula = MathTex(r"A \, B \, A'", font_size=44)
        formula.next_to(title, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula))
        self.wait()
        
        # Explanation
        explanation = Text(
            "1. Setup (A)  2. Algorithm (B)  3. Undo Setup (A')",
            font_size=24
        )
        explanation.next_to(formula, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        self.wait()
        
        # Create cube
        cube = RubiksCube(side_length=2.2)
        self.play(FadeIn(cube))
        self.wait()
        
        # Example: D R D' (conjugate of R by D)
        example = Text("Example: D R D'", font_size=32, color=YELLOW)
        example.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(example)
        self.play(Write(example))
        self.wait()
        
        # Execute
        steps = [
            ('D', 1, "D: Setup move"),
            ('R', 1, "R: Main algorithm"),
            ('D', -1, "D': Undo setup"),
        ]
        
        for face, direction, desc in steps:
            desc_text = Text(desc, font_size=28, color=GREEN)
            desc_text.to_edge(DOWN).shift(UP * 0.8)
            self.add_fixed_in_frame_mobjects(desc_text)
            self.play(Write(desc_text))
            
            self.play(cube.rotate_face(face, direction=direction, animation_time=1.5))
            self.wait(0.5)
            
            self.play(FadeOut(desc_text))
        
        # Result
        result = Text(
            "R algorithm now affects DIFFERENT pieces!",
            font_size=28,
            color=GREEN
        )
        result.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(result)
        self.play(Transform(example, result))
        self.wait(3)


class ParityScene(Scene):
    """
    Explain permutation parity and why certain positions are impossible.
    
    This is a fundamental mathematical constraint!
    """
    
    def construct(self):
        # Title
        title = Text("Permutation Parity", font_size=44, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Subtitle
        subtitle = Text(
            "Some cube positions are mathematically IMPOSSIBLE",
            font_size=30,
            color=YELLOW
        )
        subtitle.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle))
        self.wait()
        
        # Show impossible configurations
        impossible_title = Text("Impossible Configurations:", font_size=32, weight=BOLD)
        impossible_title.shift(UP * 1.5)
        self.play(Write(impossible_title))
        
        impossibles = VGroup(
            Text("❌ Swap exactly two corners", font_size=28, color=RED),
            Text("❌ Swap exactly two edges", font_size=28, color=RED),
            Text("❌ Flip exactly one edge", font_size=28, color=RED),
            Text("❌ Twist exactly one corner", font_size=28, color=RED),
        )
        impossibles.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        impossibles.next_to(impossible_title, DOWN, buff=0.5)
        
        for item in impossibles:
            self.play(FadeIn(item), run_time=0.5)
        self.wait(2)
        
        # Mathematical explanation
        math_title = Text("Why?", font_size=36, weight=BOLD, color=GREEN)
        math_title.shift(DOWN * 1.2)
        self.play(Write(math_title))
        
        explanation = Text(
            "All legal moves are EVEN permutations\n"
            "Composing even permutations gives even permutations\n"
            "Swapping two pieces is an ODD permutation!",
            font_size=24,
            line_spacing=1.2
        )
        explanation.next_to(math_title, DOWN, buff=0.4)
        self.play(Write(explanation))
        self.wait(3)
        
        # Key insight
        insight = Text(
            "This is why you can't solve a reassembled cube with wrong parity!",
            font_size=26,
            color=BLUE
        )
        insight.to_edge(DOWN, buff=0.5)
        self.play(Write(insight))
        self.wait(3)


class GroupStructureScene(Scene):
    """
    Visualize the group structure of the Rubik's cube.
    
    Shows generators, subgroups, and the Cayley graph concept.
    """
    
    def construct(self):
        # Title
        title = Text("The Rubik's Cube Group", font_size=44)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Group properties
        properties = VGroup(
            Text("• Set: ~43 quintillion cube positions", font_size=28),
            Text("• Identity: Solved cube", font_size=28),
            Text("• Operation: Compose moves", font_size=28),
            Text("• Inverses: Every move has R → R'", font_size=28),
            Text("• Associativity: (AB)C = A(BC)", font_size=28),
        )
        properties.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        properties.shift(UP * 0.8)
        
        for prop in properties:
            self.play(FadeIn(prop), run_time=0.5)
        self.wait(2)
        
        # Generators
        gen_title = Text("Generators:", font_size=32, weight=BOLD, color=YELLOW)
        gen_title.shift(DOWN * 1.5)
        self.play(Write(gen_title))
        
        generators = MathTex(
            r"\langle R, L, U, D, F, B \rangle",
            font_size=40,
            color=YELLOW
        )
        generators.next_to(gen_title, DOWN, buff=0.3)
        self.play(Write(generators))
        self.wait()
        
        # Explanation
        gen_explain = Text(
            "Every position can be reached using these 6 moves!",
            font_size=24,
            color=GREEN
        )
        gen_explain.next_to(generators, DOWN, buff=0.4)
        self.play(Write(gen_explain))
        self.wait()
        
        # God's number
        gods_number = Text(
            "God's Number: 20",
            font_size=36,
            weight=BOLD,
            color=BLUE
        )
        gods_number.shift(DOWN * 3.2)
        self.play(Write(gods_number))
        
        gods_explain = Text(
            "(Maximum moves needed to solve ANY position)",
            font_size=22,
            color=GRAY
        )
        gods_explain.next_to(gods_number, DOWN, buff=0.2)
        self.play(Write(gods_explain))
        self.wait(3)


class AlgorithmOrderScene(ThreeDScene):
    """
    Show that repeating an algorithm eventually returns to the start.
    
    Demonstrates the concept of "order" of a permutation.
    """
    
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        
        title = Text("Order of Permutations", font_size=40)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait()
        
        explanation = Text(
            "Repeating any move sequence enough times\nreturns the cube to its starting position!",
            font_size=26,
            line_spacing=1.2
        )
        explanation.next_to(title, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        self.wait()
        
        # Create cube
        cube = RubiksCube(side_length=2.2)
        self.play(FadeIn(cube))
        self.wait()
        
        # Show R move has order 4
        sequence_text = Text("Sequence: R (repeated 4 times)", font_size=28)
        sequence_text.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(sequence_text)
        self.play(Write(sequence_text))
        self.wait()
        
        # Repeat R four times
        for i in range(4):
            counter = Text(f"Repetition {i+1}/4", font_size=36, color=YELLOW)
            counter.to_corner(UR).shift(DOWN)
            self.add_fixed_in_frame_mobjects(counter)
            self.play(Write(counter))
            
            self.play(cube.rotate_face('R', direction=1, animation_time=1.5))
            self.wait(0.5)
            
            self.play(FadeOut(counter))
        
        # Celebrate return
        success = Text(
            "BACK TO START! ✓",
            font_size=40,
            color=GREEN,
            weight=BOLD
        )
        success.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(success)
        self.play(Transform(sequence_text, success))
        self.wait()
        
        # Flash the cube
        self.play(
            cube.animate.scale(1.2),
            rate_func=there_and_back,
            run_time=1
        )
        self.wait(2)


if __name__ == "__main__":
    """
    Render these advanced scenes:
    
    manim animations.py PermutationCyclesScene -pqh
    manim animations.py CommutatorScene -pqh
    manim animations.py ConjugateScene -pqh
    manim animations.py ParityScene -pqh
    manim animations.py GroupStructureScene -pqh
    manim animations.py AlgorithmOrderScene -pqh
    """
    pass
