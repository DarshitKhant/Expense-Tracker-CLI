from fileHandler import loadExp
import os

def monthlySummary(month, year):
    expenses = loadExp()
    total = 0
    biggestExpCateg= 0
    biggestExpAmt =  0
    categoryTotal = {}
    searchPeriod = f"{year}-{month.zfill(2)}"

    for exp in expenses:
        if exp.date.startswith(searchPeriod):
            if biggestExpAmt<exp.amount:
                biggestExpCateg = exp.category
                biggestExpAmt = exp.amount
            total += exp.amount
            categoryTotal[exp.category] = categoryTotal.get(exp.category,0) + exp.amount

    print(f"Total Spent: {total}")
    print(f"Your biggest expense was {biggestExpAmt} on {biggestExpCateg}")
    print("\nBreakdown by Category:")

    for categ, amt in categoryTotal.items():
        print(f"- {categ}: {amt}")

    if os.path.getsize("BudgetFile.txt") < 0 : 
        with open("BudgetFile.txt","r") as file:
            budget=int(file.read())
            if budget != -1 and total>budget:
                print("You have exceded your monthly budget!")
                print(f"Budget: {budget} | Spent: {total} | Over by: {total-budget}") 
    