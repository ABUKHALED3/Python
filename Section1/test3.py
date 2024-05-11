#Variables to save inputs user
#Hier ist Error wenn print
#warum?
#  تأخذ الكلام وتخزنه كا جمله فقط function input 
# ich use function int to convert srting >> intger
first_num = int(input("was ist dein num? "))
second_num = int(input("was ist dein num? "))
third_num = int(input("was ist dein num? "))


if first_num > second_num:
    #yah if again
    if first_num > third_num:
        #Hier ist Error wenn print.  Warum?
        #string with intger عند الطباعة لايمكن طباعة  
        # function str convert >> (int >> str)
        #wenn print str with str.
        #حاليا هطبع سترنج مع سترنج يبقا كده اشطا 
        # عند الطباعة لازم يبقو شبه بعض في النوع

        print(str(first_num)+" Erste ist the gratest")
    
    #nein
    else:
        print(str(third_num)+" Drittel ist the gratest")

#nein
else:
    if second_num > third_num:
        print(str(second_num)+" Zweite ist the gratest")
    else:
        print(str(third_num)+" Drittel ist the gratest")