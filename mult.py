num=int(input("Enter number:"))
if num<0:
    print("Does not exist")
elif num==0:
    print("0")
else:
    print("Multiplication table of ",num)
    for i in range (1,11):
        print(num,"x",i,"=",num*i)
    