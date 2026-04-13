#!/usr/bin/env python3
"""
Rubik's Cube Permutation Mathematics

This module demonstrates how Rubik's cube moves are permutations
and how they form a group structure.
"""

from manim import *
import numpy as np
from itertools import permutations as iter_perms


class Permutation:
    """
    A permutation object for Rubik's cube mathematics.
    
    Permutations can be represented in multiple ways:
    1. Cycle notation: (1 2 3)(4 5) means 1→2, 2→3, 3→1, 4→5, 5→4
    2. Array notation: [2, 3, 1, 5, 4] means position 0→2, 1→3, etc.
    3. Two-line notation: Shows input and output explicitly
    """
    
    def __init__(self, mapping):
        """
        Initialize a permutation.
        
        Args:
            mapping: List or dict representing the permutation
                    [1, 0, 3, 2] means 0→1, 1→0, 2→3, 3→2
        """
        if isinstance(mapping, dict):
            n = max(max(mapping.keys()), max(mapping.values())) + 1
            self.mapping = [mapping.get(i, i) for i in range(n)]
        else:
            self.mapping = list(mapping)
        
        self.size = len(self.mapping)
    
    def __call__(self, i):
        """Apply the permutation: returns where element i goes."""
        return self.mapping[i]
    
    def __mul__(self, other):
        """
        Compose two permutations (self ∘ other).
        (f ∘ g)(x) means "apply g first, then f"
        """
        if isinstance(other, Permutation):
            new_mapping = [self.mapping[other.mapping[i]] for i in range(self.size)]
            return Permutation(new_mapping)
        else:
            raise TypeError("Can only multiply with another Permutation")
    
    def inverse(self):
        """Get the inverse permutation."""
        inv_mapping = [0] * self.size
        for i, val in enumerate(self.mapping):
            inv_mapping[val] = i
        return Permutation(inv_mapping)
    
    def order(self):
        """
        Calculate the order of this permutation.
        Order = smallest positive integer k such that p^k = identity
        """
        current = Permutation(list(range(self.size)))
        count = 0
        
        while True:
            count += 1
            current = self * current
            if current.mapping == list(range(self.size)):
                return count
            if count > 1000:  # Safety limit
                return float('inf')
    
    def to_cycles(self):
        """
        Convert to cycle notation.
        Returns: List of cycles, e.g., [(0, 1, 2), (3, 4)]
        """
        visited = [False] * self.size
        cycles = []
        
        for start in range(self.size):
            if visited[start]:
                continue
            
            cycle = []
            current = start
            
            while not visited[current]:
                visited[current] = True
                cycle.append(current)
                current = self.mapping[current]
            
            # Only include non-trivial cycles (length > 1)
            if len(cycle) > 1:
                cycles.append(tuple(cycle))
        
        return cycles
    
    def __repr__(self):
        cycles = self.to_cycles()
        if not cycles:
            return "()"
        return "".join(f"({' '.join(map(str, cycle))})" for cycle in cycles)
    
    def __eq__(self, other):
        return self.mapping == other.mapping


class RubikPermutations:
    """
    Defines the basic permutations for Rubik's cube moves.
    
    Each face turn is a permutation of the 48 colored stickers:
    - 6 faces × 8 positions = 48 stickers (excluding centers)
    
    For simplicity, we'll track the 8 corners and 12 edges separately.
    """
    
    @staticmethod
    def get_r_move():
        """
        Right face clockwise (R move).
        
        This permutation affects:
        - 4 corner pieces: cycle them around the right face
        - 4 edge pieces: cycle them around the right face
        """
        # Simplified: just showing the mathematical concept
        # In reality, this would track all 20 movable pieces
        corners = list(range(8))
        # R move cycles corners: 1→2→6→5→1
        corners[1], corners[2], corners[6], corners[5] = corners[5], corners[1], corners[2], corners[6]
        return Permutation(corners + list(range(8, 20)))  # Edges unchanged for simplicity
    
    @staticmethod
    def get_u_move():
        """Up face clockwise (U move)."""
        corners = list(range(8))
        # U move cycles corners: 0→1→2→3→0
        corners[0], corners[1], corners[2], corners[3] = corners[3], corners[0], corners[1], corners[2]
        return Permutation(corners + list(range(8, 20)))
    
    @staticmethod
    def get_f_move():
        """Front face clockwise (F move)."""
        corners = list(range(8))
        # F move cycles corners: 0→3→7→4→0
        corners[0], corners[3], corners[7], corners[4] = corners[4], corners[0], corners[3], corners[7]
        return Permutation(corners + list(range(8, 20)))
    
    @staticmethod
    def commutator(a, b):
        """
        Calculate the commutator [A, B] = ABA'B'
        
        The commutator measures how much two permutations "don't commute".
        If [A, B] = identity, then AB = BA (they commute).
        
        Commutators are fundamental to solving algorithms!
        """
        a_inv = a.inverse()
        b_inv = b.inverse()
        return a * b * a_inv * b_inv
    
    @staticmethod
    def conjugate(a, b):
        """
        Calculate the conjugate ABA'.
        
        Conjugation "repositions" a move. It's like:
        1. Move to a different position (A)
        2. Do the move (B)
        3. Move back (A')
        
        Used extensively in solving to affect different pieces with the same algorithm.
        """
        a_inv = a.inverse()
        return a * b * a_inv


def demonstrate_cycle_notation():
    """
    Educational function showing cycle notation.
    
    Example: (1 2 3)(4 5) means:
    - 1 goes to 2
    - 2 goes to 3
    - 3 goes to 1
    - 4 goes to 5
    - 5 goes to 4
    - Everything else stays put
    """
    # Simple 3-cycle
    perm = Permutation([1, 2, 0, 3, 4, 5])  # (0 1 2)
    print(f"Permutation [1, 2, 0, 3, 4, 5] in cycle notation: {perm}")
    print(f"Order (how many times to repeat to get identity): {perm.order()}")
    
    # Composition
    perm2 = Permutation([0, 2, 1, 3, 4, 5])  # (1 2)
    composition = perm * perm2
    print(f"\n(0 1 2) ∘ (1 2) = {composition}")
    
    # Inverse
    print(f"\nInverse of (0 1 2): {perm.inverse()}")
    
    # Commutator
    comm = RubikPermutations.commutator(perm, perm2)
    print(f"\nCommutator [(0 1 2), (1 2)]: {comm}")


def demonstrate_rubiks_group():
    """
    The Rubik's cube group has fascinating properties:
    
    - Size: ~4.3 × 10^19 (43 quintillion) positions
    - God's Number: 20 (max moves needed to solve any position)
    - Generators: 6 basic moves {R, L, U, D, F, B}
    - Subgroups: Many interesting structures
    """
    print("\n=== The Rubik's Cube Group ===")
    print("Group elements: ~43 quintillion cube positions")
    print("Identity: Solved cube")
    print("Generators: R, L, U, D, F, B (6 face turns)")
    print("Closure: Any sequence of moves gives a valid position")
    print("Inverses: Every move can be undone (R has inverse R')")
    print("Associativity: (AB)C = A(BC)")
    
    # Show orders of basic moves
    r_move = RubikPermutations.get_r_move()
    print(f"\nOrder of R move: {r_move.order()} (repeating 4 times returns to start)")


def demonstrate_parity():
    """
    Parity constraints on the Rubik's cube:
    
    1. Can't swap exactly two corners
    2. Can't swap exactly two edges
    3. Can't flip exactly one edge
    4. Can't twist exactly one corner
    5. Edge permutation and corner permutation have same parity
    
    These are mathematical impossibilities - no sequence of legal moves can achieve them!
    """
    print("\n=== Parity Constraints ===")
    print("The following are IMPOSSIBLE on a Rubik's cube:")
    print("❌ Swap only two corner pieces")
    print("❌ Swap only two edge pieces")
    print("❌ Flip only one edge piece")
    print("❌ Twist only one corner piece")
    print("\nWhy? The group structure forbids it!")
    print("All legal moves are EVEN permutations.")


if __name__ == "__main__":
    print("=== Rubik's Cube Permutation Mathematics ===\n")
    demonstrate_cycle_notation()
    demonstrate_rubiks_group()
    demonstrate_parity()
