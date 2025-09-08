prior_arrests = int(input("Prior arrests: "))
local_ord = input("Prior arrests for local ordinance (Y/N): ")
age = int(input("Age at release: "))

score = 0

if prior_arrests >= 2:
    score = score + 1

if prior_arrests >= 5:
    score = score + 1

if local_ord == "Y":
    score = score + 1


if 18 <= age <= 24:
    score = score + 1

if 40 <= age:
    score = score - 1
    

if score == -1:
    risk = 11.9
elif score == 0:
    risk = 26.9
elif score == 1:
    risk = 50.0
elif score == 2:
    risk = 73.1
elif score == 3:
    risk = 88.1
elif score == 4:
    risk = 95.3


print("The recidivism risk score is ", score)
