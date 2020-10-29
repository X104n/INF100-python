import time, sys
indent = 0 #How many spaces to indent
indentIncreasing = True #Wheter the indentation is increasing or not

try:
    while True: #The main program loop.r
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.05) #Pause for 1/10 of a second

        if indentIncreasing:
            #Increase the number of spaces:
            indent = indent + 1
            if indent == 253:
                #Change directions:
                indentIncreasing = False
            
        else:
            #Decrease the number of spaces:
            indent = indent -1
            if indent == 0:
                #Change directions:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()