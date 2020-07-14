#!/usr/bin/env python3

import re
import random


def parse(diceString):
    # Check if diceString is a string
    if not isinstance(diceString, str):
        print("The provided input must be a string")
        return

    # Strips trailing and leading whitespace from input
    diceString = diceString.strip().lower()

    # Check if valid string
    if not re.match('^[0-9]*[dD][1-9][0-9]*\s*([+-][0-9]*)?\s*([kKdD][lLhH][0-9]*)?$', diceString):
        print("The provided string is not a valid dice role")
        return

    # Get the amount of dice
    amount = re.search('[0-9]+[dD]', diceString)
    if amount:
        print("Number of dice: %s" % (amount.group(0)[:-1]))
        amount = int(amount.group(0)[:-1])
    else:
        amount = 1

    # Don't roll more than 10,000 dice
    if amount > 10000:
        print("Too many dice, exiting")
        return

    # Get the type of dice
    sides = re.search('[dD][0-9]+', diceString)
    if sides:
        print("Number of sides: %s" % (sides.group(0)[1:]))
        sides = int(sides.group(0)[1:])

    # Get roll modifier
    mod = re.search('[\+\-][0-9]+', diceString)
    if mod:
        print("Modifier for roll: %s" % (mod.group(0)))
        mod = int(mod.group(0))
    else:
        mod = 0

    # Get dice to keep/drop
    keep = re.search('[kKdD][lLhH][0-9]+', diceString)
    if keep:
        # Get amount to keep/drop
        keep_drop_amount = int(keep.group(0)[2:])
        # Get keeping
        if (keep.group(0)[0:1] == "k"):
            # Get high/low
            if(keep.group(0)[1:2] == "l"):
                print("Keep: Low")
                high = False
            else:
                print("Keep: High")
                high = True
            print("amount of dice to keep: %s" % (keep.group(0)[2:]))
            # Set keep/drop
            keep = True
            drop = False
        # Get dropping
        else:
            # Get high/low
            if(keep.group(0)[1:2] == "l"):
                print("Drop: Low")
                high = False
            else:
                print("Drop: High")
                high = True
            print("amount of dice to drop: %s" % (keep.group(0)[2:]))
            # Set keep/drop
            keep = False
            drop = True
    else:
        keep = False
        drop = False
        high = False
        keep_drop_amount = 0

    if(drop or keep and keep_drop_amount > amount):
        print("Too many dice kept/dropped: Keeping/Dropping all dice")
        keep_drop_amount = amount

    # Roll parsed dice
    roll(amount, sides, mod, keep, drop, high, keep_drop_amount)


def roll(amount, sides, modifier, keep=False, drop=False, high=True, keep_drop_amount=0):
    # Initialize list
    rollList = []

    # Generate all rolls
    for i in range(0, amount):
        rollList.append(random.randint(1, sides))

    # Sort the rolls
    rollList = sorted(rollList) if high else sorted(rollList, reverse=True)

    if(keep):
        # Initialize list of rolls to keep
        keepList = []
        # Pull out rolls to keep
        for i in range(0, keep_drop_amount):
            keepList.append(rollList.pop())
        # Print adjusted rolls
        print("Kept dice: ", keepList)
        print("Discarded Dice: ", rollList)
        print("Total: ", (sum(keepList) + modifier))
        return (keepList, (sum(keepList) + modifier), rollList)
    elif(drop):
        # Initialize list of rolls to keep
        dropList = []
        # Pull out rolls to keep
        for i in range(0, keep_drop_amount):
            dropList.append(rollList.pop())
        # Print adjusted rolls
        print("Kept dice: ", rollList)
        print("Discarded Dice: ", dropList)
        print("Total: ", (sum(rollList) + modifier))
        return (rollList, (sum(rollList) + modifier), dropList)
    else:
        print(rollList, (sum(rollList) + modifier))
        return (rollList, (sum(rollList) + modifier), [])


# Main function to run if file is called directly
if __name__ == '__main__':
    diceString = ''
    while(True):
        # Get the users input
        print("Please input the dice you want to roll:")
        diceString = input().lower()
        # Exit program on input being exit
        if (diceString == "exit"):
            break
        # Pass input to parser
        parse(diceString)
        # Line brake for rolls
        print("\n--------------------------------------------\n")
