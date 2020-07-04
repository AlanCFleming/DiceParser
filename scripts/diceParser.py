#!/usr/bin/env python3

import re

def parse( diceString ):
    #get the type of dice
    sides = re.search('[dD][0-9]+', diceString)
    if sides:
        print(sides.group(0))

    #get the ammount of dice
    ammount = re.search('[0-9]+[dD]', diceString)
    if ammount:
        print(ammount.group(0))

    #get roll modifier
    mod = re.search('[\+\-][0-9]+', diceString)
    if mod:
        print(mod.group(0))

    #get dice to keep/drop
    keep = re.search('[kKdD][lLhH][0-9]+', diceString)
    if keep:
        print(keep.group(0))
