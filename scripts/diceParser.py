#!/usr/bin/env python3

import re

def parse( diceString ):

    #check if diceString is a string
    if not isinstance(diceString, str):
        print("The provided input must be a string")
        return

    #strips trailing and leading whitespace from input
    diceString = diceString.strip()

    #check if valid string
    if not re.match('^[0-9]*[dD][0-9]+\s*([+-][0-9]*)?\s*([kKdD][lLhH][0-9]*)?$', diceString):
        print("The privided string is not a valid dice role")
        return

    #get the ammount of dice
    ammount = re.search('[0-9]+[dD]', diceString)
    if ammount:
        print("Number of dice: %s" % (ammount.group(0)))

    #get the type of dice
    sides = re.search('[dD][0-9]+', diceString)
    if sides:
        print("Number of sides: %s" % (sides.group(0)))
    
    #get roll modifier
    mod = re.search('[\+\-][0-9]+', diceString)
    if mod:
        print("Modifier for roll: %s" % (mod.group(0)))

    #get dice to keep/drop
    keep = re.search('[kKdD][lLhH][0-9]+', diceString)
    if keep:
        print("Ammount of dice to keep/drop: %s" % (keep.group(0)))
