
bal = float(input('Enter balance'))
interest = float(input('Enter interest rate annual'))/100/12
principal = float(input('Enter principal'))/100
for i in range(1,13): ## Loops i for 1 to 12
    print("Month " + str(i))
    print("Outstanding: $" + str(bal))
    print("Principal paid: $" + str((principal*bal)-(interest*bal)))
    bal = bal-((principal*bal)-(interest*bal)) ## equation for balance which calculates 12 times
    print("Outstanding after deduction: $" + str(bal))
print(str(bal).__getslice__(0,6))
