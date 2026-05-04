# Import section (optional)
import math

# Function definition
def calculate_area(radius):
    """Calculate area of a circle"""
    return math.pi * radius * radius


# Main program
def main():
    # Variable declaration
    radius = 5

    # Function call
    area = calculate_area(radius)

    # Output
    print("Radius:", radius)
    print("Area of circle:", area)


# Entry point of the program
if __name__ == "__main__":
    main()