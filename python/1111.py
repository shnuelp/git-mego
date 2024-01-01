a = []
for i in range(int(input())):
    for j in range(int(input())):
       a.append(int(input(end='')))
print(a)

'''

a = [] # start an empty list
n = int(input()) # read number of element in the list
for i in range(n):
    new_element = int(input()) # read next element
    a.append(new_element) # add it to the list
    # the last two lines could be replaced by one:
    # a.append(int(input()))
print(a)

a = [0] * int(input())
for i in range(len(a)):
    a[i] = int(input())
print(a)

a = [] # start an empty list
n = int(input()) # read number of element in the list
for i in range(n):
    new_element = int(input()) # read next element
    a.append(new_element) # add it to the list
    # the last two lines could be replaced by one:
    # a.append(int(input()))
print(a)

a = []
for i in range(int(input())):
    a.append(int(input()))
print(a)

a = [1, 2, 3, 4, 5]
for i in a:
    print(a[i])
a = [1, 2, 3, 7, 5]
for i in a:
    print()
n = int(input())
length = 0
while n > 0:
    n //= 10  # this is equivalent to n = n // 10
    length += 1
print(length)  # 4

i = 1
while i <= 10:
    print(i ** 2)
    i += 1

i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Loop ended, i =', i)

total_sum = 0
a = int(input())
while a != 0:
    total_sum += a
    if total_sum >= 21:
        print('Total sum is', total_sum)
        break
    a = int(input())
else:
    print('Total sum is less than 21 and is equal to', total_sum, '.')

for i in range(5):
    a = int(input())
    if a < 0:
        print('Met a negative number', a)
        break
else:
    print('No negative numbers met')

# Read an integer:
num = int(input())
print('The next number for the number ' + str(num) + ' is ' + str(num + 1) + '.')
print('The previous number for the number ' + str(num) + ' is ' + str(num - 1) + '.')
number = int(input("Enter a number: "))
print("Previous number:", number - 1)
print("Next number:", number + 1)

a = int(input("Enter the number of students in the first classroom: "))
b = int(input("Enter the number of students in the second classroom: "))
c = int(input("Enter the number of students in the third classroom: "))

total_students = a + b + c
# Round up the total number of students to the nearest even number, since each desk sits two students.
total_desks = (total_students + 1) // 2

print("The smallest possible number of desks that can be purchased is:", total_desks)
a = int(input("Enter the number of students in the first classroom: "))
b = int(input("Enter the number of students in the second classroom: "))
c = int(input("Enter the number of students in the third classroom: "))

total_students = a + b + c
# Round up the total number of students to the nearest even number, since each desk sits two students.
# If the total number of students is odd, then rounding down will result in one more desk than needed.
total_desks = (total_students + 1) // 2 + 1 if total_students % 2 != 0 else (total_students + 1) // 2

print("The smallest possible number of desks that can be purchased is:", total_desks)
print(round(1.3))   # gives 1
print(round(1.7))   # gives 2
print(round(-1.3))  # gives -1
print(round(-1.7))  # gives -2
print(1 % 0.2)  # gives 0.30000000000000004
x = int(input("Please enter an integer: "))

if x < 0:

    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
a=sum(range(50))
print(a)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
num = int(input("Enter the number: "))

if num > 1:
# check for factors
for i in range(2,num):
 if (num % i) == 0:
  print(num,"is not a prime number")
   print(i,"times",num//i,"is",num)
  break
 else:
  print(num,"is a prime number")
# if input number is less than
# or equal to 1, it is not prime
 else:
  print(num,"is not a prime number")
num = int(input("Enter the number: "))f

squares = [x**2 for x in range(1, 6)]
print(squares)
fruits = ['apple', 'banana', 'orange', 'kiwi']
filtered_fruits = [fruit.upper() for fruit in fruits if len(fruit) > 5]
print(filtered_fruits)
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
# Combine names and ages into a list of tuples
combined = list(zip(names, ages))
print(combined)
sentence = "Hello, how are you today?"
words = sentence.split(" t")  # Splitting at the comma delimiter
print(words)
sentence = "Hello   world!\tHow\nare you?"
words = sentence.split()
print(words)'
user_input = "   Hello, how are you?   "
words = user_input.split()
print(words)
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
    break
    print("Found an odd number", num)
# Python program to illustrate
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
	print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
	print(i)

# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
	print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
	print("%s %d" % (i, d[i]))

# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
	print(i),
c=0
s = "Geeks"
for i in s:
    c=c+1
    print(i)
print(c)
from __future__ import print_function
for i in range(1, 20):
    for j in range(i):
        print(i, end=' ')
    print()
#Program to reverse a string
gfg = "geeksforgeeks"
print(gfg[1::-1])
# Joining with empty separator
list1 = ['g', 'e', 'e', 'k', 's']
print("".join(list1))

# Joining with string


# elements in tuples
list1 = ('1', '2', '3', '4')
print("-".join(list1))
import itertools
a = [[1, 2], [3, 4], [5, 6]]
b = list(itertools.chain.from_iterable(a))
print(b)
a=["10","9","8","7"]
print(a[::-1])
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[-3::-1])
a="Python is the language of the future"
b=a.split()
print(b)

a=10
b=20
print(f"first:  {a, b}")

a, b = b, a + 2
print(f"Second: {a, b}")

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)


a = [x * 2 for x in range(10)]
print(a)

a = [1, 2, 3, 4 ,5]
b = a

# Change the 4th index in b
b = a[:]

print(id(a))
print(id(b))
print(a) # Remember we did not explicitly make changes to a.

x = 10
y = 20
print(f"{x = }, {y = }")

"""
x = 10, y = 20
"""

a = ["english", "french", "spanish", "german", "twi"]
for language in a:
    print(language, end=" ")

"""
english french spanish german twi
"""

a = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 2, 2]
print(list(set(a)))

"""
[1, 2, 3, 4, 5, 6, 7]
"""

day = "04"
month = "10"
year = "2022"

print(day, month, year)
print(day, month, year, sep = "")
print(day, month, year, sep = ".")




"""
04 10 2022
04/10/2022
04.10.2022
"""
print(...)

list_of_strings = ["Hello", "my", "friend"]

# BAD:
list_of_strings = ["Hello", "my", "friend"]
my_string = " ".join(list_of_strings)
print(my_string)

colors = ["red", "green", "blue"]

c = "red"

# better:
if c in colors:
    print("is main color")

    print("Number Pattern ")

    # Decide the row count. (above pattern contains 5 rows)
row = 5
    # start: 1
    # stop: row+1 (range never include stop number in result)
    # step: 1
    # run loop 5 times
for i in range(1, row + 1, 1):
        # Run inner loop i+1 times
        for j in range(1, i + 1):
            print(j, end=' ')
        # empty line after each row
        print("")
names = ['Kelly', 'Jessa', 'Emma']
# outer loop
for name in names:
    # inner while loop
    count = 0
    while count < 5:
        print(name, end=' ')
        # increment counter
        count = count + 1
    print()

    # 5 rows
for name in range(5):
        # 3 column
        for j in range(3):
            print('*', end='')
        print()
import random

e = int(random.random()*100)
print(e)

def main():
    # מודפס הודעה למשתמש
    print("הזן מספרים. כדי לסיים, הקלד 'q'.")

    # משתנה לניהול מספר המספרים שנקלטו
    count = 0

    # משתנה לניהול הסכום של המספרים שנקלטו
    sum = 0

    # לולאה לקבלת מספרים מהמשתמש
    while True:
        # קולט מספר מהמשתמש
        number = input("הזן מספר: ")

        # אם המשתמש הקליד 'q', מסיים את הלולאה
        if number == "q":
            break

        # מוסיף את המספר לסכום
        sum += float(number)

        # מוסיף 1 למונה
        count += 1

    # אם לא נקלטו מספרים, הדפס הודעה
    if count == 0:
        print("לא נקלטו מספרים.")

    # אחרת, הדפס את הממוצע
    else:
        average = sum / count
        print("הממוצע הוא:", average)


if __name__ == "__main__":
    main()'''

def is_palindrome(word):
  """
  בדיקה האם מחרוזת היא פלינדרום.

  Args:
    word: המחרוזת לבדיקה.

  Returns:
    True אם המחרוזת היא פלינדרום, False אחרת.


  i = 0
  j = len(word) - 1
  while i < j:
    if word[i] != word[j]:
      return False
    i += 1
    j -= 1
  return True


if __name__ == "__main__":
  word = input("הכנס מחרוזת: ")
  is_palindrome = is_palindrome(word)
  print("האם המחרוזת היא פלינדרום? ", is_palindrome)

import random

# יצירת רשימה של 100 מספרים אקראיים בין 0 ל-9, כולל
numbers = random.sample(range(0, 10),100)

# הדפסת המספרים האקראיים
print(numbers)


# Python program to draw square
# using Turtle Programming
# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)

# More complex example
for i in [1, 3, 5, 7, 9]:
    x = i**2 - (i-1)*(i+1)
    print(x, end=", ") # prints 1, 1, 1, 1, 1,


for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, end="")
    print()
  # empty list
  # empty list
  print(list())

  # vowel string
  vowel_string = 'aeiou'
  print(list(vowel_string))

print(' '.join(input().split()[::2]))"""




