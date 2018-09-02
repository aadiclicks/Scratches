def sumd():
    num=int(input("Enter the Number"))
    sum=0
    while(num>0):
        rem=num%10
        sum+=rem
        num=num//10
    print("The sum of digits is "+str(sum))

sumd()
