def rnumber():
    num=int(input("Enter the Number to br reversed"))
    rev=0
    while(num>0):
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    print("The reversed number = "+str(rev))

rnumber()