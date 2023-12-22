from art import logo,vs
from gamedata import data
import os
from random import shuffle,choice

def clear_screen():
    os.system('cls')
    
def has_more_followers(dictA,dictB):
    return dictA['follower_count'] > dictB['follower_count']
        

def compare(dictA,dictB):
    global score
    print(f"Compare A: {dictA['name']}, a {dictA['description']}, from {dictA['country']}")
    print(vs)
    print(f"Against B: {dictB['name']}, a {dictB['description']}, from {dictB['country']}")
    
    guess=input("Who has more followers? Type 'A' or 'B':").lower()
    clear_screen()
    print(logo)
    if has_more_followers(dictA,dictB) and guess=='a':
        score+=1
        print(f"You are right! Current Score {score}.")
    elif not has_more_followers(dictA,dictB) and guess=='b':
        score+=1
        print(f"You are right! Current Score {score}.")
    else:
        print(f"Sorry, that's wrong.Final score: {score}")
        return 0
    return score
    
shuffle(data)
score=0
print(logo) 
dictA=choice(data)
dictB=choice(data)

while True:
    dictA=dictB
    dictB=choice(data)
    while dictA==dictB:
        dictB=choice(data)
    score=compare(dictA,dictB)   
    if score==0:
        break
        
        