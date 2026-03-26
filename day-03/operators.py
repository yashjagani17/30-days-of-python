age = 27
height = 169.5
complex_num = 3 + 4j

base = int(input("Enter base: "))
height = int(input("Enter height: "))
print("The area of the triangle is ", base * height)

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
print("The perimeter of the triangle is ", side_a + side_b + side_c)

length = int(input("Enter length: "))
width = int(input("Enter width: "))
print("The area of the circle is ", length * width)
print("The perimeter is ", 2 * (length + width))

radius = int(input("Enter radius: "))
print("The area of the circle is ", 3.14159265359 * (radius**2))
print("The circumference of the circle is ", 2 * 3.14159265359 * radius)

p = (2, 2)
q = (6, 10)
slope = ((10-2)/(6-2))
euclid_dist = (((p[0]-q[0])**2) + ((p[1]-q[1])**2))**0.5
print("Slope of (2, 2) and (6, 10) is ", slope)
print("Euclidean distance between (2, 2) and (6, 10) is ", euclid_dist)

python_len = len("python")
dragon_len = len("dragon")
print(python_len != dragon_len)
print('on' in 'python' and 'on' in 'dragon')
sentence = "I hope this course is not full of jargon"
print('jargon' in sentence)
print('on' not in 'dragon' and 'on' not in 'python')
text_length_int = len(sentence)
text_length_float = float(text_length_int)
text_length_string = str(text_length_float)

print(4 % 2)
print(7 // 3 == int(2.7))
print(type('10') == type(10))
# print(int('9.8') == 10) ValueError: invalid literal for int() with base 10: '9.8'

hours = int(input("Enter hours: "))
rate = int(input("Enter rate: "))
print("Your weekly earning is ", rate * hours)

years = int(input("Enter number of years: "))
print("You have lived for ", years * 31536000, " seconds")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")