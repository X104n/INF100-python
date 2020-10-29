import time, sys, random
indent = 0 #How many spaces to indent
indentIncreasing = True #Wheter the indentation is increasing or not

randomNumber = 20

try:
    while True: #The main program loop.r
        print(' ' * indent, end='')
        print('***********')
        time.sleep(0.01) #Pause for 1/10 of a second

        if indentIncreasing:
            #Increase the number of spaces:
            indent = indent + 1
            if indent == randomNumber:
                #Change directions:
                indentIncreasing = False
            
        else:
            #Decrease the number of spaces:
            indent = indent -1
            if indent == 0:
                global x
                randomNumber = (randomNumber * random.randint(1, 240)) / randomNumber
                #Change directions:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()

