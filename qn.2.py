# ---------------------------------Qn no.2----------------------------------------------

from functools import reduce

#creating the list
list1 = [1,2,3,4,5,6,7,8,9]

#calculating product using reduce and lamda
product = reduce(lambda x, y: x*y, list1)
print(product)
