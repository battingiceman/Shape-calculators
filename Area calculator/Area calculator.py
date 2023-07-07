import random


while True:
    shape = input("Enter shape you want to find the area of. The options are Circle, Square, Triangle, Rectangle, Oval, Parallelogram, and Trapezoid (Do not enter units of measurement or the program will crash). Enter 'exit' to quit: ")

    if shape.lower() == "circle":
        radius = input("Enter radius of the Circle: ")
        area = int(radius) ** 2 * 3.14159265358979
        print(area)

    elif shape.lower() == "square":
        side = input("Enter one side length of the square: ")
        area = int(side) ** 2
        print(area)
       

    elif shape.lower() == "triangle":
        base = input("Enter base length of the triangle: ")
        height = input("Enter height length of the triangle: ")
        area = 0.5 * int(base) * int(height)
        print(area)

    elif shape.lower() == "rectangle":
        length = input("Enter length of the rectangle: ")
        width = input("Enter width of the rectangle: ")
        area = int(length) * int(width)
        print(area)

    elif shape.lower() == "oval":
        semi_major_axis = input("Enter length from the middle of the oval to the side: ")
        semi_minor_axis = input("Enter length from the middle of the oval to the top side: ")
        area = float(semi_major_axis) * float(semi_minor_axis) * 3.14159265358979
        print(area)

    elif shape.lower() == "parallelogram":
        base = input("Enter base length of the parallelogram: ")
        height = input("Enter height length of the parallelogram: ")
        area = float(base) * float(height)
        print(area)

    elif shape.lower() == "trapezoid":
        top_base = input("Enter top base length of the trapezoid: ")
        bottom_base = input("Enter bottom base length of the trapezoid: ")
        height = input("Enter length from bottom base to top base of the trapezoid: ")
        area = 0.5 * (float(top_base) + float(bottom_base)) * float(height)
        print(area)

    elif shape.lower() == "easter egg":
        print("Dad's Easter Egg")

    elif shape.lower() == "exit":
        break

    else:
        print("Invalid shape entered!")

window.exitonclick()
