## Newton's Method

### Overview
Newton's method (also known as the Newton-Raphson method) is a powerful root-finding algorithm that uses the first derivative of a function to find better approximations of the roots of a real-valued function. It's known for its quadratic convergence rate, making it much faster than methods like bisection when it converges.

### Mathematical Background
For a differentiable function f(x), Newton's method uses the tangent line at the current approximation to find the next approximation.

The algorithm works as follows:
1. Start with an initial guess x₀
2. Calculate the next approximation using the formula: x_{n+1} = x_n - f(x_n) / f'(x_n)
3. If |f(x_{n+1})| or |x_{n+1} - x_n| is sufficiently small, x_{n+1} is the approximate root
4. Otherwise, repeat steps 2-3 with the new approximation until convergence or maximum iterations

### Implementation C
The implementation can be found in `newton.c`. The current version solves the equation x³ - 8 = 0, finding the cube root of 8.
### Implementation Python
The implementation can be found in `newton.py`. User inputs solved equation and its derivative

### Building and Running

#### Using Make
A Makefile is provided for easy compilation:
# Compile the program
make

# Run the program
make run

# Clean built files
make clean

#### Manual Compilation
If you prefer to compile manually:

```bash
gcc -Wall -o newton newton.c -lm
./newton
```
### Running Python
python newton.py

