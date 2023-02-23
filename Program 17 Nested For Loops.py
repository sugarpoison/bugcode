initialSalesGoal = 20000
muliplier = 100
offMonth = True

# Creates the variable monthlyGoals with values 1 - 12
for monthlyGoal in range(1,13):
# When monthlyGoal has the value of 6 and offMonth is set to be true, different text will display.
    if monthlyGoal == 6 and offMonth:
        print("There is no goal for the sixth month.")
        continue

#monthlySalesGoal will 
    monthlySalesGoal = initialSalesGoal + (monthlyGoal * muliplier)
    print("Your sales goal for the month " + str(monthlyGoal) + " is $"+ str(monthlySalesGoal))
    for weeklyGoal in range(1,5):
        print("Your goal for week " + str(weeklyGoal) + " is $"+ str(monthlySalesGoal/4))
    print("Good luck with your goals.")

