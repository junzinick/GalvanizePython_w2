x = int(input("Pick a number: "))
def factorial(x):
    for i in reversed(range(x)):
        if i == 0:
            return x
        else:
            x *= int(i)
            print(i)
factor=factorial(x)
print(factor)

print(x)


