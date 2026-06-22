import * as THREE from 'three';
import { RubiksCube } from './cube.js';
import { Animator } from './animator.js';
import { setupControls } from './controls.js';

// ——— Scene Setup ———
const canvas = document.getElementById('cube-canvas');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(canvas.clientWidth, canvas.clientHeight);

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x1a1a2e);

// Camera
const camera = new THREE.PerspectiveCamera(
  45,
  canvas.clientWidth / canvas.clientHeight,
  0.1,
  100
);
camera.position.set(4, 3, 5);
camera.lookAt(0, 0, 0);

// Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(5, 10, 7);
scene.add(directionalLight);

const fillLight = new THREE.DirectionalLight(0xffffff, 0.3);
fillLight.position.set(-5, -3, -5);
scene.add(fillLight);

// ——— Cube ———
const cube = new RubiksCube(scene);

// ——— Animator ———
const animator = new Animator(cube, scene);

// ——— Controls ———
const orbit = setupControls(camera, renderer, animator, cube);

// ——— Render Loop ———
const clock = new THREE.Clock();

function animate() {
  requestAnimationFrame(animate);

  const deltaMs = clock.getDelta() * 1000;
  animator.update(deltaMs);
  orbit.update();

  renderer.render(scene, camera);
}

animate();

// ——— Resize Handling ———
function onResize() {
  const width = canvas.clientWidth;
  const height = canvas.clientHeight;
  renderer.setSize(width, height, false);
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
}

window.addEventListener('resize', onResize);
// Initial size sync
onResize();
