x = int(input("Pick a number: "))
if x > 1:

   for i in range(2,x):
       if x % i == 0:
           print({0},"is not a prime number".format(x))
           print(i,"*",x//i,"is",x)
           print(i)
           print(x)
           break
   else:
       print(x,"is a prime number")
       print(i)
       print(x)
