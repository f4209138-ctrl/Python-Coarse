import math
angle=float(input("Input an angle in degrees:"))
angle_radians=math.radians(angle)
sin_value=math.sin(angle_radians)
cos_value=math.cos(angle_radians)
tan_value=math.tan(angle_radians)
print(angle,"=",sin_value,cos_value,tan_value)