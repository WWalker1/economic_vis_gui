import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

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

def calculate_cost(x, y, px, py):
    """
    Calculate the total cost of a bundle of goods.
    
    Args:
    x, y: Quantities of goods X and Y
    px, py: Prices of goods X and Y
    
    Returns:
    Total cost
    """
    return x * px + y * py


def plot_budget_line(px, py, budget, x_range, ax=None):
    """
    Plot a budget line.
    
    Args:
    px, py: Prices of goods X and Y
    budget: Total budget
    x_range: Tuple of (min_x, max_x) for the x-axis
    ax: Matplotlib axis to plot on (optional)
    
    Returns:
    Matplotlib axis object
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.linspace(x_range[0], x_range[1], 100)
    y = (budget - px * x) / py
    
    ax.plot(x, y, label=f'Budget Line (Budget: {budget})')
    ax.set_xlabel('Good X')
    ax.set_ylabel('Good Y')
    ax.set_title('Budget Line')
    ax.legend()
    ax.grid(True)
    
    return ax


# Example usage:
optimal_x, optimal_y = optimal_bundle(0.5, 0.5, 2, 3, 100, 'budget')
utility = calculate_utility(optimal_x, optimal_y, 0.5, 0.5)

print(utility)


def plot_indifference_curves(a, b, utilities, x_range, num_points=100, ax=None):
    """
    Plot indifference curves for a Cobb-Douglas utility function.
    
    Args:
    a, b: Cobb-Douglas utility function parameters
    utilities: List of utility levels to plot
    x_range: Tuple of (min_x, max_x) for the x-axis
    num_points: Number of points to calculate for each curve
    ax: Matplotlib axis object (optional)
    
    Returns:
    Matplotlib axis object
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.linspace(x_range[0], x_range[1], num_points)
    
    for u in utilities:
        y = (u / (x**a))**(1/b)
        ax.plot(x, y, label=f'U = {u:.2f}')
    
    ax.set_xlabel('Good X')
    ax.set_ylabel('Good Y')
    ax.set_title('Indifference Curves')
    ax.legend()
    ax.grid(True)
    
    return ax


# Example usage:
a, b = 0.5, 0.5
utilities = [10, 20, 30, 40, 50]
x_range = (0.1, 10)
plot_indifference_curves(a, b, utilities, x_range)

def calculate_cost(x, y, px, py):
    """
    Calculate the total cost of a consumption bundle.
    
    Args:
    x, y: Quantities of goods X and Y
    px, py: Prices of goods X and Y
    
    Returns:
    Total cost
    """
    return x * px + y * py

def plot_budget_line(px, py, budget, ax=None):
    """
    Plot the budget line.
    
    Args:
    px, py: Prices of goods X and Y
    budget: Total budget
    ax: Matplotlib axis object (optional)
    
    Returns:
    Matplotlib axis object
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    
    max_x = budget / px
    max_y = budget / py
    
    ax.plot([0, max_x], [max_y, 0], 'r-', label=f'Budget Line (${budget})')
    ax.set_xlabel('Good X')
    ax.set_ylabel('Good Y')
    ax.set_title('Budget Line and Indifference Curve')
    ax.legend()
    ax.grid(True)
    
    return ax

def calculate_tangent_budget(a, b, px, py, x, y):
    """Calculate the budget that is tangent to the indifference curve at point (x, y)"""
    return px * x + py * y

def adjust_axis_limits(ax, x, y):
    """Adjust axis limits to show 2-3 times the optimal values with asymptotic adjustment"""
    max_num = max(x, y)
    min_num = min(x, y)
    
    # Calculate ratio
    ratio = max_num / min_num if min_num != 0 else 1
    
    # Use hyperbolic tangent for asymptotic behavior
    # The constant 0.5 controls how quickly it approaches the asymptote
    # The addition of 1 ensures the minimum value is 1 (no adjustment when x == y)
    adjust_factor = 1 + 1.5*math.tanh(0.5 * (ratio - 1))
    
    # Apply adjustment
    if x > y:
        ax.set_xlim(0, x * 3 / adjust_factor)
        ax.set_ylim(0, y * 3 * adjust_factor)
    else:
        ax.set_xlim(0, x * 3 * adjust_factor)
        ax.set_ylim(0, y * 3 / adjust_factor)

# Example usage with interactive components:

def launch_gui():
    root = tk.Tk()
    root.title("Economic Analysis Tool")

    # Create input fields
    ttk.Label(root, text="a:").grid(row=0, column=0)
    a_var = tk.DoubleVar(value=0.5)
    ttk.Entry(root, textvariable=a_var).grid(row=0, column=1)

    ttk.Label(root, text="b:").grid(row=1, column=0)
    b_var = tk.DoubleVar(value=0.5)
    ttk.Entry(root, textvariable=b_var).grid(row=1, column=1)

    ttk.Label(root, text="Price X:").grid(row=2, column=0)
    px_var = tk.DoubleVar(value=2)
    ttk.Entry(root, textvariable=px_var).grid(row=2, column=1)

    ttk.Label(root, text="Price Y:").grid(row=3, column=0)
    py_var = tk.DoubleVar(value=3)
    ttk.Entry(root, textvariable=py_var).grid(row=3, column=1)

    ttk.Label(root, text="Budget:").grid(row=4, column=0)
    budget_var = tk.DoubleVar(value=100)
    ttk.Entry(root, textvariable=budget_var).grid(row=4, column=1)

    ttk.Label(root, text="Constraint:").grid(row=5, column=0)
    constraint_var = tk.StringVar(value="budget")
    ttk.Combobox(root, textvariable=constraint_var, values=["budget", "utility"]).grid(row=5, column=1)

    # Create output text area
    output_text = tk.Text(root, height=10, width=50)
    output_text.grid(row=6, column=0, columnspan=2)

    # Create plot area
    fig, ax = plt.subplots(figsize=(6, 4))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=7)

    def calculate():
        a = a_var.get()
        b = b_var.get()
        px = px_var.get()
        py = py_var.get()
        constraint = budget_var.get()
        constraint_type = constraint_var.get()

        optimal_x, optimal_y = optimal_bundle(a, b, px, py, constraint, constraint_type)
        utility = calculate_utility(optimal_x, optimal_y, a, b)
        cost = calculate_cost(optimal_x, optimal_y, px, py)

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Optimal X: {optimal_x:.2f}\n")
        output_text.insert(tk.END, f"Optimal Y: {optimal_y:.2f}\n")
        output_text.insert(tk.END, f"Utility: {utility:.2f}\n")
        output_text.insert(tk.END, f"Total Cost: ${cost:.2f}\n")

        ax.clear()
        
        if constraint_type == 'utility':
            # Calculate tangent budget for utility constraint
            tangent_budget = calculate_tangent_budget(a, b, px, py, optimal_x, optimal_y)
            plot_budget_line(px, py, tangent_budget, ax)
            ax.set_title(f"Indifference Curve (U={utility:.2f}) and Tangent Budget (${tangent_budget:.2f})")
        else:
            plot_budget_line(px, py, constraint, ax)
            ax.set_title(f"Indifference Curve (U={utility:.2f}) and Budget Line (${constraint:.2f})")

        plot_indifference_curves(a, b, [utility], (0, optimal_x * 3), ax=ax)
        ax.scatter([optimal_x], [optimal_y], color='red', s=100, zorder=5, label='Optimal Bundle')
        ax.legend()
        
        adjust_axis_limits(ax, optimal_x, optimal_y)
        canvas.draw()

    ttk.Button(root, text="Calculate", command=calculate).grid(row=7, column=0, columnspan=2)

    root.mainloop()

# Run the GUI
launch_gui()