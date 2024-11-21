#!/usr/bin/env python3
"""Calculate the area of a triangle."""

def area_triangle():
    """Prompt user for base and height and find area."""
    base = input("Enter the base of the triangle: ")
    height =input("Enter the height of triangle: ")
    Area = 0.5 * float(base) * float(height)
    print("{:.2f}".format(Area))

area_triangle()
