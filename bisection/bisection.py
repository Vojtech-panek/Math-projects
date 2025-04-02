fx=input('Enter the function: ')
a=float(input('Enter leftbound: '))
b=float(input('Enter rightbound: '))
n=int(input('Enter the number of iterations: '))
e= float(input('Enter the tolerance: '))
fx = eval(f"lambda x: {fx}")

def Bisection(fx, a, b, n, e):
    # Initialize variables
    fa = fx(a)
    fb = fx(b)
    
    # Helper function to determine sign
    def sign(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        return 0
    
    # Check if the interval brackets a root
    if sign(fa) == sign(fb):
        print(f"a= {a} b= {b} f(a)= {fa} f(b)= {fb}")
        print("Function has the same sign in a and b")
        return None
    
    # Initial error is the width of the interval
    error = b - a
    # Output header
    print("n=  c=  f(c)=   error=  ")
    
    # Main bisection iteration loop
    for i in range(n):
        error = error / 2           # Error is halved in each iteration
        c = a + error               # New midpoint
        fc = fx(c)                  # Evaluate function at midpoint
        
        # Output current iteration data
        print(f"{i}  {c}  {fc}  {error}")
        
        # Check for convergence based on interval width
        if abs(error) < e:
            print("Convergence")
            return c
        
        # Update the interval [a, b] for the next iteration
        if sign(fc) == sign(fa):   # If f(c) and f(a) have the same sign
            a = c                  # Move left endpoint to c
            fa = fc                # Update function value at a
        else:                      # If f(c) and f(a) have different signs
            b = c                  # Move right endpoint to c
            fb = fc                # Update function value at b
    
    return c  # Return the final approximation

# Test the Bisection function with user input
result = Bisection(fx, a, b, n, e)
if result is not None:
    print(f"Approximate root: {result}")



