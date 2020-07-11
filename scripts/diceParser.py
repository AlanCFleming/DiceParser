#!/usr/bin/env python3

import re
import random

def parse( diceString ):

    #check if diceString is a string
    if not isinstance(diceString, str):
        print("The provided input must be a string")
        return

    #strips trailing and leading whitespace from input
    diceString = diceString.strip().lower()

    #check if valid string
    if not re.match('^[0-9]*[dD][1-9][0-9]*\s*([+-][0-9]*)?\s*([kKdD][lLhH][0-9]*)?$', diceString):
        print("The provided string is not a valid dice role")
        return

    #get the ammount of dice
    ammount = re.search('[0-9]+[dD]', diceString)
    if ammount:
        print("Number of dice: %s" % (ammount.group(0)[:-1]))
        ammount = int(ammount.group(0)[:-1])

    #get the type of dice
    sides = re.search('[dD][0-9]+', diceString)
    if sides:
        print("Number of sides: %s" % (sides.group(0)[1:]))
        sides = int(sides.group(0)[1:])

    #get roll modifier
    mod = re.search('[\+\-][0-9]+', diceString)
    if mod:
        print("Modifier for roll: %s" % (mod.group(0)))
        mod = int(mod.group(0))
    
    #get dice to keep/drop
    keep = re.search('[kKdD][lLhH][0-9]+', diceString)
    if keep:
        #get ammount to keep/drop
        keepDropAmmount = int(keep.group(0)[2:])
        #get keeping
        if (keep.group(0)[0:1] == "k"):
            #get high/low
            if(keep.group(0)[1:2] == "l"):
                print("Keep: Low")
                high = False
            else:
                print("Keep: High")
                high = True
            print("Ammount of dice to keep: %s" % (keep.group(0)[2:]))
            #set keep/drop
            keep = True
            drop = False
        #get dropping
        else:
            #get high/low
            if(keep.group(0)[1:2] == "l"):
                print("Drop: Low")
                high = False
            else:
                print("Drop: High")
                high = True
            print("Ammount of dice to drop: %s" % (keep.group(0)[2:]))
            #set keep/drop
            keep = False
            drop = True
    else:
        keep = False
        drop = False
        high = False
        keepDropAmmount = 0

    #print(ammount, sides, mod, keep, drop, high, keepDropAmmount)
    #roll parsed dice
    roll(ammount, sides, mod, keep, drop, high, keepDropAmmount)

def roll(ammount, sides, modifier, keep = False, drop = False, high = True, keepDropAmmount = 0):

    #initialize list
    rollList = []

    #generate all rolls
    for i in range(0, ammount):
        rollList.append(random.randint(1 , sides))

    print(sorted(rollList), sum(rollList))
    

