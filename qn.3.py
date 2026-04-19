#creating the list of numbers
list1 = [1,2,3,4,5,6,7,8,9]

#lambda function to check even condition
even = lambda x: x % 2 == 0

# list comprehension
squares = [x**2 for x in list1 if even(x)]
print(squares)
