import random
import time

def dice_roll():
        low = int(input("Enter you low number: "))
        high = int(input("Enter you high number: "))
        guess = int(input("Enter your guess: "))
        start_time = time.time()
        total = 0
        while True:
                roll = random.randint(low,high)
                if (roll > guess):
                        print("Your guess is less than " + str(roll))
                if (roll < guess):
                        print("Your guess is greater than " + str(roll))
                total += 1
                if (roll == guess):
                        print("It took "+ str(total) + " tries")
                        print("--- %s seconds ---" % (time.time() - start_time))
                        dice_roll()
                        break
                

dice_roll()
