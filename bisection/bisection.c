/*
* bisection.c
*
* Program for finding approximated solution of equation f(x) = 0 using the bisection method.
* The bisection method works by repeatedly dividing an interval and selecting the subinterval
* where the function changes sign, thus containing a root.
*
* Current implementation solves: x³ - 2 = 0 (cube root of 2)
*
* Author: Vojtěch Pánek
*/
#include <stdio.h>

// Function prototypes
double func(double x);    // The function whose root we want to find
int sign(double x);       // Returns the sign of a number (-1, 0, or 1)
double absa(double x);    // Absolute value function

int main(void)
{
    // Initial interval [a, b] must bracket a root (f(a) and f(b) have opposite signs)
    double a = 1;           // Left bound of the interval
    double b = 2;           // Right bound of the interval
    double c = 0;           // Middle point (where we approximate the root)

    double fa = 0;          // Function value at a: f(a)
    double fb = 0;          // Function value at b: f(b)
    double fc = 0;          // Function value at c: f(c)

    double error = 0;       // Current error estimation
    double eps = 0.5e-16;   // Desired precision (stopping criterion)

    double n = 20;          // Maximum number of iterations

    // Evaluate function at interval endpoints
    fa = func(a);
    fb = func(b);
    
    // Check if the interval brackets a root
    if(sign(fa) == sign(fb)) {
        printf(" a= %f b= %f  f(a)= %f f(b)= %f", a, b, fa, fb);
        printf("Function has the same sign in a and b\n");
        return 0;
    }
    
    // Initial error is the width of the interval
    error = b - a;
    // Output current iteration data
    printf("n=  c=  f(c)=   error=  \n");
    // Main bisection iteration loop
    for(int i = 0; i < n; i++) {
        error = error / 2;           // Error is halved in each iteration
        c = a + error;               // New midpoint (asymmetric to ensure proper convergence)
        fc = func(c);                // Evaluate function at midpoint
        
        // Output current iteration data
        printf("%d  %f  %f  %f  \n", i, c, fc, error);
        
        // Check for convergence based on interval width
        if(absa(error) < eps) {
            printf("Convergence\n");
            return 0;
        }
        
        // Update the interval [a, b] for the next iteration
        if(sign(fc) == sign(fa)) {   // If f(c) and f(a) have the same sign
            a = c;                   // Move left endpoint to c
            fa = fc;                 // Update function value at a
        } else {                     // If f(c) and f(a) have different signs
            b = c;                   // Move right endpoint to c
            fb = fc;                 // Update function value at b
        }
    }
    
    return 0;
}

/**
 * The function whose root we want to find.
 * Current implementation: f(x) = x³ - 2
 * (finding the cube root of 2)
 */
double func(double x) {
    return x*x*x - 2;
}

/**
 * Returns the sign of a number:
 * 1 for positive numbers,
 * -1 for negative numbers,
 * 0 for zero.
 */
int sign(double x) {
    if (x > 0) return 1;
    if (x < 0) return -1;
    return 0;
}

/**
 * Returns the absolute value of a number.
 */
double absa(double x) {
    if (x < 0) return -x;
    return x;
}