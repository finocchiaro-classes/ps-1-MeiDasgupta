firstnum = int(input("Enter an integer between 10 and 100:"))
secondnum = int(input("Enter an integer less than 4:"))
print("You entered " + str(firstnum) +  " and " + str(secondnum))
sum_of_first_and_second_num = firstnum + secondnum
product_of_first_and_second_num = firstnum * secondnum
firstnum_raised_to_secondnum_power = firstnum ** secondnum
remainder = firstnum % secondnum
print(str(firstnum) + " + " + str(secondnum) + " = " + str(sum_of_first_and_second_num))
print(str(firstnum) + " * " + str(secondnum) + " = " + str(product_of_first_and_second_num))
print(str(firstnum) + " ** " + str(secondnum) + " = " + str(firstnum_raised_to_secondnum_power))
print(str(firstnum) + " % " + str(secondnum) + " = " + str(remainder))
