ch='Y'
while ch=='y' or ch=='Y':
    n=int(input("Enter the number of fibonacci series required :"))
    n1,n2 = 0,1
    temp = n2 
    count = 0
    if(n<=0):
        print("please enter a positive number")
        ch=input("enter (Y/y) for yes and any key for no to continue :")

    elif(n==1):
        print("the fibonacci series is :",n1)
        ch=input("enter (Y/y) for yes and any key for no to continue :")

    else:
        while count < n:
            print(n1, end=" ")
            count += 1
            n1, n2 = n2, temp
            temp = n1 + n2
        print()
        ch=input("enter (Y/y) for yes and any key for no to continue :")


    

