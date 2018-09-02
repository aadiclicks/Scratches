x=int(input("Enter Any Number"))
for i in range(2,x):
    if(x%i)==0:
        print("It is not a Prime Number")
        break
    else:
        print("It is a prime Number")
        break

