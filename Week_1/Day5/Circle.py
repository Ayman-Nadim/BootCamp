import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Must provide either radius or diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

def draw_circle(radius):
    turtle.circle(radius)
    turtle.penup()
    turtle.setheading(90)  
    turtle.forward(radius * 2)
    turtle.pendown()
    turtle.setheading(0)  

def main():
    circle1 = Circle(radius=3)
    circle2 = Circle(diameter=8)

    print(circle1)  
    print(circle2)  

    print(f"Area of circle1: {circle1.area}")  
    print(f"Area of circle2: {circle2.area}")  

    
    circle3 = circle1 + circle2
    print(circle3) 

    # Comparing circles
    print(circle1 < circle2)  
    print(circle1 == circle2)  

    # List of circles
    circles = [circle1, circle2, circle3]
    sorted_circles = sorted(circles)
    print("Sorted circles:", sorted_circles)

    # Drawing sorted circles
    turtle.speed(0) 
    for circle in sorted_circles:
        draw_circle(circle.radius)
        turtle.penup()
        turtle.setheading(90)
        turtle.forward(circle.diameter)
        turtle.pendown()

    turtle.done()

if __name__ == "__main__":
    main()