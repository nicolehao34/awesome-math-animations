# Chess Algebra Animations

This project uses Manim to create educational animations that explain chess concepts using algebra and mathematics. The animations demonstrate how chess can be understood as a mathematical system with coordinate geometry, vector analysis, and game theory.

## Overview
**This project is WIP.**

The project consists of several animation scenes that cover:

1. **Basic Chess Algebra** (`chess_algebra.py`)
   - Claude Shannon, the father of information theory, estimated: Number of possible chess games ≈ 10^120 (Shannon's Number).  This is based on an average branching factor of ~35 and average game length of 80 moves (per player, so 40 full moves).
   - Coordinate system and algebraic notation
   - Piece movement vectors
   - Knight mathematics (L-shaped vectors)
   - Bishop diagonal analysis
   - Queen as combination of rook and bishop
   - Distance analysis using Euclidean geometry
   - **Move Trees** (need to start): 
Chess can be represented as a tree:

      - Each node is a board position.

      - Each edge is a legal move.

      - The root is the starting position.

      - Each path from root to leaf is a complete game.

      - The branching factor (how many moves are available from a given position) is ≈ 35. So if you try to look ahead d moves: Total nodes≈35^d, Total nodes≈35^d
   
      - For d = 5, you’re already at ~52 million nodes.
   - Combinatorial Explosion
      - The total number of legal positions is estimated to be ~
      - Trying to brute-force all possibilities quickly becomes infeasible — this is the combinatorial explosion.

      - That's why we use:

         - Pruning (cutting unpromising branches)

         - Heuristics (approximations)

         - Evaluation functions instead of full-tree search

✅ This explains why chess engines can't search all the way to checkmate (except in very limited cases). Using combinatorisc to understand the game of chess forces us to abstract, approximate, and build smarter algorithms. Also, it helps understand why endgames are easier to solve, the tree is shallow and positions are fewer.

2. **Advanced Chess Mathematics** (`advanced_chess_math.py`)
   - **Game theory analysis** (animation to be implemented)

   ### 🔁 Zermelo's Theorem (1913)
   One of the earliest results in game theory.

   In any finite, two-player, perfect information game (like chess):
   - Either White can force a win
   - Or Black can force a win  
   - Or both can force a draw

   **Chess is determined in theory.**

   *But: we don't know which of these is true because of the game's complexity.*

   ### ♟️ Minimax Theorem
   Choose moves assuming your opponent plays perfectly to minimize your gain.

   **Recursive algorithm:**
   - Your best move = the one that minimizes the opponent's maximum response
   - Leads to a game tree search: simulate moves → opponent responses → your counter-responses, etc.

   ```
   Score(A) = max(min(Opponent's replies to A))
   ```

   ### ✂️ Alpha-Beta Pruning
   Optimizes Minimax by not exploring branches that can't possibly influence the final decision.

   - Cuts down the number of nodes explored from `O(b^d)` to `O(b^{d/2})` in the best case
   - Significantly improves search efficiency

   ### 🧠 Nash Equilibrium (related)
   In non-zero-sum games, a Nash equilibrium is where neither player can benefit by unilaterally changing their strategy.

   In zero-sum perfect information games like chess, the concept simplifies: **the optimal strategy is a best response to the opponent's best strategy.**

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