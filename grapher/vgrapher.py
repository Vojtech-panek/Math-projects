# Author: Vojtěch Pánek
# Purpose: Graphing 3D and 2D vector functions
# Example input: r(t) = <2*t, t, ln(t)>  → user inputs 2*t, t, np.log(t)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to evaluate the function from text input
def evaluate_function(func_str):
    """Convert text to a function that computes the value at point t."""
    # Replace common math functions with numpy equivalents
    replacements = {
        'cos': 'np.cos',
        'sin': 'np.sin',
        'tan': 'np.tan',
        'exp': 'np.exp',
        'log': 'np.log10',
        'ln': 'np.log',
        'sqrt': 'np.sqrt',
        'abs': 'np.abs',
        'pi': 'np.pi',
        'e': 'np.e'
    }
    
    # Apply replacements
    for old, new in replacements.items():
        if old in func_str:
            func_str = func_str.replace(old, new)
    
    # Create and return the lambda function
    return lambda t: eval(func_str)

# Get components from user
print("Zadejte parametrickou funkci r(t) = <x(t), y(t), z(t)>")
x_input = input("Zadejte složku x(t): ")
y_input = input("Zadejte složku y(t): ")
z_input = input("Zadejte složku z(t): ")

# Evaluate functions
x_func = evaluate_function(x_input)
y_func = evaluate_function(y_input)
z_func = evaluate_function(z_input)

# Function for r(t) with the given components
def r(t, x_func, y_func, z_func):
    return np.array([x_func(t), y_func(t), z_func(t)])

# Create array of t values
t_min = 0.1  # Default minimum t value
t_max = 10.0  # Default maximum t value

try:
    t_min = float(input("Zadejte minimální hodnotu t (výchozí 0.1): ") or t_min)
    t_max = float(input("Zadejte maximální hodnotu t (výchozí 10.0): ") or t_max)
except ValueError:
    print("Neplatná hodnota, použity výchozí hodnoty.")

t_values = np.linspace(t_min, t_max, 500)

# Use the r(t) function for each t
r_t_values = np.array([r(t, x_func, y_func, z_func) for t in t_values])

# Extract components
x_values = r_t_values[:, 0]
y_values = r_t_values[:, 1]
z_values = r_t_values[:, 2]

# Plot 3D curve
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x_values, y_values, z_values, label=r'$\mathbf{r}(t)$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add start and end points
ax.plot([x_values[0]], [y_values[0]], [z_values[0]], 'go', label=f'Start (t={t_min})')
ax.plot([x_values[-1]], [y_values[-1]], [z_values[-1]], 'ro', label=f'End (t={t_max})')

# Set title with the function
ax.set_title(f'r(t) = <{x_input}, {y_input}, {z_input}>')

# Add legend
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
