from random import random, randrange
import time

for flip in range(3):
    time.sleep(3)
    val  = randrange(1, 6)
    if val == 1:
        print("*")
    elif val == 2:
        print("**")
    elif val == 3:
        print("***")
    elif val == 4:
        print("****")
    elif val == 5:
        print("*****")
    elif val == 6:
        print("******")
    else:
        print("ERROR!!!!!!")
