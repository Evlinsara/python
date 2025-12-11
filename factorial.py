num=int(input("Enter number:"))
fact=1
if num==0:
    print("1")
elif num<0:
    print("invalid")
else:
    for i in range(1,num+1):
      fact*=i
    print(fact)

    