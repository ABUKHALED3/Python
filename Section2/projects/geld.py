# answer

money_father = float(input("Enter amount of money: "))
num_children = int(input("Enter number of children: "))
currency = input("Enter Currency: " )

result = round(money_father / num_children,2)
print("-" *33)
print("Each one should get " + str(result) +" " + currency)