# ---------------------------------Qn no.4----------------------------------------------------

#lambda function to check whether the given string is number
is_digit = lambda s : s.isdigit()

str = input("enter your string")
if is_digit(str):
    print("It is a number")
else:
    print("It is not a number")

