from math import  pi

def circle_area(r):
    return pi * r**2

def rectangle_area(a,b):
    return a*b


if __name__ == "__main__":
    print(rectangle_area(3,4))
    print(circle_area(1))