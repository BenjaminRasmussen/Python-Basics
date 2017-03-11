bal = float(input('Enter Balance here'));


for ans in range(1,13):
    interest = bal*0.18/12.0
    principal = 0.02*bal
    bal = bal-(principal-interest);
print(bal)