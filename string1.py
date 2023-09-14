str_var=input("enter value:")
str_rev=str_var[::-1]
age=40
if str_var==str_rev:
    print("polindrome")
else:
    print("not polindrome")
print(str_var.replace("a","o"))
j=0
for i in str_var:
    print(str_var[:j+1])
    j+=1
print("my Dear:{} your reverse is {} age is  {}".format(str_var,str_rev,age))