from fileHandler import loadExp, saveExp
from reports import monthlySummary
import os


def showMainMenu():
    print("\n1. Add expense")
    print("2. View all expenses")
    print("3. Monthly summary")
    print("4. Exit")

def showCategMenu():
    print("\nSelect category:")
    print("1. Food")
    print("2. Travel")
    print("3. Bills")
    print("4. Other")

def addNewExp():
    print("--- Add New Expense ---")
    try:
        amt = int(input("Enter Amt :"))
        if amt<0:
            print("Amount cannot be negative.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    showCategMenu()
    catagChoice = input("Enter choice (1-4): ")

    match catagChoice:
        case "1":
            category = "Food"
        case "2":
            category = "Travel"
        case "3":
            category = "Bills"
        case "4":
            category = "Other"
        case _:
            print("Invalid category. Please choose 1 to 4.")
            return
    note = input("Enter note (optional): ")
    saveExp(amt, category, note)
    print("Expense saved successfully!")

def viewAllExp():
    print("\n--- All Expenses ---")
    expenses = loadExp()
    if not expenses:
        print("No expenses found.")
        return
    print("date  |  category  |  amount  |  note")
    for e in expenses:
        print(f"{e.date} | {e.category} | {e.amount} | {e.note}")

def showSummary():
    month = input("Enter month in num: ")
    year  = input("Enter year  (e.g. 2026): ")
    monthlySummary(month, year)

print("============================")
print("Expense Tracker v1.0")
print("============================")


if os.path.getsize("BudgetFile.txt") == 0:
    budget = -1
    choice = input("want to set monthly budget? (Y/N): ")
    if choice.lower() == "y":
        while True:
            try:
                budget = int(input("Enter budget: "))
                if budget < 0:
                    print("Cannot be negative.")
                else:
                    with open("BudgetFile.txt","w") as file:
                        file.write(str(budget))
                    print(f"Budget set to {budget}")
                    break
            except ValueError:
                print("Enter a valid number.")

while(True):
    showMainMenu()
    choice = input("Enter choice (1-4): ")
    match choice :
        case "1":
            addNewExp()
        case "2":
            viewAllExp()
        case "3":
            showSummary()        
        case "4":
            print("Goodbye! Keep tracking your expenses.")
            break
        case _:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")
