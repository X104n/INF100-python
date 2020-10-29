#Rock Paper Sicors

import random, sys, time
print()
print('Welcome to The Rock, Paper, Sissors game!')
print()

#Variables to keep track of the score

wins = 0
losses = 0
ties = 0


#The main game
while True:
    print('Youre score is %s Wins, %s Losses, %s Ties!' % (wins, losses, ties))
    if losses > 0:
        print()
        print('your win/loss rate is currently' + str(wins/losses))
    while True:
        print()
        print('Choose Rock, Paper, or Sissor by their respective letter in lower case. (r, p, s). Press (q) to Quit if you are a gay man')
        playerMove = input()
        if playerMove == 'q':
            print()
            print('Initiating protocal gay man')
            print()
            sys.exit()
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #Continues the game
        print()
        print()
        print('Type r, p, s or fucking q (for the fucking gayes of you) you stupid ass bitch motherfucking ass sittn incompetent lookn low iq human fucking beeing, go get yourself a job insted if you dont want to play by the rules')

    #Display the players move
    if playerMove == 'r':
        print()
        print('Ah, yes the ROCK a classic, you from the fucking ancient greece or something ready to stone someone?')
    elif playerMove == 'p':
        print()
        print('PAPER huh, yea probably heard a lot about that shit. The douhg, bread, moolah got thoose Benjis')
    elif playerMove == 's':
        print()
        print('So my man chooses the SISSORS? Didnt find ya shank did ya pall? Well guess who got it...')

    time.sleep(10)

    #Now what the machine chooses
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print()
        print('Now let me see here what this random ass computer thing got for me. A fucking ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print()
        print('How would you look at that? This mother fucker got one of the PAPERS')
    elif randomNumber == 3:
        computerMove = 's'
        print()
        print('Now why the fuck would i in Gods name need SISSORS?')

    #Display whos getting theese wins
    winner = 'This mother fucker out here winning, fucking tryhard'
    looser = 'Hah, would you look at that, guess that stupid ass of yours aint so high on that iq shit afterall'

    if playerMove == computerMove:
        print()
        print('Nah fam, why would you choose what i got, fucking morron. Another tie for us')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print()
        print(winner)
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print()
        print(winner)
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print()
        print(winner)
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print()
        print(looser)
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print()
        print(looser)
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print()
        print(looser)
        losses = losses + 1
