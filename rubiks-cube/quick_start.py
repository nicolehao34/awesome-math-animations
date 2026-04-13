#!/usr/bin/env python3
"""
Quick Start Guide: Learning Rubik's Cube in Manim

This is your step-by-step learning path!
Follow the tutorials in order.
"""

from manim import *

print("""
╔════════════════════════════════════════════════════════════════╗
║     RUBIK'S CUBE PERMUTATION ANIMATIONS IN MANIM              ║
║                   Quick Start Guide                            ║
╚════════════════════════════════════════════════════════════════╝

📚 LEARNING PATH:

STEP 1: Install Dependencies
────────────────────────────────────────────────────────────────
   pip install -r requirements.txt

STEP 2: Basic Demonstrations
────────────────────────────────────────────────────────────────
   Start here to understand the 3D cube and how to animate it:

   manim basic_demo.py IntroScene -pql
      → Introduction to the Rubik's cube in 3D

   manim basic_demo.py SingleMoveScene -pql
      → Learn how a single face rotation works

   manim basic_demo.py NotationScene -pql
      → Understand R, U, F, L, D, B notation

   manim basic_demo.py FaceSequenceScene -pql
      → See a sequence of moves: R U R' U'

   manim basic_demo.py ExplodedViewScene -pql
      → View the cube's internal structure

STEP 3: Understanding Permutations
────────────────────────────────────────────────────────────────
   Learn the mathematics behind the cube:

   python permutations.py
      → Run the console demo to learn cycle notation

   Read through permutations.py to understand:
      • Cycle notation: (1 2 3)(4 5)
      • Permutation composition
      • Commutators: [A, B] = ABA'B'
      • Conjugates: ABA'
      • Group theory basics

STEP 4: Advanced Mathematical Animations
────────────────────────────────────────────────────────────────
   Visualize the deep mathematics:

   manim animations.py PermutationCyclesScene -pqh
      → See how moves are permutations in cycle notation

   manim animations.py CommutatorScene -pqh
      → Learn the magic of commutators

   manim animations.py ConjugateScene -pqh
      → Understand how conjugates reposition algorithms

   manim animations.py ParityScene -pqh
      → Discover why some positions are impossible

   manim animations.py GroupStructureScene -pqh
      → Explore the cube's group structure

   manim animations.py AlgorithmOrderScene -pqh
      → See how repetition returns to the start

STEP 5: Explore the Code
────────────────────────────────────────────────────────────────
   Open and study these files:

   rubiks_cube.py
      → The 3D cube model class
      → Learn: VGroup, Cube, 3D positioning, rotations

   basic_demo.py
      → Simple animation scenes
      → Learn: ThreeDScene, camera control, Create, Rotate

   animations.py
      → Advanced mathematical scenes
      → Learn: Complex animations, text overlays, MathTex

   permutations.py
      → Pure Python mathematics
      → Learn: Permutation class, group operations

🎯 KEY MANIM CONCEPTS TO LEARN:

1. ThreeDScene:
   - Set camera: self.set_camera_orientation(phi=..., theta=...)
   - Move camera: self.move_camera(phi=..., zoom=...)

2. VGroup:
   - Group objects together
   - Transform groups as units

3. Animations:
   - Create(obj) - draws object
   - FadeIn(obj) - fades in
   - Write(text) - writes text
   - Rotate(obj, angle=..., axis=...) - rotates
   - Transform(obj1, obj2) - morphs obj1 into obj2

4. 3D Objects:
   - Cube() - 3D cube
   - Axes: RIGHT (x), UP (y), OUT (z)
   - Position: .move_to(), .shift()

5. Text & Math:
   - Text("...", font_size=...) - plain text
   - MathTex(r"...", font_size=...) - LaTeX math

🔧 MANIM COMMANDS:

Quality flags:
   -ql  = Low quality (480p, fast)
   -qm  = Medium quality (720p)
   -qh  = High quality (1080p)
   -qk  = 4K quality (2160p)

Other flags:
   -p   = Preview after rendering
   -s   = Save last frame only (for thumbnails)
   -a   = Render all scenes in file

Examples:
   manim basic_demo.py IntroScene -pql        # Quick preview
   manim animations.py -pqh                   # Render all in HD
   manim basic_demo.py SingleMoveScene -pql   # Single scene

💡 CUSTOMIZATION IDEAS:

Try modifying the code to:
   • Change the cube colors
   • Add different move sequences
   • Create your own solving algorithm visualization
   • Animate a specific scramble pattern
   • Show the sexy move: R U R' U' (5 times returns!)
   • Visualize the Sune algorithm
   • Create a comparison of different solving methods

📖 LEARNING RESOURCES:

Manim:
   • Official docs: https://docs.manim.community/
   • 3Blue1Brown videos (created with Manim!)

Group Theory:
   • Rubik's Cube Group: Wikipedia
   • Cycle notation: Khan Academy - Permutations

Rubik's Cube:
   • Solving methods: Badmephisto, J Perm (YouTube)
   • Speedcubing algorithms: algdb.net

🎓 TEACHING TIPS:

When explaining to others:
   1. Start with the physical cube (basic_demo.py)
   2. Introduce notation gradually
   3. Show ONE mathematical concept at a time
   4. Use cycle notation visualization
   5. Build up to commutators and conjugates
   6. End with the "impossible positions" insight

🚀 NEXT STEPS:

Once comfortable:
   • Create a BeginnerMethodScene (layer-by-layer solving)
   • Visualize the F2L (First Two Layers) concept
   • Animate the Cross, F2L, OLL, PLL steps
   • Show algorithm generation using commutators
   • Create a "cube in a cube in a cube" pattern animation
   • Visualize subgroup structures

Happy animating! 🎬🎨
═══════════════════════════════════════════════════════════════════
""")

# Example: Quick test to verify Manim is working
class TestScene(Scene):
    """
    Quick test scene to verify your Manim installation.
    
    Run: manim quick_start.py TestScene -pql
    """
    
    def construct(self):
        # Create a simple welcome message
        welcome = Text("Manim is working! ✓", font_size=48, color=GREEN)
        self.play(Write(welcome))
        self.wait()
        
        # Show cube colors
        colors_title = Text("Rubik's Cube Colors:", font_size=32)
        colors_title.to_edge(UP)
        self.play(Transform(welcome, colors_title))
        
        # Display color squares
        color_names = {
            "White": WHITE,
            "Yellow": YELLOW,
            "Red": RED,
            "Orange": ORANGE,
            "Blue": BLUE,
            "Green": GREEN,
        }
        
        color_group = VGroup()
        for name, color in color_names.items():
            square = Square(side_length=0.8, fill_opacity=1, fill_color=color)
            square.set_stroke(BLACK, width=3)
            label = Text(name, font_size=20)
            label.next_to(square, DOWN, buff=0.1)
            group = VGroup(square, label)
            color_group.add(group)
        
        color_group.arrange_in_grid(rows=2, cols=3, buff=0.8)
        
        self.play(FadeIn(color_group), run_time=2)
        self.wait()
        
        # Final message
        ready = Text("Ready to animate Rubik's cubes!", font_size=36, color=YELLOW)
        ready.to_edge(DOWN)
        self.play(Write(ready))
        self.wait(2)


if __name__ == "__main__":
    """
    First, run this test scene to verify everything is working:
    
        manim quick_start.py TestScene -pql
    
    If that works, follow the learning path above!
    """
    pass
