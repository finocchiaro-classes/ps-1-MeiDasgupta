def heart_rate(age, goal):
    max_HR = 220 - age
    print("Your maximum heart rate is:", max_HR)
    
    if goal == "S":
        low_target_HR = .8 * max_HR
        high_target_HR = max_HR
        print("Your target heart rate is between", low_target_HR, "and", high_target_HR)

    if goal == "E":
        low_target_HR = .6 * max_HR
        high_target_HR = .8 * max_HR
        print("Your target heart rate is between", low_target_HR, "and", high_target_HR)


user_age = int(input("What is your age? "))
user_goal = input("Is your goal speed (S) or endurance (E)? ")

heart_rate(user_age, user_goal)
