# Import math functions
import math


class Shape():
        ''' Class representing a light switch '''
        def __init__(self, base, side, theta):
                '''(Shape, int,int,int) -> NoneType

                Create a switch that has a width,length and angle

                REQ: base >= 0
                REQ: side >= 0
                REQ: theta >= 0
                '''

                self.width = base
                self.length = side
                self.angle = theta

        def __str__(self):
                '''(Shape) -> str
                Return a string representing the shape and area
                '''
                return ("I am a shape with an area")

        def area(self):
                '''(Shape) -> int
                Return the area of the shape
                '''
                # Convert the angle to radians
                Angle = math.radians(self.angle)
                # Multiply the length with the sin of the angle
                Height = self.length * math.sin(Angle)
                # Multiply the width and height
                Area = self.width * Height
                # Return the area
                return Area

        def bst(self):
                '''(Shape) -> list
                Return the dimensions and angle of a shape in a list
                '''
                # Empty list for the dimensions
                List = []
                # Add the width
                List.append(self.width)
                # Add the length
                List.append(self.length)
                # Add the angle
                List.append(self.angle)
                return List

# Inherit the shape class


class Parallelogram(Shape):
        ''' Class representing a parallelogram '''
        def __init__(self, base, side, theta):
                '''(Parallelogram, int,int,int) -> NoneType

                Create a parallelogram

                '''
                Shape. __init__(self, base, side, theta)

        def __str__(self):
                '''(Shape) -> str
                Return a string representing the shape and area
                '''

                Res = "I am a Parallelogram with an area " + str(self.area())
                return Res

# Inherit the shape class


class Rectangle(Shape):
        def __init__(self, base, side):
                '''(Rectangle, int,int) -> NoneType

                Create a Rectangle

                '''
                # Make the angle 90
                Angles = 90
                Shape. __init__(self, base, side, Angles)

        def __str__(self):
                '''(Rectangle) -> str
                Return a string representing the shape and area
                '''

                Res = "I am a Rectangle with an area " + str(self.area())
                return Res

# Inherit the shape class


class Rhombus(Shape):
        def __init__(self, base, theta):
                '''(Rhombus, int,int) -> NoneType

                Create a Rhombus

                '''
                # Make the length become the base
                Length = base
                Shape. __init__(self, base, Length, theta)

        def __str__(self):
                '''(Rhombus) -> str
                Return a string representing the shape and area
                '''

                Res = "I am a Rhombus with an area " + str(self.area())
                return Res

# Inherit the shape class


class Square(Shape):
        def __init__(self, base):
                '''(Square, int,int) -> NoneType

                Create a Square

                '''
                # Make the angle 90
                Angles = 90
                # Make the length become the base
                Length = base
                Shape. __init__(self, base, Length, Angles)

        def __str__(self):
                '''(Square) -> str
                Return a string representing the shape and area
                '''

                Res = "I am a Square with an area " + str(self.area())
                return Res
