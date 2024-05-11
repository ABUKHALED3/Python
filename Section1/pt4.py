erste_num = int(input("Was ist erste nummer? "))
zweite_num = int(input("Was ist zweite nummer? "))
operator = input("was ist math? ")

dertext = ""
result = 0

if operator == "+":
    dertext = "addtional result ist "
    result = erste_num + zweite_num
elif operator == "-":
    dertext = "subcation result ist "
    result = erste_num - zweite_num
elif operator == "*":
    dertext="multiplication "
    result= erste_num * zweite_num
elif operator == "/":
    dertext="divication "
    result =erste_num / zweite_num
else:
    result=""
    dertext="ich verstehe nicht"
    
print(dertext + str(result))