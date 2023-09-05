import random as rd

b = rd.randint(10, 50)
a = rd.randint(10, b)
while(True):
    s = int(input())
    if a==s:
        print("угодал")
        break
    else:
        randomNegr = rd.randint(0, 3)

        if randomNegr == 1:
            print("я не знаю")
            continue

        if a>s:
            print("оно больше")

        else:
            print("оно меньше")