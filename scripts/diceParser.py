#!/usr/bin/env python3

import re

def parse( diceString ):
    dice = re.search('[0-9]*d[0-9]+', diceString)
    print(dice.group(0))
