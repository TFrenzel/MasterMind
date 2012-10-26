'''
Created on Oct 24, 2012

@author: TFrenzel

Mastermind.py 

A player thinks of a number while his opponent tries to guess the secret code.
Each guess has the player tell how many numbers in the code are exact matches and how many
are present in the code but incorrect location.

'''
from random import randint

MAXSIZE = 4
MAXDIGIT = 9

def match(guess, solution):
    exact = 0
    inexact = 0      
    for x in range(MAXSIZE):
        if guess[x] == solution[x]:
            guess[x] = '*'
            solution[x] = '*'
            exact+=1          
    
    for i in range(MAXSIZE):
        for x in range(MAXSIZE):
            if guess[i] == solution[x] and guess[i] !='*':
                print guess
                guess[i] = '*'
                solution[x] = '*'
                inexact+=1
                
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



def run():
    solutions = genSolutionPool()
    initialGuess = [randint(0,9), randint(0,9), randint(0,9), randint(0,9)]
    gameOver = False
    
    answer = raw_input("Is your number " + ''.join(str(num) for num in initialGuess)+" ?\n")
    if answer.lower() is "yes":
        gameOver = True
        print "Great! Thanks for playing!" 
    else: 
        exact = raw_input("How many digits are exact matches?\n")
        inexact = raw_input("How many digits are present but in the wrong spot?\n") 
    while not gameOver: 
       raw_input()
    
    return

if __name__ == '__main__':
    print "Welcome to the Game of Mastermind"
    print "Think of a 4 digit code for me to guess."
    run()


