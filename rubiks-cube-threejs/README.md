# Rubik's Cube - Three.js

An interactive 3D Rubik's Cube built with [Three.js](https://threejs.org/). Features smooth animated face rotations, orbit camera controls, scramble/reset, and keyboard shortcuts.

## Getting Started

```bash
cd rubiks-cube-threejs
npm install
npm run dev
```

Then open `http://localhost:5173` in your browser.

## Controls

### Mouse
- **Drag** to orbit the camera around the cube
- **Scroll** to zoom in/out

### Buttons
Click any move button (R, R', L, L', U, U', D, D', F, F', B, B') to rotate that face.

### Keyboard
- `r` → R, `Shift+R` → R'
- `l` → L, `Shift+L` → L'
- `u` → U, `Shift+U` → U'
- `d` → D, `Shift+D` → D'
- `f` → F, `Shift+F` → F'
- `b` → B, `Shift+B` → B'
- `s` → Scramble (20 random moves)

## Architecture

```
src/
├── main.js       # Scene setup, render loop, camera, lighting
├── cube.js       # Cube model — 27 cubies with per-face coloring
├── moves.js      # Move definitions (face, axis, angle) + scramble generator
├── animator.js   # Queue-based animation with eased tweening
└── controls.js   # OrbitControls + UI button/keyboard bindings
```

## How It Works

1. **Cube Model**: 27 `BoxGeometry` meshes arranged in a 3×3×3 grid. Each cubie has 6 materials — exterior faces get standard Rubik's colors, interior faces are black.

2. **Face Selection**: `getFaceCubies(face)` checks each cubie's world position against a threshold to identify which 9 cubies belong to that face.

3. **Animation**: A temporary `THREE.Group` (pivot) is created at the origin. The 9 face cubies are attached to it, and the pivot is rotated with cubic ease-in-out. On completion, cubies are detached back and positions are rounded to prevent drift.

4. **Sequencing**: Moves are queued and processed one at a time, enabling scramble sequences and algorithm demonstrations.

## Building for Production

```bash
npm run build
```

Output goes to `dist/` — static files ready to deploy.
