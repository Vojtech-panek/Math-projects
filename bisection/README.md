# Numerické Algoritmy (Numerical Algorithms)

This repository contains implementations of various numerical algorithms for solving mathematical problems.

## Bisection Method

### Overview
The bisection method is a root-finding algorithm that repeatedly bisects an interval and then selects a subinterval in which a root must lie for further processing. It is a simple and robust method, although it converges slowly.

### Mathematical Background
For a continuous function f(x), if f(a) and f(b) have opposite signs, then by the Intermediate Value Theorem, there exists at least one root in the interval [a, b].

The algorithm works as follows:
1. Start with an interval [a, b] where f(a) and f(b) have opposite signs
2. Calculate the midpoint c = (a + b) / 2
3. If f(c) is sufficiently close to zero, c is the approximate root
4. Otherwise, create a new interval:
   - If f(c) and f(a) have the same sign, the root is in [c, b]
   - If f(c) and f(a) have opposite signs, the root is in [a, c]
5. Repeat steps 2-4 until convergence or maximum iterations

### Implementation
The implementation can be found in `bisection.c`. The current version solves the equation x³ - 2 = 0, finding the cube root of 2.

### Complexity
- Time Complexity: O(log((b-a)/ε)), where ε is the desired precision
- Space Complexity: O(1)

### Building and Running

#### Using Make
A Makefile is provided for easy compilation:

```bash
# Compile the program
make

# Run the program
make run

# Clean built files
make clean
```

#### Manual Compilation
If you prefer to compile manually:

```bash
gcc -Wall -o bisection bisection.c -lm
./bisection
```

### Customization
You can modify the function `func()` in the source code to solve different equations.

## Other Algorithms
More algorithms will be added in the future.
