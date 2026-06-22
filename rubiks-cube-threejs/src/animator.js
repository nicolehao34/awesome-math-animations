import * as THREE from 'three';
import { MOVES } from './moves.js';

/**
 * Animator handles queued face rotations with smooth tweening.
 */
export class Animator {
  constructor(cube, scene, onMoveStart) {
    this.cube = cube;
    this.scene = scene;
    this.onMoveStart = onMoveStart || (() => {});
    this.queue = [];
    this.isAnimating = false;
    this.duration = 300; // ms per move
    this.pivot = null;
    this.currentMove = null;
    this.startAngle = 0;
    this.targetAngle = 0;
    this.elapsed = 0;
    this.rotationAxis = null;
  }

  /**
   * Add one or more moves to the queue.
   * @param {string|string[]} moves
   */
  enqueue(moves) {
    if (typeof moves === 'string') moves = [moves];
    this.queue.push(...moves);
    if (!this.isAnimating) {
      this.next();
    }
  }

  /**
   * Process the next move in the queue.
   */
  next() {
    if (this.queue.length === 0) {
      this.isAnimating = false;
      return;
    }

    this.isAnimating = true;
    const moveName = this.queue.shift();
    const moveDef = MOVES[moveName];
    if (!moveDef) {
      this.next();
      return;
    }

    this.onMoveStart(moveName);
    this.currentMove = moveDef;
    this.rotationAxis = moveDef.axis.clone();
    this.targetAngle = moveDef.angle;
    this.elapsed = 0;

    // Create pivot and attach cubies
    this.pivot = new THREE.Group();
    this.scene.add(this.pivot);

    const cubies = this.cube.getFaceCubies(moveDef.face);
    for (const cubie of cubies) {
      this.pivot.attach(cubie);
    }
  }

  /**
   * Called every frame with delta time in ms. Returns true if animating.
   */
  update(deltaMs) {
    if (!this.isAnimating || !this.pivot) return false;

    this.elapsed += deltaMs;
    const t = Math.min(this.elapsed / this.duration, 1);

    // Ease in-out cubic
    const eased = t < 0.5
      ? 4 * t * t * t
      : 1 - Math.pow(-2 * t + 2, 3) / 2;

    const angle = this.targetAngle * eased;

    // Apply rotation to pivot
    this.pivot.rotation.set(0, 0, 0);
    this.pivot.rotateOnAxis(this.rotationAxis, angle);

    if (t >= 1) {
      this.finishMove();
    }

    return true;
  }

  /**
   * Finalize the current move: detach cubies, remove pivot.
   */
  finishMove() {
    // Apply final rotation exactly
    this.pivot.rotation.set(0, 0, 0);
    this.pivot.rotateOnAxis(this.rotationAxis, this.targetAngle);
    this.pivot.updateMatrixWorld(true);

    // Detach cubies back to the cube group
    const children = [...this.pivot.children];
    for (const cubie of children) {
      this.cube.group.attach(cubie);
    }

    // Clean up pivot
    this.scene.remove(this.pivot);
    this.pivot = null;
    this.currentMove = null;

    // Round cubie positions to avoid floating-point drift
    for (const cubie of this.cube.cubies) {
      cubie.position.x = Math.round(cubie.position.x);
      cubie.position.y = Math.round(cubie.position.y);
      cubie.position.z = Math.round(cubie.position.z);
    }

    // Process next move
    this.next();
  }

  /**
   * Check if currently busy animating.
   */
  get busy() {
    return this.isAnimating;
  }

  /**
   * Set animation speed (ms per move).
   */
  setSpeed(ms) {
    this.duration = ms;
  }
}
