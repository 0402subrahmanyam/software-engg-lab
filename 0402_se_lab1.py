# -*- coding: utf-8 -*-
"""0402 SE lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VQjtmPn2LvrUqrLwx9sZaxn0I1RzzvqW
"""

import math

def quadratic_solution(a, b, c):

    delta = b**2 - 4*a*c


    if delta >= 0:

        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    else:
        return None

def weather_model_hard_coded():

    a = 1
    b = -3
    c = 2


    solutions = quadratic_solution(a, b, c)


    if solutions:
        print("Weather model hard-coded solutions:", solutions)
    else:
        print("No real solutions for the weather model.")

def weather_model_keyboard_input():

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))


    solutions = quadratic_solution(a, b, c)


    if solutions:
        print("Weather model keyboard input solutions:", solutions)
    else:
        print("No real solutions for the weather model.")

def weather_model_read_from_file(filename):

    try:
        with open(filename, 'r') as file:
            coefficients = [float(x) for x in file.readline().split()]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return


    if len(coefficients) != 3:
        print("Invalid number of coefficients in the file.")
        return


    a, b, c = coefficients


    solutions = quadratic_solution(a, b, c)


    if solutions:
        print("Weather model solutions from file:", solutions)
    else:
        print("No real solutions for the weather model.")

if __name__ == "__main__":

    weather_model_hard_coded()


    weather_model_keyboard_input()


    file_name = "coefficients.txt"
    weather_model_read_from_file(file_name)