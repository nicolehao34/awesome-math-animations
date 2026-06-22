import * as THREE from 'three';

/**
 * Standard Rubik's cube color scheme.
 */
const COLORS = {
  R: 0x0045ad, // Blue (Right)
  L: 0x009b48, // Green (Left)
  U: 0xffffff, // White (Up)
  D: 0xffd500, // Yellow (Down)
  F: 0xb90000, // Red (Front)
  B: 0xff5900, // Orange (Back)
  interior: 0x111111,
};

/**
 * Face index mapping for BoxGeometry.
 * BoxGeometry creates faces in order: +x, -x, +y, -y, +z, -z
 * Each face has 2 triangles (so material indices 0-5 map to these faces).
 */
const FACE_MATERIAL_INDEX = {
  R: 0, // +x
  L: 1, // -x
  U: 2, // +y
  D: 3, // -y
  F: 4, // +z
  B: 5, // -z
};

/**
 * Creates a single cubie mesh with appropriately colored faces.
 */
function createCubie(x, y, z) {
  const size = 0.93;
  const geometry = new THREE.BoxGeometry(size, size, size);

  // Determine which faces are on the exterior
  const materials = [];
  // +x face (Right)
  materials.push(new THREE.MeshStandardMaterial({
    color: x === 1 ? COLORS.R : COLORS.interior,
  }));
  // -x face (Left)
  materials.push(new THREE.MeshStandardMaterial({
    color: x === -1 ? COLORS.L : COLORS.interior,
  }));
  // +y face (Up)
  materials.push(new THREE.MeshStandardMaterial({
    color: y === 1 ? COLORS.U : COLORS.interior,
  }));
  // -y face (Down)
  materials.push(new THREE.MeshStandardMaterial({
    color: y === -1 ? COLORS.D : COLORS.interior,
  }));
  // +z face (Front)
  materials.push(new THREE.MeshStandardMaterial({
    color: z === 1 ? COLORS.F : COLORS.interior,
  }));
  // -z face (Back)
  materials.push(new THREE.MeshStandardMaterial({
    color: z === -1 ? COLORS.B : COLORS.interior,
  }));

  const mesh = new THREE.Mesh(geometry, materials);
  mesh.position.set(x, y, z);
  return mesh;
}

/**
 * RubiksCube builds and manages the 27-cubie model.
 */
export class RubiksCube {
  constructor(scene) {
    this.scene = scene;
    this.cubies = [];
    this.group = new THREE.Group();
    this.build();
    this.scene.add(this.group);
  }

  build() {
    for (let x = -1; x <= 1; x++) {
      for (let y = -1; y <= 1; y++) {
        for (let z = -1; z <= 1; z++) {
          const cubie = createCubie(x, y, z);
          this.cubies.push(cubie);
          this.group.add(cubie);
        }
      }
    }
  }

  /**
   * Returns the array of cubies belonging to the given face,
   * based on their current world position.
   */
  getFaceCubies(face) {
    const threshold = 0.5;
    const checks = {
      R: (p) => p.x > threshold,
      L: (p) => p.x < -threshold,
      U: (p) => p.y > threshold,
      D: (p) => p.y < -threshold,
      F: (p) => p.z > threshold,
      B: (p) => p.z < -threshold,
    };

    const check = checks[face];
    if (!check) return [];

    const result = [];
    for (const cubie of this.cubies) {
      const worldPos = new THREE.Vector3();
      cubie.getWorldPosition(worldPos);
      if (check(worldPos)) {
        result.push(cubie);
      }
    }
    return result;
  }

  /**
   * Reset cube to solved state by removing all cubies and rebuilding.
   */
  reset() {
    while (this.group.children.length > 0) {
      this.group.remove(this.group.children[0]);
    }
    this.cubies = [];
    this.build();
  }
}
