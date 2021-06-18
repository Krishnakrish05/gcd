def gcd(num1,num2):
    while(num2 !=0):
        temp=num2
        num2=num1%num2
        num1=temp
    print(num1)

gcd(10,12)