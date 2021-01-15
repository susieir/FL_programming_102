# Calculates the area of a triangle

def calculate_triangle_a():
    height = float(input("Enter triangle height "))
    base = float(input("Enter triangle base "))
    area = height * base * 0.5
    return area


print(calculate_triangle_a())
