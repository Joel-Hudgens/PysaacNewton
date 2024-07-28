import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from typing import Optional

def calculate_derivative(function_str: str, variable_str: str) -> str:
    try:
        variable = sp.symbols(variable_str)
        function = sp.sympify(function_str)
        derivative = sp.diff(function, variable)
        return str(derivative)
    except Exception as e:
        return f"Error: {str(e)}"

def calculate_integral(function_str: str, variable_str: str, lower_bound: Optional[str] = None, upper_bound: Optional[str] = None) -> str:
    try:
        variable = sp.symbols(variable_str)
        function = sp.sympify(function_str)

        if lower_bound and upper_bound:
            lower = sp.sympify(lower_bound)
            upper = sp.sympify(upper_bound)
            integral = sp.integrate(function, (variable, lower, upper))
        else:
            integral = sp.integrate(function, variable)
        return str(integral)
    except Exception as e:
        return f"Error: {str(e)}"

def calculate_limit(function_str: str, variable_str: str, point: str) -> str:
    try:
        variable = sp.symbols(variable_str)
        function = sp.sympify(function_str)
        limit = sp.limit(function, variable, sp.sympify(point))
        return str(limit)
    except Exception as e:
        return f"Error: {str(e)}"

def plot_function(function_str: str, variable_str: str, x_range: tuple):
    try:
        variable = sp.symbols(variable_str)
        function = sp.lambdify(variable, sp.sympify(function_str), "numpy")
        x_vals = np.linspace(x_range[0], x_range[1], 400)
        y_vals = function(x_vals)

        plt.plot(x_vals, y_vals)
        plt.xlabel(variable_str)
        plt.ylabel('f(x)')
        plt.title(f'Plot of {function_str}')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error: {str(e)}")

def calculate_mean(data: list) -> float:
    try:
        return float(sum(data) / len(data))
    except Exception as e:
        return f"Error: {str(e)}"

def calculate_median(data: list) -> float:
    try:
        sorted_data = sorted(data)
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            median = sorted_data[mid]
        return median
    except Exception as e:
        return f"Error: {str(e)}"

def calculate_variance(data: list) -> float:
    try:
        mean = calculate_mean(data)
        return float(sum((x - mean) ** 2 for x in data) / len(data))
    except Exception as e:
        return f"Error: {str(e)}"

def print_banner():
    print("""
                _____                                                                         _____ 
               ( ___ )-----------------------------------------------------------------------( ___ )
                |   |                                                                         |   | 
                |   |  _____                              _   _               _               |   | 
                |   | |  __ \                            | \ | |             | |              |   | 
                |   | | |__) |   _ ___  __ _  __ _  ___  |  \| | _____      _| |_ ___  _ __   |   | 
                |   | |  ___/ | | / __|/ _` |/ _` |/ __| | . ` |/ _ \ \ /\ / / __/ _ \| '_ \  |   | 
                |   | | |   | |_| \__ \ (_| | (_| | (__  | |\  |  __/\ V  V /| || (_) | | | | |   | 
                |   | |_|    \__, |___/\__,_|\__,_|\___| |_| \_|\___| \_/\_/  \__\___/|_| |_| |   | 
                |   |         __/ |                                                           |   | 
                |   |        |___/                                                            |   | 
                |___|                                                                         |___| 
               (_____)-----------------------------------------------------------------------(_____)                                                                                        
        """)

def print_instructions():
    print("Welcome to the Derivative and Integral Calculator")
    print("\nYou can use the following mathematical functions:")
    print("- Trigonometric functions: sin(x), cos(x), tan(x), cot(x), sec(x), csc(x)")
    print("- Inverse trigonometric functions: asin(x), acos(x), atan(x), acot(x), asec(x), acsc(x)")
    print("- Exponential function: exp(x) (e^x)")
    print("- Logarithmic functions: log(x) (natural log), log(x, base) (logarithm with base)")
    print("- Use '**' for exponentiation (e.g., 'x**2' for x squared)")
    print()

def main():
    print_banner()
    print_instructions()
    
    while True:
        print("\nChoose an operation:")
        print("1. Derivative")
        print("2. Integral")
        print("3. Limit")
        print("4. Plot Function")
        print("5. Statistics (Mean, Median, Variance)")
        print("6. Exit")
        print()

        choice = input("Enter the number of your choice: ").strip()

        if choice == '1':
            variable_str = input("Enter the variable with respect to which the derivative is taken (e.g., 'x'): ").strip()
            function_str = input("Enter the function to differentiate (e.g., 'x**2 + 3*x + 2'): ").strip()
            result = calculate_derivative(function_str, variable_str)
            print(f"The derivative of {function_str} with respect to {variable_str} is: {result}")
        elif choice == '2':
            variable_str = input("Enter the variable with respect to which the integral is taken (e.g., 'x'): ").strip()
            function_str = input("Enter the function to integrate (e.g., 'x**2 + 3*x + 2'): ").strip()
            definite = input("Do you want to calculate a definite integral? (yes or no): ").strip().lower()
            if definite == 'yes':
                lower_bound = input("Enter the lower bound (e.g., '0'): ").strip()
                upper_bound = input("Enter the upper bound (e.g., '1'): ").strip()
                result = calculate_integral(function_str, variable_str, lower_bound, upper_bound)
            else:
                result = calculate_integral(function_str, variable_str)
            print(f"The integral of {function_str} with respect to {variable_str} is: {result}")
        elif choice == '3':
            variable_str = input("Enter the variable in the function (e.g., 'x'): ").strip()
            function_str = input("Enter the function to find the limit of (e.g., 'sin(x)/x'): ").strip()
            point = input("Enter the point the variable approaches (e.g., '0'): ").strip()
            result = calculate_limit(function_str, variable_str, point)
            print(f"The limit of {function_str} as {variable_str} approaches {point} is: {result}")
        elif choice == '4':
            variable_str = input("Enter the variable in the function (e.g., 'x'): ").strip()
            function_str = input("Enter the function to plot (e.g., 'x**2'): ").strip()
            x_start = float(input("Enter the start of the x-range (e.g., '-10'): ").strip())
            x_end = float(input("Enter the end of the x-range (e.g., '10'): ").strip())
            plot_function(function_str, variable_str, (x_start, x_end))
        elif choice == '5':
            data_str = input("Enter the data as a comma-separated list (e.g., '1, 2, 3, 4, 5'): ").strip()
            try:
                data = list(map(float, data_str.split(',')))
                mean = calculate_mean(data)
                median = calculate_median(data)
                variance = calculate_variance(data)
                print(f"Mean: {mean}, Median: {median}, Variance: {variance}")
            except ValueError:
                print("Error: Invalid data. Please enter a comma-separated list of numbers.")
        elif choice == '6':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number corresponding to the available options.")

if __name__ == "__main__":
    main()
