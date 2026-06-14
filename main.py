"""
file: spending_habit.py
-------------------------
This is a program that will track user's expense by inputting your 
expenses and generate a summary story about your spending habits.

This is a wonderful program as it combines a basic data 
analysis task with a GPT narrative summary at the end. 

"""

from ai import call_gpt # a library that access the gpt API

expense_summary = {} # an empty dictionary to store the day and the expenditure of each day

def main():
    print("")
    budget = float(input("Your budget for these days is: ")) # ask a budget from the user
    num_of_day = int(input("How many days of expense you want to input? ")) # ask a number of days that user want to input
    
    # ask for all the data (expenditure of each day) from the user 
    for i in range(num_of_day):
        day = 1 + i
        day_expense(day)

    print_expense(expense_summary)
    
    # tell the user to wait for the response from gpt
    print("")
    print("-------------------------------------------------------------------------------")
    print("We are going to generate your spending habit and some suggestions for you. ")
    print("")
    print("Please wait for several seconds... ")
    print("")

    # make a call to gpt and get a response
    response = call_gpt(f"{expense_summary},This is the expenditure of a user in each day. The budget of the user for these days is ${budget}. Please generate user's spending habit and some suggestions according to the budget and expenditure of the user above.") 
    print(response) # print out the response 

def print_expense(expense_summary):
    # pre-condition: got the day and the expenditure of the user from each days
    # post-condition: print out the day and the expenditure of each days to the user
    for key, value in expense_summary.items():
        if value == "0":
            print("")
            print(f"{key}:")
        else:
            print(f"{key}: ${value}")

def day_expense(day):
    # pre-condition: knowing each day 
    # post-condition: puting all the data (expenditure of each day) into a dictionary called 'expense_summary'
    expense_summary[f"day {day}"] = "0"
    print(f"Day {day}: ")
    title = input("Please enter the title of your expense: ") 
    while title != "0":
        list_expense = []
        expense = float(input(f"Please enter your expense on {title}: "))
        while expense != 0:
            list_expense.append(expense)
            expense = float(input(f"Please enter your enpense on {title}: "))
        total_expense_here = sum(list_expense)
        expense_summary[f"{title}_{day}"] = total_expense_here
        title = input("Please enter the title of your expense: ")
    print("")

if __name__ == "__main__":
    main()