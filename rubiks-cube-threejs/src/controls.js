import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { generateScramble } from './moves.js';

/**
 * Set up OrbitControls and UI button bindings.
 */
export function setupControls(camera, renderer, animator, cube) {
  // Orbit controls for camera
  const orbit = new OrbitControls(camera, renderer.domElement);
  orbit.enableDamping = true;
  orbit.dampingFactor = 0.08;
  orbit.minDistance = 4;
  orbit.maxDistance = 15;

  // Move display element
  const moveDisplay = document.getElementById('move-display');

  // Callback when a move starts
  function onMoveStart(moveName) {
    if (moveDisplay) {
      moveDisplay.textContent = moveName;
      clearTimeout(moveDisplay._timeout);
      moveDisplay._timeout = setTimeout(() => {
        moveDisplay.textContent = '';
      }, 800);
    }
  }

  // Wire up the callback
  animator.onMoveStart = onMoveStart;

  // Move buttons
  const moveButtons = document.querySelectorAll('[data-move]');
  for (const btn of moveButtons) {
    btn.addEventListener('click', () => {
      const move = btn.getAttribute('data-move');
      animator.enqueue(move);
    });
  }

  // Scramble button
  const scrambleBtn = document.getElementById('scramble-btn');
  if (scrambleBtn) {
    scrambleBtn.addEventListener('click', () => {
      const scramble = generateScramble(20);
      animator.enqueue(scramble);
    });
  }

  // Reset button
  const resetBtn = document.getElementById('reset-btn');
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      if (!animator.busy) {
        cube.reset();
        if (moveDisplay) moveDisplay.textContent = '';
      }
    });
  }

  // Keyboard controls
  const keyMap = {
    r: 'R', R: "R'",
    l: 'L', L: "L'",
    u: 'U', U: "U'",
    d: 'D', D: "D'",
    f: 'F', F: "F'",
    b: 'B', B: "B'",
  };

  document.addEventListener('keydown', (e) => {
    // Ignore if typing in an input
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

    const move = keyMap[e.key];
    if (move) {
      animator.enqueue(move);
    }
    if (e.key === 's') {
      const scramble = generateScramble(20);
      animator.enqueue(scramble);
    }
  });

  return orbit;
}
