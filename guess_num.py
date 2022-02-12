from random import randint
# import random

max_border = 50

min_border = 1

answer = randint(min_border, max_border)

while(True):

    n = int(input("please input positive integer[" + str(min_border) + " <= n <= " + str(max_border) + "]:\n"))

    if (n > max_border) or (n < min_border):

        print("Input out of range.\n")
    
    else:

        if n == answer:

            print("Bingo !")
            break
        
        else:

            if n > answer:

                max_border = n
                print("Input positive integer between", min_border, "and", max_border, ".\n")
            
            else:

                min_border = n
                print("Input positive integer between", min_border, "and", max_border, ".\n")


