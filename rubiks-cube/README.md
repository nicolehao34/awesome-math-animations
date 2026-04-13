# Rubik's Cube Permutation Animations in Manim

## ⚠️ Installation Note

**If you're using Python 3.14**: Manim has installation issues. Use **`matplotlib_demo.py`** instead (works immediately!). 

**For full Manim support**: Install Python 3.11 or 3.12.

# 🚀 Quick Start - Working Now!

## Your Setup Issue (Solved!)

**Problem**: Python 3.14 is too new for Manim's OpenGL dependencies  
**Solution**: Use matplotlib now, install proper Manim later with Python 3.12

## ✅ What Works Right Now

### 1. **Matplotlib Demo (3D Visualizations)**
```powershell
cd rubiks-cube
python matplotlib_demo.py
```

Choose from:
- Static 3D Rubik's Cube
- Rotating animation
- Permutation cycles explanation  
- Group theory concepts

### 2. **Pure Math (No Graphics)**
```powershell
python permutations.py
```
Learn cycle notation, permutation composition, commutators, and group theory.

## 📖 What You're Learning

### Mathematics
- **Permutations**: Every move rearranges pieces
- **Cycle Notation**: `(1 2 3)(4 5)` means 1→2→2→3→3→1, 4→5→5→4
- **Group Theory**: 43 quintillion positions form a mathematical group
- **Commutators**: `[A,B] = ABA'B'` creates 3-cycles
- **Parity**: Why some positions are impossible

### Manim Techniques (from code)
- **ThreeDScene**: 3D camera control
- **VGroup**: Grouping objects
- **Animations**: Create, Rotate, FadeIn, Write
- **3D Objects**: Cube, positioning, transformations

## 🎨 Project Files

### Working Right Now
- ✅ `matplotlib_demo.py` - 3D visualizations (working!)
- ✅ `permutations.py` - Math library (working!)
- ⏳ `rubiks_cube.py` - 3D cube model class
- ⏳ `basic_demo.py` - 5 beginner animation scenes
- ⏳ `animations.py` - 6 advanced math visualizations
- ⏳ `quick_start.py` - Test scene + learning path

## 💡 Tips

1. **Start with matplotlib_demo.py** - See the 3D cube and concepts NOW
2. **Read permutations.py** - Understand the math
3. **Study the code** - The Manim files are still great learning resources
4. **Install Python 3.12** - When ready for video-quality animations

## 🎬 Matplotlib vs Manim

**Matplotlib** (what works now):
- ✅ Interactive 3D plots
- ✅ Static and rotating cubes
- ✅ Great for learning and exploration
- ✅ Export to PNG/PDF

**Manim** (after Python 3.12 install):
- ✅ Smooth video animations
- ✅ Professional math explanations
- ✅ Camera movement and transitions
- ✅ Export to MP4 videos
- ✅ 3Blue1Brown-style animations

**Both teach the same mathematics!** Manim just looks prettier on video.

## Mathematical Concepts

### Group Theory and Permutations

The Rubik's cube is a physical representation of **group theory**:

1. **The Rubik's Cube Group**: The set of all possible cube positions forms a group with ~43 quintillion elements
2. **Permutations**: Each move is a permutation of the cube's pieces
3. **Composition**: Combining moves = composing permutations
4. **Inverses**: Every move has an inverse (opposite rotation)
5. **Cycle Notation**: Moves can be written as cycles like (1 2 3)(4 5 6)

### Key Properties

- **Order**: The smallest number of repetitions to return to start (e.g., R has order 4)
- **Commutators**: [A, B] = ABA'B' - fundamental for solving algorithms
- **Conjugates**: ABA' - repositions a move to affect different pieces
- **Parity**: You can't swap just two pieces or flip just one edge

## File Structure

- `rubiks_cube.py` - Core Rubik's cube 3D model in Manim
- `permutations.py` - Permutation mathematics and group theory
- `animations.py` - Main animation scenes
- `basic_demo.py` - Simple getting-started examples
- `advanced_demo.py` - Complex permutation visualizations
- `requirements.txt` - Python dependencies

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run a basic demo
manim basic_demo.py IntroScene -pql

# Run permutation visualization
manim animations.py PermutationCyclesScene -pqh

# Run all animations
manim animations.py -pql
```


## Quick Start 2
```bash
# Basic demos
manim basic_demo.py IntroScene -pql           # Introduction to 3D cube
manim basic_demo.py SingleMoveScene -pql      # Single R move
manim basic_demo.py NotationScene -pql        # Notation explanation
manim basic_demo.py FaceSequenceScene -pql    # R U R' U' sequence
manim basic_demo.py ExplodedViewScene -pql    # See all 27 cubies

# Advanced math animations
manim animations.py PermutationCyclesScene -pqh   # Cycle notation
manim animations.py CommutatorScene -pqh          # Commutators [A,B]
manim animations.py ConjugateScene -pqh           # Conjugates ABA'
manim animations.py ParityScene -pql              # Impossible positions
manim animations.py GroupStructureScene -pql      # Group theory
manim animations.py AlgorithmOrderScene -pqh      # Order of moves

# Test scene
manim quick_start.py TestScene -pql          # Verify installation
```

## Manim Quality Flags

- `-ql` = Low quality (480p, fast preview)
- `-qm` = Medium quality (720p)
- `-qh` = High quality (1080p)
- `-qk` = 4K quality (2160p)
- `-p` = Preview after rendering

## Animation Scenes

### Basic Scenes
1. **IntroScene** - Introduction to the cube
2. **SingleMoveScene** - Show a single rotation
3. **NotationScene** - Explain move notation (R, U, F, etc.)

### Permutation Scenes
4. **PermutationCyclesScene** - Visualize cycle notation
5. **CommutatorScene** - Demonstrate commutators
6. **ConjugateScene** - Show conjugate moves
7. **ParityScene** - Explain permutation parity

### Advanced Scenes
8. **SolvingAlgorithmScene** - Animate a solving algorithm
9. **GroupStructureScene** - Visualize group properties
10. **BeginnerMethodScene** - Show layer-by-layer method

## Rubik's Cube Notation

- **R** = Right face clockwise
- **L** = Left face clockwise
- **U** = Up (top) face clockwise
- **D** = Down (bottom) face clockwise
- **F** = Front face clockwise
- **B** = Back face clockwise
- **'** = Prime (counter-clockwise): R' = Right counter-clockwise
- **2** = Double turn: R2 = Right 180°

## Learning Path

1. Start with `basic_demo.py` to understand the 3D cube structure
2. Study `permutations.py` to grasp the mathematics
3. Explore `animations.py` to see visualization techniques
4. Experiment by modifying the scenes!

## Resources

- [Manim Documentation](https://docs.manim.community/)
- [Rubik's Cube Group Theory](https://en.wikipedia.org/wiki/Rubik%27s_Cube_group)
- [Cycle Notation](https://en.wikipedia.org/wiki/Permutation#Cycle_notation)
- [The Mathematics of the Rubik's Cube](https://web.mit.edu/sp.268/www/rubik.pdf)
