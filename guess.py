import random
import sys


def guess():
    secret = random.randint(1,100)
    #print(secret)

    while True:
        number = int(input("угадай число от 1 до 100: "))
        #print(number)

        if number > secret:
            print("слишком большое")

        if number < secret:
            print("слишком маленькое")

        if number == secret:
            print("вы угадали")
            break