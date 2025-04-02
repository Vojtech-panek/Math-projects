#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function pointer types for the function and its derivative
typedef double (*Function)(double);

// Function to implement the Newton-Raphson method
double NewtonRaphson(Function fx, Function fd, double x0, int n, double e) {
    double xn = x0;  // Initialize the current approximation with the initial guess
    
    for (int i = 0; i < n; i++) {
        double fxn = fx(xn);  // Evaluate the function at the current point
        double fdxn = fd(xn);  // Evaluate the derivative at the current point
        
        if (fabs(fxn) < e) {  // Check if we've reached the desired accuracy
            printf("Root found: %lf\n", xn);
            return xn;
        }
        
        if (fdxn == 0) {  // Check if the derivative is zero (to avoid division by zero)
            printf("Derivative is zero. No solution found.\n");
            return xn;  // Return current value since we can't continue
        }
        
        xn = xn - fxn / fdxn;  // Newton-Raphson formula: x_n+1 = x_n - f(x_n)/f'(x_n)
    }
    
    // If the maximum number of iterations is reached without convergence
    printf("Method did not converge after %d iterations. Last value: %lf\n", n, xn);
    return xn;
}

// Example function: f(x) = x^2 - 4
double function(double x) {
    return x*x - 4;
}

// Example derivative: f'(x) = 2x
double derivative(double x) {
    return 2*x;
}

int main() {
    // Declare variables
    double x0, e;
    int n;
    int scan_result;
    
    // Get user input
    printf("Enter the initial guess: ");
    scan_result = scanf("%lf", &x0);
    if (scan_result != 1) {
        printf("Error: Invalid input for initial guess.\n");
        return 1;
    }
    
    printf("Enter the number of iterations: ");
    scan_result = scanf("%d", &n);
    if (scan_result != 1) {
        printf("Error: Invalid input for number of iterations.\n");
        return 1;
    }
    
    printf("Enter the tolerance: ");
    scan_result = scanf("%lf", &e);
    if (scan_result != 1) {
        printf("Error: Invalid input for tolerance.\n");
        return 1;
    }
    
    // Note to the user about the function
    printf("Using function f(x) = x^2 - 4 and its derivative f'(x) = 2x\n");
    printf("To use a different function, modify the 'function' and 'derivative' functions in the code.\n\n");
    
    // Execute the Newton-Raphson method with the provided inputs
    NewtonRaphson(function, derivative, x0, n, e);
    
    return 0;
}
