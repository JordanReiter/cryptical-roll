import re
import secrets

def parse_roll(input):
    count, diceFaces = input.split('d')
    try:
        diceFaces, modifier = re.split('[-+]', diceFaces)
        modifier = int(modifier)
        if f'-{modifier}' in input:
            modifier *= -1
    except ValueError:
        modifier = None
    if not count:
        count = 1
    count = int(count)
    dice = count * [int(diceFaces)]
    if modifier is not None:
        return (dice, modifier)
    return dice

def roll_die(faces):
    return secrets.randbelow(faces) + 1

def roll_dice(input):
    return [
        roll_die(ii)
        for ii in input
    ]

def get_roll_result(dice, modifier=None):
    modifier = modifier or 0
    dice_sum = sum(roll_dice(dice))
    return dice_sum + modifier
