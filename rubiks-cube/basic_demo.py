#!/usr/bin/env python3
"""
Basic Rubik's Cube Manim Demonstrations

This file contains simple, educational scenes to get you started
with animating a Rubik's cube in Manim.

Run individual scenes:
    manim basic_demo.py IntroScene -pql
    manim basic_demo.py SingleMoveScene -pql
    manim basic_demo.py NotationScene -pql
"""

from manim import *
from rubiks_cube import RubiksCube, CubeSlice


class IntroScene(ThreeDScene):
    """
    Introduction to the Rubik's Cube in 3D.
    
    This scene demonstrates:
    - Creating a 3D cube
    - Camera movement in 3D
    - Basic rotations
    """
    
    def construct(self):
        # Set up the 3D scene
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        
        # Title
        title = Text("The Rubik's Cube", font_size=48)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait()
        
        # Create the cube
        cube = RubiksCube(side_length=2.5)
        
        # Animate cube appearance
        self.play(Create(cube), run_time=2)
        self.wait()
        
        # Rotate the entire cube to show all sides
        subtitle = Text("A 3D puzzle with 43 quintillion positions!", font_size=28)
        subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle)
        self.play(Write(subtitle))
        
        # Spin the cube
        self.play(Rotate(cube, angle=2*PI, axis=OUT, run_time=4, rate_func=smooth))
        self.wait()
        
        # Camera orbit
        self.play(Rotate(cube, angle=PI/2, axis=UP, run_time=2))
        self.wait()
        
        # Zoom in
        self.move_camera(phi=75 * DEGREES, theta=-60 * DEGREES, zoom=1.5, run_time=2)
        self.wait(2)


class SingleMoveScene(ThreeDScene):
    """
    Demonstrate a single face rotation.
    
    Key learning: Each move rotates 9 cubies at once!
    """
    
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        
        # Title
        title = Text("Single Move: R (Right clockwise)", font_size=40)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Create cube
        cube = RubiksCube(side_length=2.5)
        self.play(FadeIn(cube))
        self.wait()
        
        # Highlight the right face
        explanation = Text("This move rotates the RIGHT face 90° clockwise", font_size=24)
        explanation.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        self.wait()
        
        # Perform the R move
        self.play(cube.rotate_face('R', direction=1, animation_time=2))
        self.wait()
        
        # Show it again
        explanation2 = Text("Let's see that again...", font_size=24)
        explanation2.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(explanation2)
        self.play(Transform(explanation, explanation2))
        self.wait()
        
        # Slower rotation
        self.play(cube.rotate_face('R', direction=1, animation_time=3))
        self.wait()
        
        # Explain inverse
        explanation3 = Text("R' (R-prime) means counter-clockwise: the INVERSE", font_size=24)
        explanation3.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(explanation3)
        self.play(Transform(explanation, explanation3))
        self.wait()
        
        # Perform R' to undo
        self.play(cube.rotate_face('R', direction=-1, animation_time=2))
        self.wait(2)


class NotationScene(Scene):
    """
    Explain standard Rubik's cube notation.
    
    This is a 2D scene showing the notation system.
    """
    
    def construct(self):
        # Title
        title = Text("Rubik's Cube Notation", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Create notation table
        notation_text = [
            ("R", "Right face clockwise", BLUE),
            ("L", "Left face clockwise", GREEN),
            ("U", "Up (top) face clockwise", WHITE),
            ("D", "Down (bottom) face clockwise", YELLOW),
            ("F", "Front face clockwise", RED),
            ("B", "Back face clockwise", ORANGE),
        ]
        
        notation_group = VGroup()
        for i, (move, description, color) in enumerate(notation_text):
            # Move letter
            move_text = Text(move, font_size=36, color=color, weight=BOLD)
            
            # Description
            desc_text = Text(description, font_size=24)
            desc_text.next_to(move_text, RIGHT, buff=0.5)
            
            # Combine
            row = VGroup(move_text, desc_text)
            notation_group.add(row)
        
        notation_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        notation_group.next_to(title, DOWN, buff=0.8)
        
        # Animate each row
        for row in notation_group:
            self.play(FadeIn(row), run_time=0.5)
        self.wait()
        
        # Modifiers
        modifier_title = Text("Modifiers:", font_size=36, weight=BOLD)
        modifier_title.next_to(notation_group, DOWN, buff=0.8)
        self.play(Write(modifier_title))
        
        modifiers = VGroup(
            Text("'  (prime) = Counter-clockwise", font_size=28),
            Text("2  (double) = 180° turn", font_size=28),
        )
        modifiers.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        modifiers.next_to(modifier_title, DOWN, buff=0.4)
        
        for mod in modifiers:
            self.play(FadeIn(mod), run_time=0.5)
        self.wait()
        
        # Examples
        examples_title = Text("Examples:", font_size=36, weight=BOLD)
        examples_title.next_to(modifiers, DOWN, buff=0.8)
        self.play(Write(examples_title))
        
        examples = VGroup(
            Text("R' = Right counter-clockwise", font_size=28),
            Text("U2 = Up face 180°", font_size=28),
            Text("F' = Front counter-clockwise", font_size=28),
        )
        examples.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        examples.next_to(examples_title, DOWN, buff=0.4)
        
        for ex in examples:
            self.play(FadeIn(ex), run_time=0.5)
        
        self.wait(3)


class FaceSequenceScene(ThreeDScene):
    """
    Show a sequence of moves: R U R' U'
    
    This is a common pattern in many algorithms.
    """
    
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-50 * DEGREES)
        
        # Title
        title = Text("Move Sequence: R U R' U'", font_size=40)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Create cube
        cube = RubiksCube(side_length=2.4)
        self.play(FadeIn(cube))
        self.wait()
        
        # Define the sequence
        moves = [
            ('R', 1, "R: Right clockwise"),
            ('U', 1, "U: Up clockwise"),
            ('R', -1, "R': Right counter-clockwise"),
            ('U', -1, "U': Up counter-clockwise"),
        ]
        
        # Execute each move
        for face, direction, description in moves:
            # Show description
            desc_text = Text(description, font_size=32, color=YELLOW)
            desc_text.to_edge(DOWN)
            self.add_fixed_in_frame_mobjects(desc_text)
            self.play(Write(desc_text))
            
            # Perform move
            self.play(cube.rotate_face(face, direction=direction, animation_time=1.5))
            self.wait(0.5)
            
            # Remove description
            self.play(FadeOut(desc_text))
        
        # Final message
        final_text = Text("Notice how the cube changed!", font_size=32)
        final_text.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(final_text)
        self.play(Write(final_text))
        self.wait(2)


class ExplodedViewScene(ThreeDScene):
    """
    Show an exploded view of the cube to see its structure.
    
    This demonstrates the 27 individual cubies.
    """
    
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        
        title = Text("Exploded View: 27 Cubies", font_size=40)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Create cube
        cube = RubiksCube(side_length=2)
        self.play(FadeIn(cube))
        self.wait()
        
        # Explode: move each cubie away from center
        explosions = []
        for cubie in cube.cubies:
            current_pos = cubie.get_center()
            exploded_pos = current_pos * 1.8  # Move 80% further out
            explosions.append(cubie.animate.move_to(exploded_pos))
        
        explanation = Text("Each cube is made of 27 smaller cubes!", font_size=28)
        explanation.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        
        self.play(*explosions, run_time=2)
        self.wait()
        
        # Rotate to see better
        self.play(Rotate(cube, angle=PI/3, axis=UP, run_time=2))
        self.wait()
        
        # Collapse back
        collapses = []
        for cubie in cube.cubies:
            original_pos = cubie.get_center() / 1.8
            collapses.append(cubie.animate.move_to(original_pos))
        
        self.play(*collapses, run_time=2)
        self.wait(2)


if __name__ == "__main__":
    """
    To render these scenes, use:
    
    manim basic_demo.py IntroScene -pql          # Introduction
    manim basic_demo.py SingleMoveScene -pql     # Single move demo
    manim basic_demo.py NotationScene -pql       # Notation explanation
    manim basic_demo.py FaceSequenceScene -pql   # Move sequence
    manim basic_demo.py ExplodedViewScene -pql   # Exploded view
    
    Or render all at once:
    manim basic_demo.py -pql
    """
    pass
