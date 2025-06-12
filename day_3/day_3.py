#day 3
age = int(18) #1. Declare your age as integer variable
height = 1.75 #2. Declare your height as float variable
numero_complejo = 3 + 4j #3. Declare a variable that store a complex number
#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
height = float( input( " Enter the height of a triangle: "))
Base = float( input( " Enter the base of a triangle: "))
area = 0.5 * Base * height
print( "The area of the triangle is: ", area) 
#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is: ", perimeter)
#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("The area of the rectangle is: ", area_rectangle)
print("The perimeter of the rectangle is: ", perimeter_rectangle)
#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area_circle = pi * radius * radius
circumference_circle = 2 * pi * radius
print("The area of the circle is: ", area_circle)
print("The circumference of the circle is: ", circumference_circle)
#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2  
x_intercept = -y_intercept / slope
print("The x-intercept of the line is: ", x_intercept)
print("The slope of the line is: ", slope)
print("The y-intercept of the line is: ", y_intercept)
#9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance]between point (2, 2) and point (6,10) 
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("The slope between the points is: ", slope_points)
print("The Euclidean distance between the points is: ", euclidean_distance)
#10. Compare the slopes in tasks 8 and 9.
if slope == slope_points:
    print("The slopes are equal.")
else:
    print("The slopes are not equal.")
#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x_values = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
for x in x_values:
    y = x**2 + 6*x + 9
    print(f"When x = {x}, y = {y}")
    if y == 0:
        print(f"The value of x that makes y equal to 0 is: {x}")
        break
#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_length = len("python")
dragon_length = len("dragon")
if python_length != dragon_length:
    print("The lengths of 'python' and 'dragon' are not equal.")
#13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
python_string = "python"
dragon_string = "dragon"
if "on" in python_string and "on" in dragon_string:
    print("'on' is found in both 'python' and 'dragon'.")
#14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
sentence = "I hope this course is not full of jargon"
if "jargon" in sentence:
    print("'jargon' is found in the sentence.")
#15. There is no 'on' in both dragon and python
if "on" not in python_string and "on" not in dragon_string:
    print("'on' is not found in both 'python' and 'dragon'.")
#16. Find the length of the text _python_ and convert the value to float and convert it to string
length_python = len("_python_")
length_python_float = float(length_python)
length_python_str = str(length_python_float)
print(f"The length of '_python_' as a float is: {length_python_float}")
print(f"The length of '_python_' as a string is: {length_python_str}")
#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number to check if it is even: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is not an even number.")
#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division_result = 7 // 3
int_value = int(2.7)
if floor_division_result == int_value:
    print("The floor division of 7 by 3 is equal to the int converted value of 2.7.")
else:
    print("The floor division of 7 by 3 is not equal to the int converted value of 2.7.")
#check if type of ´10´ is equal to type of 10
type_of_10_str = type('10')
type_of_10_int = type(10)
if type_of_10_str == type_of_10_int:
    print("The type of '10' is equal to the type of 10.")
else:
    print("The type of '10' is not equal to the type of 10.")
#20. Check if int('9.8') is equal to 10
    int_value = int(9.8)
    if int_value == 10:
        print("int(9.8) is equal to 10.")
    else:
        print("int(9.8) is not equal to 10.")
#21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter the number of hours worked: "))
rate_per_hour = float(input("Enter the rate per hour: "))
pay = hours * rate_per_hour
float_pay = float(pay)

print(f"The pay for {hours} hours at a rate of {rate_per_hour} per hour is: {float_pay}")
#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter the number of years: "))
seconds_per_year = 365 * 24 * 60 * 60  
seconds_lived = years * seconds_per_year
print(f"A person who lives for {years} years has lived for approximately {seconds_lived} seconds.")
#23. Write a Python script that displays the following table
print("1  1  1  1  1")
print("2  1  2  4  8")
print("3  1  3  9 27")
print("4  1  4 16 64")
print("5  1  5 25 125")
