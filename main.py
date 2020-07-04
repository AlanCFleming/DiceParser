#!/usr/bin/env python3

from scripts import diceParser

diceString = ''
while(True):
    #get the users input
    print("please input the dice you want to roll:")
    diceString = input().lower()
    
    #exit program on input being exit
    if (diceString == "exit"):
        break
    
    #pass input to parser
    diceParser.parse(diceString)
