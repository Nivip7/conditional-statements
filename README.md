
2.SALARY DEDUCTION IF ABSENT DAYS EXCEEDED PERMITTED LEAVE AND DISPLAY UPDATED SALARY:

s=float(input("enter the salary"))
n=int(input("enter the NUMBER OF DAYS ABSENT:"))
d=int(input("enter the NUMBER OF DAYS LEAVE PERMITTED:"))
p=int(input("enter the deduction amt for each exceeded leave:"))
if n>=0 and n<=d:
    print("no deduction in salary!!!")
    print("updated salary:",s)
else:
    print("deduction in salary!!!",)
    print("deducted amt:",(n-d)*p)
    print("updated salary:",(s-(n-d)*p))
