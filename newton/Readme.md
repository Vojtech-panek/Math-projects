# Newton-Raphson Method Implementation

This project implements the Newton-Raphson method for finding roots of a real-valued function in both C and Python. The Newton-Raphson method is an iterative numerical technique that uses function derivatives to approximate solutions of equations in the form f(x) = 0.

## Algorithm Overview

The Newton-Raphson method works as follows:

1. Start with an initial guess x₀
2. Compute the function value f(x₀) and its derivative f'(x₀)
3. Calculate the next approximation: xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)
4. Repeat steps 2-3 until convergence or maximum iterations

## Mathematical Background

The method is based on the linear approximation of the function at the current point. Using the tangent line at the current approximation, we find its intersection with the x-axis and use that as the next approximation.

The convergence of the Newton-Raphson method is quadratic when:
- The function is continuously differentiable
- The derivative doesn't vanish at the root
- The initial guess is sufficiently close to the root

## Implementations

### Python Implementation

The Python implementation:
- Takes user input for the function and its derivative in Python syntax
- Allows specification of initial guess, tolerance, and maximum iterations
- Reports when a solution is found or why the method failed
- Handles cases where the derivative becomes zero
- Uses dynamic evaluation of mathematical expressions

### C Implementation

The C implementation:
- Requires the function and its derivative to be defined in the source code
- Provides efficient calculation with lower overhead
- Uses command-line arguments for initial guess, tolerance, and maximum iterations
- Implements rigorous error checking and handling
- Can be compiled for various platforms

## Usage

### Python Version

Run the Python script and follow the prompts:

```
python newton.py
Enter the function: x**2 - 4
Enter the derivative of the function: 2*x
Enter the initial guess: 3
Enter the number of iterations: 10
Enter the tolerance: 1e-6
```

### C Version

# Compile the program
make

# Run the program
make run

# Clean built files
make clean
```

Where the arguments are:
1. Initial guess
2. Maximum number of iterations
3. Tolerance

## Example Functions

Here are some functions you can try:

1. Finding square root of a number:
   - Function: `x**2 - a` (replace `a` with the number)
   - Derivative: `2*x`

2. Solving cubic equation:
   - Function: `x**3 - 2*x - 5`
   - Derivative: `3*x**2 - 2`

3. Trigonometric equation:
   - Function: `sin(x) - 0.5`
   - Derivative: `cos(x)`

## Limitations

- The method may not converge if the initial guess is too far from the root
- Fails if the derivative becomes zero during iterations
- May enter an infinite loop for certain functions (handled by max iterations)
- Multiple roots require multiple runs with different initial guesses
- The C implementation requires modifying source code to change the function

## Future Improvements

- Visualization of the convergence process
- Automatic differentiation to avoid manual derivative input
- Support for complex roots
- Implementation of modified Newton methods for higher-order convergence
- Function parser for the C implementation
