# تعمل أول حرف كبير و الباقي صغير  .capitalize() 
name = input("Enter your first name? ").capitalize()
print(name)

# اول حرف من كل كلمة كبير و الباقي صغير .title()
print(name.title())

#في بداية الجملة و النهاية   spaces تحذف .strip()
print(name.strip())

# مع بعض methods يمكن أضافة 
print(name.strip().title())

print("-" *40)

# .replace takes two arguments 
# اﻷول هيتم تغيرو الي الثاني  
print(name.replace("Ahmed","-")) 

