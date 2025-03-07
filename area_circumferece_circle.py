#!/usr/bin/env python3

# Created By: Luke
# Date: March 7, 2025
# Calculates the area and circumference of a circle

import math  # Module library import


def main():
    print("This program calculates the area and circumference of a circle")
    # Intro message
    radius = float(input(("Enter the radius in cm: ")))
    # Asks user for radius input
    print()
    area = math.pi * radius**2
    # Calculates area
    circumference = 2 * math.pi * radius
    # Calculates circumference
    print("The area is: {:.2f}".format(area))
    # Displays area
    print("The circumference is: {:.2f}".format(circumference))
    # Displays circumference


if __name__ == "__main__":
    main()
