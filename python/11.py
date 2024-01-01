'''# Exercise 1
def multiplication_result(a, b, c):
    print(a * b * c)

# Exercise 2
def full_name(first_name, last_name):
  print(f"{first_name} {last_name}")

# Exercise 3
def max_number():
  a = int(input("enter the number: "))
  b = int(input("enter the number: "))
  c = int(input("enter the number: "))

  print(max(a, b, c))

# Exercise 4
#Option 1
def longest_name():

  a = (input("enter the name: "))
  b = (input("enter the name: "))
  c = (input("enter the name: "))
  long =(max(a, b, c, key=len))
  print(f"the longest_name:{long}")'''


#Option 2
def longest_name():

  longest_name =""
  for i in range(3):
    name = input("enter the name: ")
    if len(name) > len(longest_name):
      longest_name = name
    if len(name) == len(longest_name):
      longest_name = name
    print(longest_name)

longest_name()


# Exercise 5
def odd_or_even():
  number =int(input("enter the number: "))
  if number % 2 == 0:
    print("the number is even")
  else:
   print("the number is odd")

# Exercise 6
import math

def circle_area():

  radius=float(input("enter the radius: "))
  area= float(radius ** 2 * math.pi)

  print(f"The area is {area:.f}.")








