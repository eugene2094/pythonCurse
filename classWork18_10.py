num = 0

# while num < 10:
#     if num == 5:
#         break
#     print(num)
#     num += 1

# while num < 50:
#     num += 1
#     if num % 2 == 0:
#         continue
#     else:
#         print(num)


# usernum = 0
#
# while True:
#     usernum = int(input("enter num"))
#     if usernum == 0:
#         break
#     elif usernum < 0:
#         continue
#     print(usernum)
#

import random

magicNumber = random.randint(1, 10)

print(magicNumber)

usernum = 0

while magicNumber != usernum:
    usernum = int(input("enter num from 1 to 10 - > "))
    if magicNumber > usernum:
        print("try bigger num ")
    else:
        print("try lower num ")
else:
    print("You win !")
