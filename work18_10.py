import random

magicnum = random.randint(1, 10)

print(magicnum)

usernum = 0

while magicnum != usernum:
    usernum = int(input("Enter num from 1 to 10:"))
    if magicnum > usernum:
        print("bigger")
    else:
        print("lower")

else:
    print("Win")