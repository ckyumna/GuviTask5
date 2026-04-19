# ----------------------------Qn no.1----------------------------------------------

#list of dicts
list1 = [{'name':'yumna','age':25}, {'name':'alice', 'age':20}, {'name':'bob', 'age':15},{'name':'John', 'age':10},
         {'name':'Harry', 'age':28}]

#lambda function to find age > = 18
list2 = list(filter(lambda item: item['age'] >=18, list1))


#using map() to select only names from the new list
names= list(map(lambda item: item['name'], list2))
print(names)