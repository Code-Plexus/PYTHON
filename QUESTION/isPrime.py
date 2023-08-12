def prime():
    num=int(input("enter the number:"))
    lim=int(num/2)+1
    if num==1:
        print("1 is neither prime nor composite")
    else:
        for i in range(2,lim):
            rem=num%i
            if rem==0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
        
