# This is a rock paper scissors game in Python

#Goal
#Ask the player if they pick rock paper or scissors
#Have the computer chose its move
#Compare the choices and decide who wins
#Print the results

#Subgoals
#Let the player play again
#Keep a record of the score e.g. (Player: 3 / Computer: 6)

import random

def user_choice():
    c = (raw_input("Please pick your move: ").lower()); 
    if ((c != "rock") and (c != "paper") and (c !="scissors")):
        print "Pick either rock, paper or scissors";
        c = user_choice();
    return c;

def comparing(user,comp):
    u_score = 1;
    c_score = 0;
    if (user == comp):
        print "It's a draw!"
        return 2;

    if ((user == "rock") and (comp == "paper")):
        print "Computer wins this round."
        return c_score;
    elif ((user == "rock") and (comp == "scissors")):
        print "You win this round."
        return u_score;
    if ((user == "paper") and (comp == "rock")):
        print "You win this round."
        return u_score; 
    elif ((user == "paper") and (comp == "scissors")):
        print "Computer wins this round."
        return c_score;
    if ((user == "scissors") and (comp == "paper")):
        print "You win this round."
        return u_score;
    elif ((user == "scissors") and (comp == "rock")):
        print "Computer wins this round."
        return c_score;


def main():
    print "Welcome to my Rock Paper Scissors program.";
    cont = "yes";
    user_score = 0;
    comp_score = 0;
    while (cont == "yes"):
        choice = user_choice();
        comp_int = (int)(random.randint(1,3));
        #For debugging: print "Choice of numb is "+str(comp_int);
        choices = {'1': 'rock', '2': 'scissors', '3': 'paper'};
        comp_choice = choices[str(comp_int)];
        print "You played: "+choice;
        print "Computer plays: "+comp_choice;
        a = comparing(choice, comp_choice);
        if (a==1):
            user_score +=1;
        elif (a==0):
            comp_score +=1;
        cont = raw_input("Another game?(yes/no) ").lower();
    
    print "Player: "+str(user_score)+" / Computer: "+str(comp_score);

main()
