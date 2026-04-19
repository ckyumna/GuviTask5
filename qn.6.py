#range of series
n = 10

#lambda function to calculate fibonacci
fib = lambda x: x if x <= 1 else fib(x-1) + fib(x-2)

#list comprehension to generate fibonacci upto n terms
series = [fib(i) for i in range(n)]

print(series)