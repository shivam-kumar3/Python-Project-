import random
l= ["Rock", "Scissor", "Paper"]
while True:
    ccount=0
    ucount=0
    userchoice = int(input( '''
Game Start....
1 YES
2 NO | Exit
'''))
    if userchoice ==1:
       for a in range (1,6):
            userinput= int(input('''
1 Rock
2 Scissor
3 Paper           
'''))
            if userinput == 1:
                selected = "Rock"
            elif userinput ==2:
                selected = "Scissor"
            elif userinput == 3:
                selected = "Paper"
            cchoice= random.choice(l)
           
            if cchoice == selected:
                print("You Choose",selected)
                print("Computer's choice",cchoice)
                print("Game Draw")
                ccount=ccount+1
                ucount=ucount+1
            elif (selected =="Rock" and cchoice =="scissor") or (selected=="Paper" and selected=="Rock") or (selected == "Scissor" and cchoice =="Paper"):
                print("You Choose",selected)
                print("Computer's choice",cchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("You Choose",selected)
                print("Computer's choice",cchoice)
                print("You Loose")
                ccount=ccount+1
       if ucount==ccount:
            print("Final Game Draw")
            print("User Score", ucount)
            print("Computer Score", ccount)
       elif ucount > ccount:
            print("You Won")
            print("User Score", ucount)
            print("Computer Score", ccount)
       else:
            print("Computer win the game...")
            print("User Score", ucount)
            print("Computer Score", ccount)
            
    else:
        break
        