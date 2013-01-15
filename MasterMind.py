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
MAXDIGIT = 3

def match(guess, prevGuess):
    exact = 0
    inexact = 0
    matchIndex = []
    indirectMatches = []
   
    #print "My new Guess: " + ''.join(str(num) for num in guess)
    #print "My old Guess "+''.join(str(num) for num in prevGuess)
         
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
    print len(solutions)
    newSolutionSet = []
    count = 0
    for x in range(len(solutions)):
        newStats = match(solutions[x], prevGuess)
        
        if newStats[0] > stats[0] and newStats[0] != 0:
            #print "New Stats %r%r" % newStats
            #print "Old Stats %r%r" % stats
            newSolutionSet.append(solutions[x])
            print solutions[x]
            
        elif newStats[1] >= stats[1]:
            newSolutionSet.append(solutions[x])
            print solutions[x]

        count += 1
    print count    
    return newSolutionSet


def run():
    solutions = genSolutionPool()
    guess = [randint(0,MAXDIGIT-1), randint(0,MAXDIGIT-1), randint(0,MAXDIGIT-1), randint(0,MAXDIGIT-1)]
    guesses = []
    guesses.append(guess)
    solutions.remove(guess)
    gameOver = False
    answer = raw_input("Is your number " + ''.join(str(num) for num in guess)+" ?\n")
    if(answer.lower() !="yes"):
        exact = int(raw_input("How many are exact matches?\n"))
        inexact = int(raw_input("How many are inexact matches?\n"))
        print "1st guess " +''.join(str(num) for num in guess)
        solutions = removeSolutions(solutions, guess, (exact, inexact))
        
        #print solutions
        #sys.exit(1)
    else: gameOver = True
    
    while not gameOver:
        guess = solutions[randint(0, len(solutions)-1)]
        raw_input("Is your number " + ''.join(str(num) for num in guess))  
        exact = int(raw_input("How many are exact matches?\n"))
        inexact = int(raw_input("How many are inexact matches?\n"))
        if exact == 4: gameOver = True
        else: solutions = removeSolutions(solutions, guess, (exact, inexact))
      
    print "Thanks for playing!!"
    sys.exit(1)
    

if __name__ == '__main__':
    print "Welcome to the Game of Mastermind"
    print "Think of a 4 digit code for me to guess."
    run()


