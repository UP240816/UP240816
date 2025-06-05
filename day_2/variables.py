#Day 2: 30 Days of python programming
# Variables 
First_name = input("Escribre tu nombre: ") #3. Declare a first name variable and assign a value to it
Last_name = input("Escribe tus apellidos: ") #4. Declare a last name variable and assign a value to it
full_name = First_name + " " + Last_name #5. Declare a full name variable and assign a value to it
Country = input("Escribe tu pais: ")#6. Declare a country variable and assign a value to it
city = input("Escribe tu ciudad: ") #7. Declare a city variable and assign a value to it
age = int(input("Escribe tu edad: ")) #8. Declare an age variable and assign a value to it
year = input("Escribe el año actual: ") #9. Declare a year variable and assign a value to it
is_married = input("Estas casado? (True/False): ") #9. Declare a is_married variable and assign a value to it
is_true = input("Es verdadero? (True/False): ") #10. Declare a is_true variable and assign a value to it
is_light_on = input("La luz esta encendida? (True/False): ") #11. Declare a is_light_on variable and assign a value to it
a, b, c = 5, 10, 15  #12. Declare multiple variable on one line


# Exercises: Level 2
PI = 3.14 # 1. Declare a variable named `PI` and assign it to an initial value of 3.14.
print(len(First_name)) #2. Using the _len()_ built-in function, find the length of your first name
print(type(PI)) #3. Using the _type()_ built-in function, check the data type of your first name variable.
print("Longitud del nombre:", len(First_name))
print("Longitud del apellido:", len(Last_name)) #3. Compare the length of your first name and your last name
num_one, num_two = 5,4 #4. Declare 5 as num_one and 4 as num_two
total = num_one + num_two #5. Add num_one and num_two and assign the value to a variable total
diff = num_one - num_two #6. Subtract num_two from num_one and assign the value to a variable diff
product = num_one * num_two   #7. Multiply num_two and num_one and assign the value to a variable product
quotient = num_one / num_two #8. Divide num_one by num_two and assign the value to a variable quotient
remainder = num_two % num_one #9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
exponent = num_one ** num_two #10. Calculate num_one to the power of num_two and assign the value to a variable exponent
floor_division = num_one // num_two #11. Find floor division of num_one by num_two and assign the value to a variable floor_division
radius = 30 #12. The radius of a circle is 30 meters.
area_of_circle = PI * radius ** 2 #13. Calculate the area of a circle and assign the value to a variable named area_of_circle.
circumference_of_circle = 2 * PI * radius #14.  Calculate the circumference and assign the value to a variable named circumference_of_circle.
 #    15. Take radius as user input and calculate the area.
radius = float(input("Escribe el radio del circulo: "))
area_of_circle = PI * radius ** 2
#16. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
print("Nombre:", First_name)
print("Apellido:", Last_name)
print("Pais:", Country)
print("Ciudad:", city)
print("Edad:", age)
#17. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
import keyword
help(keyword)