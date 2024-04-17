# #Sequential Problem 2

#  Acircle = pi*radius**2
#  Arectangle = length * width
#  Atriangle = 1/2(base*height)

shape = input('Choose your shape (ie. circle, rectangle, triangle): ')

if shape == 'circle':
    radius = int(input('Provide the radius of the circle: '))
    AreaC = 3.14*radius**2
    print('Area of the circle is', AreaC)
elif shape == 'rectangle':
    length = int(input('Provide the length of the rectangle: '))
    width = int(input('Provide the width of the retangle: '))
    AreaR = length*width
    print('Area of the rectangle is', AreaR)
elif shape == 'triangle':
    base = int(input('Provide the base of the triangle: '))
    height = int(input('Provide the height of the triangle: '))
    AreaT = (base*height)/2
    print('Area of the triangle is', AreaT)
else:
    print('Invalid input')