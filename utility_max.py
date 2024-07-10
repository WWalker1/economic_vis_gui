import numpy as np
import matplotlib.pyplot as plt

def optimal_bundle(a, b, px, py, constraint, constraint_type='budget'):
    """
    Calculate the optimal consumption bundle for a Cobb-Douglas utility function.
    
    Args:
    a, b: Cobb-Douglas utility function parameters
    px, py: Prices of goods X and Y
    constraint: Budget constraint or utility level
    constraint_type: 'budget' or 'utility'
    
    Returns:
    Tuple of optimal X and Y quantities
    """
    if constraint_type == 'budget':
        x = (a / (a + b)) * (constraint / px)
        y = (b / (a + b)) * (constraint / py)
    else:  # utility constraint
        k = constraint ** (1 / (a + b))
        x = k * (a * py / (b * px)) ** (b / (a + b))
        y = k * (b * px / (a * py)) ** (a / (a + b))
    
    return x, y

def calculate_utility(x, y, a, b):
    """
    Calculate utility for a Cobb-Douglas utility function.
    
    Args:
    x, y: Quantities of goods X and Y
    a, b: Cobb-Douglas utility function parameters
    
    Returns:
    Utility value
    """
    return x**a * y**b


# Example usage:
optimal_x, optimal_y = optimal_bundle(0.5, 0.5, 2, 3, 100, 'budget')
utility = calculate_utility(optimal_x, optimal_y, 0.5, 0.5)

print(utility)


def plot_indifference_curves(a, b, utilities, x_range, num_points=100):
    """
    Plot indifference curves for a Cobb-Douglas utility function.
    
    Args:
    a, b: Cobb-Douglas utility function parameters
    utilities: List of utility levels to plot
    x_range: Tuple of (min_x, max_x) for the x-axis
    num_points: Number of points to calculate for each curve
    """
    x = np.linspace(x_range[0], x_range[1], num_points)
    
    plt.figure(figsize=(10, 6))
    for u in utilities:
        y = (u / (x**a))**(1/b)
        plt.plot(x, y, label=f'U = {u:.2f}')
    
    plt.xlabel('Good X')
    plt.ylabel('Good Y')
    plt.title('Indifference Curves')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
a, b = 0.5, 0.5
utilities = [10, 20, 30, 40, 50]
x_range = (0.1, 10)
plot_indifference_curves(a, b, utilities, x_range)