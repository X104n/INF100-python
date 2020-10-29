def spam():
    eggs = 'spam local'
    print(eggs) #Prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) #Prints 'bacon local'
    spam()
    print(eggs) #Prints 'bacon local'

def junk():
    global eggs
    eggs = 'junk' #Makes the global eggs to junk

eggs = 'global'
bacon()
junk() 
print(eggs) #Prints 'global'