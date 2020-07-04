#!/usr/bin/env python3

import re

def parse( diceString ):
    #get dice ammount and type
    dice = re.search('[0-9]*d[0-9]+', diceString)
    if dice:
        print(dice.group(0))

    #get roll modifier
    mod = re.search('[\+\-][0-9]+', diceString)
    if mod:
        print(mod.group(0))

    #get dice to keep/drop
    keep = re.search('[kKdD][lLhH][0-9]+', diceString)
    if keep:
        print(mod.group(0))
