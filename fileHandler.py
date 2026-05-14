import csv,os
from datetime import datetime
from expense import Expense
fileName = "expenses.csv"

def saveExp(amount, category, note):
    try:
        id = getNextId()
        date = datetime.now().strftime("%Y-%m-%d")
        file_exists = os.path.isfile(fileName)
        with open(fileName,"a",newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["ID", "Date", "Category", "Amount", "Note"])
            writer.writerow([id, date, category, amount, note])
    except Exception as e:
        print(f"an err occurred : {e}")

def loadExp():
    expList = []
    if not os.path.isfile(fileName):
        return []

    try:
        with open(fileName, "r", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                newExp = Expense(
                    id=int(row['ID']),
                    amount=int(row['Amount']),
                    category=row['Category'],
                    note=row['Note'],
                    date=row['Date']
                )
                expList.append(newExp) 
    except Exception as e:
        print(f"Error loading expenses: {e}")
        
    return expList  

def getNextId():
    try:
        with open(fileName, "r") as f:
            lines = f.readlines()
            if len(lines) <= 1:  # empty or just header
                return 1
            lastLine = lines[-1]
            lastId = int(lastLine.split(",")[0])
            return lastId + 1
    except FileNotFoundError:
        return 1