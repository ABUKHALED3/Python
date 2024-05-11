# Caluelt Break Even Point in units und Pounds

fixed_cost = int(input("Fixed cost: "))
unit_price = int(input("Unit selling price:"))
variable_cost = int(input("Variable cost: "))


BEP = fixed_cost / (unit_price - variable_cost)
print("The result ist " +str(BEP))