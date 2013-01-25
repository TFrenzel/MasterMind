'''
Created on Oct 24, 2012

@author: TFrenzel

Mastermind.py 

A player thinks of a number while his opponent tries to guess the secret code.
Each guess has the player tell how many numbers in the code are exact matches and how many
are present in the code but incorrect location.

'''
from random import randint
import sys

MAXSIZE = 4
MAXDIGIT = 6
EXACT = 0 ##location in tuples of exact matches
INEXACT = 1 ##location in tuples of inexact matches

bestGuess = [0, 0, []]


def match(guess, prevGuess):
    exact = 0
    inexact = 0
    matchIndex = []
    indirectMatches = []
         
    for x in range(MAXSIZE):
        if guess[x] == prevGuess[x]:
            matchIndex.append(x)
            exact+=1          
    
    for i in range(MAXSIZE):
        for x in range(MAXSIZE):
            if guess[i] == prevGuess[x] and x not in matchIndex and guess[i] not in indirectMatches:#guess[i] !='*':
                indirectMatches.append(guess[i])
                inexact+=1
    #print "result of Match: exact %r inexact %r" % (exact,inexact)            
    return (exact, inexact)
        

def genSolutionPool():
    solutionPool = []
    for a in range(MAXDIGIT):
        for b in range(MAXDIGIT):
            for c in range(MAXDIGIT):
                for d in range(MAXDIGIT):
                    code = [a,b,c,d]
                    solutionPool.append(code)
    return solutionPool     

def removeSolutions(solutions, prevGuess, stats):
    ##For Testing
    print len(solutions) 
    
    global bestGuess
    newSolutionSet = []
    solutions.remove(prevGuess)
    
    if stats[EXACT] > bestGuess[EXACT]:
        bestGuess = (stats[EXACT], stats[INEXACT], prevGuess)
    elif stats[EXACT] == bestGuess[EXACT] and stats[INEXACT] > bestGuess[INEXACT]:
        bestGuess = (stats[EXACT], stats[INEXACT], prevGuess)
   
    
    for x in range(len(solutions)):
        print solutions[x]
        newStats = match(solutions[x], bestGuess[2])
        
        ##We want all codes that have similar number of matches to our best guess
        if newStats[EXACT]+newStats[INEXACT] >= bestGuess[EXACT]+bestGuess[INEXACT]:
            ##We only want solutions potentially as good as our current best
            newSolutionSet.append(solutions[x])
        elif bestGuess[EXACT]+bestGuess[INEXACT]==0 and newStats[EXACT]+newStats[INEXACT]==0 :
            newSolutionSet.append(solutions[x])

        '''
        TODO: If we have a truly bad guess we should eliminate any answer similar to it
        '''
        
    print len(newSolutionSet)    
    return newSolutionSet


def run():
    solutions = genSolutionPool()
    guess = [randint(0,MAXDIGIT-1), randint(0,MAXDIGIT-1), randint(0,MAXDIGIT-1), randint(0,MAXDIGIT-1)]
    global bestGuess
    gameOver = False
    answer = raw_input("Is your number " + ''.join(str(num) for num in guess)+" ?\n")
    if(answer.lower() !="yes"):
        exact = int(raw_input("How many are exact matches?\n"))
        inexact = int(raw_input("How many are inexact matches?\n"))
        bestGuess = [exact, inexact, guess] ##Our first is our best so far.
        print "1st guess " +''.join(str(num) for num in guess)
        solutions = removeSolutions(solutions, guess, (exact, inexact))

    else: gameOver = True
    
    while not gameOver:
        if len(solutions)!=1:
            guess = solutions[randint(0, len(solutions)-1)]
            raw_input("Is your number " + ''.join(str(num) for num in guess)+"?\n")  
            exact = int(raw_input("How many are exact matches?\n"))
            inexact = int(raw_input("How many are inexact matches?\n"))
            solutions = removeSolutions(solutions, guess, (exact, inexact))
        else: 
            gameOver = True
            print "Your code is:"
            print solutions
            print "Thanks for playing!!"
            sys.exit(1)
        if exact == 4: gameOver = True
        
      
    print "Thanks for playing!!"
    sys.exit(1)
    

if __name__ == '__main__':
    print "Welcome to the Game of Mastermind"
    print "Think of a 4 digit code for me to guess."
    run()
   


