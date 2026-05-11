from fileHandler import loadExp

def monthlySummary(month, year):
    expenses = loadExp()
    total = 0
    categoryTotal = {}
    searchPeriod = f"{year}-{month.zfill(2)}"
    for exp in expenses:
        if exp.date.startswith(searchPeriod):
            total += exp.amount
            categoryTotal[exp.category] = categoryTotal.get(exp.category,0) + exp.amount
    print(f"Total Spent: {total}")
    print("\nBreakdown by Category:")
    for categ, amt in categoryTotal.items():
        print(f"- {categ}: {amt}")


