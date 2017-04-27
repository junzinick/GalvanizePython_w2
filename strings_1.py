x = str(input("Write some letters "))
y = str(input("Write some letters "))

total = x + y
print(len(total))
if total.endswith('!'):
    print(total.upper())
# vowels = ["a","e","i","o","u"]
vowel_pop = total.replace('a', ' ').replace('e', ' ').replace('i', ' ').replace('o', ' ').replace('u', ' ')
print(vowel_pop)
for i in total[0::2]:
    print(i)



