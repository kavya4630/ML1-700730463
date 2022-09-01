PI = 3.14
#Let the radius be 20
radius = 20
def findAreaOfACircle(rad):
    return PI * (rad*rad);
_area_of_circle_ = findAreaOfACircle(radius)
_circum_of_circle_ = 2 * PI * radius
print("Area of circle is : %.2f" %_area_of_circle_)
print("Circumference of circle is : %.2f" %_circum_of_circle_)