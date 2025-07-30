# Chess Algebra Animations

This project uses Manim to create educational animations that explain chess concepts using algebra and mathematics. The animations demonstrate how chess can be understood as a mathematical system with coordinate geometry, vector analysis, and game theory.

## Overview

The project consists of several animation scenes that cover:

1. **Basic Chess Algebra** (`chess_algebra.py`)
   - Coordinate system and algebraic notation
   - Piece movement vectors
   - Knight mathematics (L-shaped vectors)
   - Bishop diagonal analysis
   - Queen as combination of rook and bishop
   - Distance analysis using Euclidean geometry

2. **Advanced Chess Mathematics** (`advanced_chess_math.py`)
   - Game theory analysis
   - Probability in chess positions
   - Optimization problems
   - Graph theory representation
   - Position analysis (opening, middlegame, endgame)

3. **Utility Classes** (`chess_board.py`)
   - Chess board representation
   - Algebraic notation conversion
   - Piece movement calculations
   - Vector representations

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure you have Manim installed:
```bash
pip install manim
```

## Running the Animations

### Basic Chess Algebra Scene
```bash
manim chess_algebra.py ChessAlgebraScene -pql
```

### Piece Movement Analysis
```bash
manim chess_algebra.py PieceMovementAnalysis -pql
```

### Advanced Chess Mathematics
```bash
manim advanced_chess_math.py AdvancedChessMathematics -pql
```

### Position Analysis
```bash
manim advanced_chess_math.py ChessPositionAnalysis -pql
```

## Command Line Options

- `-p`: Preview the animation
- `-q`: Quality (l=low, m=medium, h=high, k=4k)
- `-l`: Use a lower quality for faster rendering

## Mathematical Concepts Covered

### 1. Coordinate Geometry
- 8×8 coordinate grid system
- Algebraic notation (e4, Nf3, O-O)
- Vector representations of positions

### 2. Vector Analysis
- Piece movement as vectors: (dx, dy)
- Knight moves: |dx| + |dy| = 3
- Bishop moves: |dx| = |dy|
- Rook moves: dx = 0 or dy = 0
- Queen moves: Combination of rook and bishop

### 3. Distance Metrics
- Euclidean distance between squares
- Manhattan distance for certain pieces
- Distance matrices for position analysis

### 4. Game Theory
- Payoff matrices for chess positions
- Nash equilibrium in strategic decisions
- Optimal move selection

### 5. Probability
- Piece value distributions
- Position evaluation probabilities
- Expected value calculations

### 6. Graph Theory
- Chess board as a graph
- Vertices = squares
- Edges = possible moves
- Path analysis for move sequences

### 7. Optimization
- Center control maximization
- Piece development optimization
- Attack vector optimization

## Educational Value

These animations help students understand:

1. **Mathematical Thinking**: How abstract mathematical concepts apply to real-world games
2. **Coordinate Systems**: Practical application of coordinate geometry
3. **Vector Analysis**: Understanding movement and direction in mathematical terms
4. **Game Theory**: Strategic decision making in competitive situations
5. **Probability**: Risk assessment and position evaluation
6. **Optimization**: Finding the best moves and strategies

## Customization

You can modify the animations by:

1. **Changing Colors**: Modify color constants in the scene classes
2. **Adjusting Timing**: Modify `self.wait()` calls to change animation duration
3. **Adding New Concepts**: Create new methods in the scene classes
4. **Custom Positions**: Modify piece positions in the analysis scenes

## File Structure

```
chess/
├── requirements.txt          # Python dependencies
├── README.md               # This file
├── chess_board.py          # Utility classes for chess board
├── chess_algebra.py        # Basic chess algebra animations
└── advanced_chess_math.py  # Advanced mathematical concepts
```

## Examples

### Running a Specific Scene
```bash
# Run the main chess algebra scene
manim chess_algebra.py ChessAlgebraScene -pql

# Run the piece movement analysis
manim chess_algebra.py PieceMovementAnalysis -pql

# Run advanced mathematics
manim advanced_chess_math.py AdvancedChessMathematics -pql
```

### Rendering Options
```bash
# High quality rendering
manim chess_algebra.py ChessAlgebraScene -pqh

# 4K quality
manim chess_algebra.py ChessAlgebraScene -pqk

# Save as GIF
manim chess_algebra.py ChessAlgebraScene -pqm --format=gif
```

## Mathematical Formulas

The animations demonstrate several key mathematical concepts:

1. **Euclidean Distance**: d = √((x₂ - x₁)² + (y₂ - y₁)²)
2. **Knight Movement**: |dx| + |dy| = 3
3. **Bishop Movement**: |dx| = |dy|
4. **Queen Movement**: |dx| = |dy| OR dx = 0 OR dy = 0
5. **King Movement**: |dx| ≤ 1 AND |dy| ≤ 1

## Contributing

To add new animations:

1. Create a new scene class inheriting from `Scene`
2. Implement the `construct()` method
3. Add mathematical analysis methods
4. Update this README with new concepts

## Troubleshooting

- **Manim not found**: Make sure Manim is installed correctly
- **Import errors**: Check that all dependencies are installed
- **Rendering issues**: Try lower quality settings (-pql)
- **Memory issues**: Use lower quality or shorter animations

## License

This project is for educational purposes. Feel free to use and modify the animations for teaching chess and mathematics. 