import random

# 4 players, 3 computers
# 400 units to begin with

score = 0
pop = 400
rounds=1

instructions = input('''
You are now a farmer in 1978 Valencia, Spain. You and several other farmer friends rely on
taking water from the irrigation canal that runs through the area to water your orange trees.
However, in the past couple of years, water supply has been low, and concerns have been raised about
how much water each farmer should get.

There are 4 different scenarios in this game that address
the water shortage problem. You will play through rounds for each scenario - one round represents one year,
and the number of rounds you play is based on your decision each precedent round.
Every year, you will decide how much water to take from the irrigation canal by typing and entering a number.

There are 3 other farmers in this game who will be making the same decision.
If you made a mistake and would like to restart the scenario, simply type and enter ‘quit’

Note: Each scenario starts off with 400 kiloliters of available water in the canal.

Press <Space> then <Enter> to continue.

''')

if (instructions.isspace()) == True:

    while True:

        take = input('How many kiloliters of water will you take? (This amount *MUST* be less than the current amount of water left) ')

        if take == 'quit':
            break

        try:
            print('YEAR {}'.format(rounds))

            rand1 = random.randint(1,int(pop/2)) # need try/except because this throws error if pop <= 0
            rand2 = random.randint(1,int(pop/4))
            rand3 = random.randint(1,int(pop/8))
            # rand1 = 67
            # rand2 = 67
            # rand3 = 67


            new_amt = pop - int(take) - rand1 - rand2 - rand3
            #print(rand1, rand2, rand3) # check

            if new_amt <= 0: # triggered if too much is taken
                share = new_amt + int(take)
                if share <= 0: # if no units left for user after the computers take
                    print('The irrigation canal has dried up. Game over')
                    print('You got 0 kiloliters of water this round')
                    print('Your final score is {}'.format(score))

                else: # if some units left for user after the computers take
                    print('The irrigation canal has dried up. Game over')
                    print('You got {} kiloliters this round'.format(share)) # the leftover amount after goods are exhausted
                    print('Your final score is {}'.format(score + share))

                    if rounds <= 2:
                        print("Nice try! Try harder next time!")
                    else:
                        print('Good run!')
                break

            else:
                score += int(take)
                #print(new_amt) # check
                pop = int(new_amt*2)

            print('There are now {} kiloliters of water left'.format(pop))
            print('You have {} kiloliters'.format(score))
            rounds+=1
            #print(pop) # check


        except: # triggered if not enough units for the computer players at the beginning of each round
            print('Uh-oh, the canal has dried up. Game over. Your final score is {}'.format(score))
            #print(new_amt) # check
            break
































# d
