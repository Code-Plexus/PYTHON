#snake water gun game
import maskpass
import random
aa="sgw"
# for such things google random methods in python or ets etc
#comp+person
def cop(n):
    c=0
    p=0
    for i in range(0,n):
        r=random.choice(aa)
        ss=input(''' Enter your turn ::: (s) for snake ,(w) for water , (g) for gun \n''')
        if(ss=="s" or ss=="g" or ss=="w"):
            if(r==ss):
                print (" Tie ")
                print("you played : " ,ss ," computer played : " ,r )
            if((r=="g" and ss=="s" ) or (r=="w" and ss=="g") or (r=="s" and ss=="w")):
                print("you played : " ,ss ," computer played : " ,r )
                print("Defeat!")
                c=c+1
            if((r=="s" and ss=="g" ) or (r=="g" and ss=="w") or (r=="w" and ss=="s")):
                print("you played : " ,ss ," computer played : " ,r )
                print("Win!") 
                p=p+1
    if(c>p):
        print("You lost by points: " ,c-p)
    if(p>c):
        print("you won by points : ", p-c )
    if(p==c):
        print("Match is tie\n\n\n")     
    print("Your total scores : " ,p)
    print("Computer total score : " ,c)

#person+person
def cop2(n):
    c=0
    p=0
    for i in range(0,n):
        ss1=maskpass.askpass(prompt=''' Person 1 Enter your turn ::: (s) for snake ,(w) for water , (g) for gun : ''',mask=" 🐞")
        ss2=maskpass.askpass(prompt=''' Person 2 Enter your turn ::: (s) for snake ,(w) for water , (g) for gun : ''',mask=" 🐞")
        if(ss1==ss2):
            print (" Tie ")
        print("Player 1 played : " ,ss1 ," Player 2 played : " ,ss2 )
        if((ss1=="g" and ss2=="s" ) or (ss1=="w" and ss2=="g") or (ss1=="s" and ss2=="w")):
            print("Player 1 played : " ,ss1 ," Player 2 played : " ,ss2 )
            print("player 1 Wins!")
            c=c+1
        if((ss1=="s" and ss2=="g" ) or (ss1=="g" and ss2=="w") or (ss1=="w" and ss2=="s")):
            print("Player 1 played : " ,ss1 ," Player 2 played : " ,ss2 )
            print("Player 2 wins!") 
            p=p+1
    if(c>p):
        print("Person 1 wins by points: " ,c-p)
    if(p>c):
        print("Person 2 wins by points : ", p-c )
    if(p==c):
        print("Match is tie\n\n\n")     
    print("Person 1 total scores : " ,c)
    print("Person 2 total score : " ,p)

ch=int(input("Enter 1 to play with computer OR 2 to play with person : "))
if(ch==1):
    nn=int(input("Number of rounds you want to play : "))

    print(cop(nn))
if(ch==2):
    nn=int(input("Number of rounds you want to play : "))

    print(cop2(nn))
else:
    print("INVALID INPUT")
