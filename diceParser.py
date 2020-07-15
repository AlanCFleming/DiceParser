#!/usr/bin/env python3

import re
import random
import time

def parse(diceString, verbose = False):
    # Check if diceString is a string
    if not isinstance(diceString, str):
        if( verbose ):
            print("The provided input must be a string")
        return -1

    # Strips trailing and leading whitespace from input
    diceString = diceString.strip().lower()

    # Check if valid string
    if not re.match('^[0-9]*[dD][1-9][0-9]*\s*([+-][0-9]*)?\s*([kKdD][lLhH][0-9]*)?$', diceString):
        if( verbose ):
            print("The provided string is not a valid dice role")
        return -1

    # Get the amount of dice
    amount = re.search('[0-9]+[dD]', diceString)
    if amount:
        amount = int(amount.group(0)[:-1])
    else:
        amount = 1

    # Get the type of dice
    sides = re.search('[dD][0-9]+', diceString)
    if sides:
        sides = int(sides.group(0)[1:])

    # Get roll modifier
    mod = re.search('[\+\-][0-9]+', diceString)
    if mod:
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
                high = False
            else:
                high = True

            # Set keep/drop
            keep = True
            drop = False
        
        # Get dropping
        else:
            
            # Get high/low
            if(keep.group(0)[1:2] == "l"):
                high = False
            else:
                high = True

            # Set keep/drop
            keep = False
            drop = True

    else:
        keep = False
        drop = False
        high = False
        keep_drop_amount = 0

    if((drop or keep) and keep_drop_amount > amount):
        if( verbose ):
            print("Too many dice kept/dropped: Keeping/Dropping all dice")
        keep_drop_amount = amount

    # Return results of parsing
    return(amount, sides, mod, keep, drop, high, keep_drop_amount)


def roll(amount, sides, modifier, keep=False, drop=False, high=True, keep_drop_amount=0 , time_out = 10):
    # Initialize list
    roll_list = []

    # Calculate timeout time
    time_out = time_out + time.time()

    # Generate all rolls
    for i in range(0, amount):
        
        # Return error if timeout is reached
        if( time.time() > time_out):
            return -1
        
        # Append to roll list otherwise 
        roll_list.append(random.randint(1, sides))


    # Sort the rolls
    roll_list = sorted(roll_list) if high else sorted(roll_list, reverse=True)


    if(keep):
        
        # Initialize list of rolls to keep
        keep_list = []

        # Pull out rolls to keep
        for i in range(0, keep_drop_amount):
            keep_list.append(roll_list.pop())
        
        # Print adjusted rolls
        return (keep_list, (sum(keep_list) + modifier), roll_list)
    elif(drop):
        
        # Initialize list of rolls to keep
        dropList = []
        
        # Pull out rolls to keep
        for i in range(0, keep_drop_amount):
            dropList.append(roll_list.pop())
        
        # Print adjusted rolls
        return (roll_list, (sum(roll_list) + modifier), dropList)
    
    else:
        print(roll_list, (sum(roll_list) + modifier))
        return (roll_list, (sum(roll_list) + modifier), [])


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
        amount , sides , modifier , keep , drop , high , keep_drop_amount = parse(diceString)

        # Print parcing results
        print("Number of dice: %s" % (amount))
        print("Number of sides: %s" % (sides))
        print("Modifier for roll: %s" % (modifier))

        if( keep and high ):
            print("Keep: High")
        elif( keep and not high ):
            print("Keep: Low")
        elif( drop and high ):
            print("Drop: High")
        elif( drop and not high ):
            print("Drop: Low")

        if( keep or drop ):
            print("amount of dice to keep: %s" % (keep_drop_amount))

        # Rolled parsed dice
        output = roll( amount , sides , modifier , keep , drop , high , keep_drop_amount , 30)

        if( isinstance( output , tuple )):
            #break apart tuple output
            keep_list , roll_list , total = output
            
            # Print roll results
            print("Kept dice: %s" % (keep_list))
            print("Discarded Dice: %s" % (roll_list))
            print("Total: %s" % (total))
        else:
            print("The dice took too long to roll")


        # Line brake for rolls
        print("\n--------------------------------------------\n")
