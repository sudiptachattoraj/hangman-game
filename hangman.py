import random
import time
words=['Bird','Dog','cat','human','jeep','pond','Sweet','tree','Garden','pillow']
name=input("enter your name")
print ('welcome',name,'to the game of hangman')
guess=random.choice(words)
print("word is of length",len(guess))
print("The game is about to start")
print("wait for few seconds")
time.sleep(2)
fail=0
guesses=""
#validwords='a' or 'b' or'c' or'd' or'e' or'f' or'g' or'h' or 'i' or'j'or 'k' or'l' or'm' or'n' or'o' or'p' or'q' or'r' or's' or't' or'u' or'v' or'w' or'x' or'y' or 'z' or'A' or'B' or'C' or'D' or 'E' or 'F'or 'G' or'H' or'I' or'J' or'K' or'L' or 'M' or'N' or'O' or'P' or'Q' or'R' or'S' or'T' or'U'or 'V'or 'W' or'X' or 'Y' or 'Z'
print('if you enter the correct character then it will give the  msg else if you give wrong input then it will blank')
turns=int(input("enter the number of turns you want"))
#tur=turns
l1=len(guess)

correct=0
    
for i in range(turns):
    char=input('enter the character')
    for x in guess:
        if x==char:
            if char in x:
                print('the character that you entered is correct and the character is ',char)
                print()
            guesses=guesses+char.join(x)
            turns-=1
            correct+=1
            
                
        else:
            turns-=1
            fail+=1
            
        
        
        if guess==guesses:
            print('you have won the game')
            print()
            print('the actual word is',guess)
            break
    if guess==guesses:
       break
if guess!=guesses:
    print('you lost the game')
    print()
    print('the actual word is',guess)
             
        
    
    
