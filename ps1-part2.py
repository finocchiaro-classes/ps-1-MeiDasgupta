def number_fun(a, b):
    print("You entered:", a, "and", b)
    print(a + b)
    print(a * b)
    print(a ** b)
    print(a % b)
firstnum = int(input("Provide an integer between 10 and 100"))
secondnum = int(input("Provide an integer less than 4"))
number_fun(firstnum, secondnum)

