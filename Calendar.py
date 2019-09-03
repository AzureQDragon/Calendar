#Name: Daniel Moon
#Date: 9/3/2019
#Program: Calendar Project
#Program description: Creates a program that outputs a calender when given a start date and number of days

playagain = "Y" #Stores whether the user wishes to play again

#Loops while the user wishes to play again
while playagain == "Y":
    #User input is given
    num_days = eval(input("Enter how many days are in the month: ")) #Stores number of days in month
    first_day = eval(input("Enter the first day of the month (Sun = 0... Sat = 6): ")) #Stores

    #Prints the days of the week in the correct format
    print(" "*2, format("Sun", "5s"), end = "")
    print(format("Mon", "5s"), end = "")
    print(format("Tue", "5s"), end = "")
    print(format("Wed", "5s"), end = "")
    print(format("Thu", "5s"), end = "")
    print(format("Fri", "5s"), end = "")
    print(format("Sat", "5s"), end = "")

    #Adds the dashed line along with the correct amount of indentation on the next line
    print("\n", 35*"-", "\n", " "*(first_day*5), end = "", sep = "")

    #For loop for printing the days
    for i in range(1,num_days+1):
        print(format(i, "5d"), end = "")
        if (i+first_day)%7 == 0: #If the day + first day is divisible by 7
            print("\n", end="") #Jump to next line

    #Prompt user if they wish to make another calendar
    playagain = input("\nWould you like to do another calendar? (Y or N): ")  



