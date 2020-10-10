def area(b, h):
 """ calculate area of a rectangle"""
 A = b * h
 return A

def perimeter(b, h):
 """ calulates perimeter of a rectangle"""
 P = 2 * (b+h)
 return P

width = 10
height = 15
print "Area = ", area(width, height)
print "Perimeter = ", perimeter(width, height)
