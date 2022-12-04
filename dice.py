import random 
import time 
 
print ("Hello Human !! \nLet's play a GAME. It's called DICE Game. ") 
print("You Enter a Number, I Roll the DICE.\nIf both matches, You WIN and get 5 Points.")
  
print ("LET's GET STARTED") 
no_of_wins = 0 
score = 0 
while (True):
    print ("Enter a Number betwen 1 and 6") 
    print ("Enter 0 to exit") 
    inp_num = int (input ()) 
    if (inp_num == 0): 
        print("Game Over") 
        break 
    elif (inp_num > 6 or inp_num < 1):
        print ("Invalid User Input") 
        continue 
    print ("Rolling the dice...") 
    time.sleep (2) 
    rand_num = random.randint (1, 6) 
    print ("Dice generated:", rand_num) 
    if (inp_num == rand_num):
        score = score + 5 
        no_of_wins += 1 
        print ("Both number Matched") 
    else:
        print ("LOL.. It did not match.. Try Again") 
      
print ("score:", score) 
print ("Total Wins:", no_of_wins)
if score==0:
    print("Accuracy:",0)
else:
    print ("Accuracy:", score / no_of_wins)