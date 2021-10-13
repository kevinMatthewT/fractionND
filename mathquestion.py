import math

a=eval(input("Enter a numerator: Value must be greater than 0:"))
if a<=0:
    while a<=0:
       a=eval(input("Please re-enter the numerator. Value must be greater than 0:"))

b=eval(input("Enter a denominator: Value must be greater than 0:"))
if b<=0:
    while b<=0:
       b=eval(input("Please re-enter the denomenator. Value must be greater than 0:"))

c=math.gcd(a,b)
if a<b and c>1:
    print(a,"/",b,"is a proper fraction.")
    print("This proper fraction can be reduced to: ",int(a/c),"/",int(b/c))
elif a<b and c==1:
    print(a, "/", b, "is a proper fraction.")
    print("This proper fraction cannot be reduced any further.")

d=(b/c)

if a>b and c>1 and d==1:
    print(a,"/",b,"is a improper fraction.")
    print("This improper fraction can be reduced to: ",int(a/c),"/",int(b/c))
    print("The whole number is ",int(a/b))
elif a>b and c>1:
    print(a, "/", b, "is a improper fraction.")
    print("This improper fraction can be reduced to: ",int(a/c),"/",int(b/c))
    print("The mixed number is", int(a / b), " and", int(a / c) % int(b / c), "/", int(b / c))
elif a>b and b==1:
    print(a, "/", b, "is a improper fraction.")
    print("This improper fraction cannot be reduced any further.")
    print("The whole number is ", int(a / b))
elif a>b and c==1:
    print(a, "/", b, "is a improper fraction.")
    print("This improper fraction cannot be reduced any further.")
    print("The mixed number is", int(a / b), " and", int(a / c) % int(b / c), "/", int(b / c))
