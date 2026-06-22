import * as THREE from 'three';

/**
 * Move definitions: maps move name → { face, axis, angle }
 *
 * Axis is the THREE.Vector3 direction for the rotation.
 * Angle is +π/2 or -π/2 depending on direction.
 *
 * Convention (looking at the face):
 *   Clockwise = negative rotation around the face's outward axis
 */
export const MOVES = {
  R:  { face: 'R', axis: new THREE.Vector3(1, 0, 0), angle: -Math.PI / 2 },
  "R'": { face: 'R', axis: new THREE.Vector3(1, 0, 0), angle: Math.PI / 2 },
  L:  { face: 'L', axis: new THREE.Vector3(1, 0, 0), angle: Math.PI / 2 },
  "L'": { face: 'L', axis: new THREE.Vector3(1, 0, 0), angle: -Math.PI / 2 },
  U:  { face: 'U', axis: new THREE.Vector3(0, 1, 0), angle: -Math.PI / 2 },
  "U'": { face: 'U', axis: new THREE.Vector3(0, 1, 0), angle: Math.PI / 2 },
  D:  { face: 'D', axis: new THREE.Vector3(0, 1, 0), angle: Math.PI / 2 },
  "D'": { face: 'D', axis: new THREE.Vector3(0, 1, 0), angle: -Math.PI / 2 },
  F:  { face: 'F', axis: new THREE.Vector3(0, 0, 1), angle: -Math.PI / 2 },
  "F'": { face: 'F', axis: new THREE.Vector3(0, 0, 1), angle: Math.PI / 2 },
  B:  { face: 'B', axis: new THREE.Vector3(0, 0, 1), angle: Math.PI / 2 },
  "B'": { face: 'B', axis: new THREE.Vector3(0, 0, 1), angle: -Math.PI / 2 },
};

/** All valid move names */
export const MOVE_NAMES = Object.keys(MOVES);

/**
 * Generate a random scramble of `length` moves.
 */
export function generateScramble(length = 20) {
  const scramble = [];
  let lastFace = '';

  for (let i = 0; i < length; i++) {
    let move;
    do {
      move = MOVE_NAMES[Math.floor(Math.random() * MOVE_NAMES.length)];
    } while (MOVES[move].face === lastFace); // avoid consecutive same-face moves

    scramble.push(move);
    lastFace = MOVES[move].face;
  }

  return scramble;
}
