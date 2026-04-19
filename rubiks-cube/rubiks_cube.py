#!/usr/bin/env python3
"""
Rubik's Cube 3D Model for Manim
Creates a beautiful, mathematically accurate Rubik's cube.
"""

from manim import *
import numpy as np


class RubiksCube(VGroup):
    """
    A 3D Rubik's Cube in Manim.
    
    The cube is built from 27 small cubes (cubies):
    - 8 corner pieces (3 colored faces each)
    - 12 edge pieces (2 colored faces each)
    - 6 center pieces (1 colored face each)
    - 1 hidden center (no visible faces)
    
    Standard color scheme:
    - White opposite Yellow
    - Red opposite Orange
    - Blue opposite Green
    """
    
    def __init__(
        self,
        side_length=2,
        gap=0.05,
        colors=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        
        # Standard Rubik's cube colors
        if colors is None:
            self.colors = {
                'U': WHITE,    # Up (top)
                'D': YELLOW,   # Down (bottom)
                'F': RED,      # Front
                'B': ORANGE,   # Back
                'R': BLUE,     # Right
                'L': GREEN,    # Left
            }
        else:
            self.colors = colors
            
        self.side_length = side_length
        self.gap = gap
        self.cubie_size = (side_length - 2 * gap) / 3
        
        # Create the 27 cubies
        self.cubies = VGroup()
        self.create_cubies()
        
        self.add(self.cubies)
        
    def create_cubies(self):
        """Create all 27 small cubes that make up the Rubik's cube."""
        offset = self.side_length / 2 - self.cubie_size / 2
        
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    position = np.array([
                        x * (self.cubie_size + self.gap),
                        y * (self.cubie_size + self.gap),
                        z * (self.cubie_size + self.gap)
                    ])
                    
                    cubie = self.create_cubie(x, y, z, position)
                    self.cubies.add(cubie)
    
    def create_cubie(self, x, y, z, position):
        """
        Create a single cubie with colored faces.
        
        Args:
            x, y, z: Position in the 3x3x3 grid (-1, 0, or 1)
            position: 3D position vector
        """
        cube = Cube(
            side_length=self.cubie_size,
            fill_opacity=1,
            stroke_width=2,
            stroke_color=BLACK
        )
        cube.move_to(position)
        
        # Color the exterior faces
        faces = self.get_face_colors(x, y, z)
        
        # Manim Cube generates faces in order: IN, OUT, LEFT, RIGHT, UP, DOWN
        # Each face is positioned at that direction from the cubie center:
        #   IN  = face at z=-side/2 (bottom),  OUT = face at z=+side/2 (top)
        #   LEFT= face at x=-side/2,            RIGHT= face at x=+side/2
        #   UP  = face at y=+side/2 (front, +y), DOWN= face at y=-side/2 (back, -y)
        face_indices = {
            'F': 4,  # Front (+y direction = UP constant,   index 4)
            'B': 5,  # Back  (-y direction = DOWN constant, index 5)
            'L': 2,  # Left  (-x direction = LEFT constant, index 2)
            'R': 3,  # Right (+x direction = RIGHT constant, index 3)
            'U': 1,  # Up    (+z direction = OUT constant,  index 1)
            'D': 0,  # Down  (-z direction = IN constant,   index 0)
        }
        
        for face_name, color in faces.items():
            if color is not None:
                cube[face_indices[face_name]].set_fill(color, opacity=1)
            else:
                # Interior faces are black
                cube[face_indices[face_name]].set_fill(BLACK, opacity=1)
        
        return cube
    
    def get_face_colors(self, x, y, z):
        """
        Determine which faces of a cubie should be colored.
        Only exterior faces get colors.
        """
        faces = {
            'F': None,  # Front (+y direction)
            'B': None,  # Back (-y direction)
            'L': None,  # Left (-x direction)
            'R': None,  # Right (+x direction)
            'U': None,  # Up (+z direction)
            'D': None,  # Down (-z direction)
        }
        
        # Check if on exterior and assign colors
        if x == 1:  # Right face
            faces['R'] = self.colors['R']
        elif x == -1:  # Left face
            faces['L'] = self.colors['L']
            
        if y == 1:  # Front face
            faces['F'] = self.colors['F']
        elif y == -1:  # Back face
            faces['B'] = self.colors['B']
            
        if z == 1:  # Top face
            faces['U'] = self.colors['U']
        elif z == -1:  # Bottom face
            faces['D'] = self.colors['D']
            
        return faces
    
    def get_face_cubies(self, face):
        """
        Get the 9 cubies that belong to a specific face.

        Uses current 3D positions rather than initial grid indices so that
        face selection remains correct after prior rotations have physically
        moved cubies to new locations.

        Args:
            face: 'U', 'D', 'F', 'B', 'R', or 'L'
        """
        step = self.cubie_size + self.gap
        # Threshold is halfway between the center layer (0) and the outer
        # layer (step), giving plenty of margin for floating-point drift.
        t = step * 0.5

        face_check = {
            'U': lambda p: p[2] >  t,
            'D': lambda p: p[2] < -t,
            'R': lambda p: p[0] >  t,
            'L': lambda p: p[0] < -t,
            'F': lambda p: p[1] >  t,
            'B': lambda p: p[1] < -t,
        }

        check = face_check[face]
        return VGroup(*[c for c in self.cubies if check(c.get_center())])
    
    def get_cubie_by_coords(self, x, y, z):
        """Get a cubie by its grid coordinates (-1, 0, or 1)."""
        # Convert grid coords to index (0-26)
        index = (x + 1) * 9 + (y + 1) * 3 + (z + 1)
        return self.cubies[index]
    
    def rotate_face(self, face, direction=1, animation_time=1):
        """
        Create animation for rotating a face.
        
        Args:
            face: 'U', 'D', 'F', 'B', 'R', or 'L'
            direction: 1 for clockwise, -1 for counter-clockwise
            animation_time: Duration of animation
            
        Returns:
            Animation object
        """
        # Get the cubies to rotate
        face_cubies = self.get_face_cubies(face)
        
        # Define rotation axes
        axes = {
            'U': OUT,    # Z-axis (up)
            'D': IN,     # Negative Z-axis (down)
            'R': RIGHT,  # X-axis (right)
            'L': LEFT,   # Negative X-axis (left)
            'F': UP,     # Y-axis (front)
            'B': DOWN,   # Negative Y-axis (back)
        }
        
        axis = axes[face]
        angle = direction * PI / 2  # 90 degrees
        
        # Create rotation animation
        return Rotate(
            face_cubies,
            angle=angle,
            axis=axis,
            about_point=ORIGIN,
            run_time=animation_time
        )


class CubeSlice(VGroup):
    """Helper class for visualizing a single slice or face of the cube."""
    
    def __init__(self, face_name, color, **kwargs):
        super().__init__(**kwargs)
        self.face_name = face_name
        
        # Create a 3x3 grid
        for i in range(3):
            for j in range(3):
                square = Square(side_length=0.8, stroke_width=3, stroke_color=BLACK)
                square.set_fill(color, opacity=1)
                square.shift(RIGHT * (i - 1) * 0.9 + UP * (j - 1) * 0.9)
                self.add(square)
        
        # Add label
        label = Text(face_name, font_size=36).next_to(self, UP)
        self.add(label)
