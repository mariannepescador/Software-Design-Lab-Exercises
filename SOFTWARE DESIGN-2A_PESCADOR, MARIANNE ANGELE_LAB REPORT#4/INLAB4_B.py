def product (x,y):
    if (x ==0 or y ==0):
        return 0

    elif(x<y):
        return product(y,x)
    elif y!=0:
        return (x+product(x,y-1))

x=int(input("Enter Number1: "))
y=int(input("Enter Number2: "))
print("Product =", product(x,y))
