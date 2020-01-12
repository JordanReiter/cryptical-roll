import re
import secrets

class CryptRoll:
    def parse_roll(self, input):
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

    def roll_die(self, faces):
        return secrets.randbelow(faces) + 1

    def roll_dice(self, input):
        return [
            self.roll_die(ii)
            for ii in input
        ]

    def get_roll_result(self, dice, modifier=None):
        modifier = modifier or 0
        dice_sum = sum(self.roll_dice(dice))
        return dice_sum + modifier
