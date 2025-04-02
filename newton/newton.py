# Get user input for the function and its parameters
fx=input('Enter the function: ')  # String representation of the function f(x)
fd=input('Enter the derivative of the function: ')  # String representation of the derivative f'(x)
x0=float(input('Enter the initial guess: '))  # Initial approximation for the root
n=int(input('Enter the number of iterations: '))  # Maximum number of iterations
e= float(input('Enter the tolerance: '))  # Error tolerance for stopping criterion

# Convert string representations to lambda functions
fx = eval(f"lambda x: {fx}")  # Convert function string to callable function
fd = eval(f"lambda x: {fd}")  # Convert derivative string to callable function

def NewtonRaphson(fx, fd, x0, n, e):
    """
    Newton-Raphson method for finding roots of a function.
    
    Parameters:
    fx -- the function whose root we want to find
    fd -- derivative of the function fx
    x0 -- initial guess for the root
    n -- maximum number of iterations
    e -- tolerance for convergence
    
    Returns:
    xn -- approximation of the root, or None if the method fails
    """
    xn = x0  # Initialize the current approximation with the initial guess
    for i in range(n):
        fxn = fx(xn)  # Evaluate the function at the current point
        fdxn = fd(xn)  # Evaluate the derivative at the current point
        
        if abs(fxn) < e:  # Check if we've reached the desired accuracy
            print(f"Root found: {xn}")
            return xn
            
        if fdxn == 0:  # Check if the derivative is zero (to avoid division by zero)
            print("Derivative is zero. No solution found.")
            return None
            
        xn = xn - fxn / fdxn  # Newton-Raphson formula: x_n+1 = x_n - f(x_n)/f'(x_n)
    
    # If the maximum number of iterations is reached without convergence
    print(f"Method did not converge after {n} iterations. Last value: {xn}")
    return xn

# Execute the Newton-Raphson method with the provided inputs
result = NewtonRaphson(fx, fd, x0, n, e)