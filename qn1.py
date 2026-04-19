# ----------------------------Qn no.1----------------------------------------------
list1 = [{'name':'yumna','age':25}, {'name':'alice', 'age':20}, {'name':'bob', 'age':15},{'name':'John', 'age':10},
         {'name':'Harry', 'age':28}]


list2 = list(filter(lambda item: item['age'] >=18, list1))

print(list2)
