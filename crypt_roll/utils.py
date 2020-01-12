import re
import secrets

from .log import get_logger

class CryptRoll:
    def __init__(self, log_level=5):
        self.log = get_logger(self.__class__.__name__, log_level)

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
            self.log.debug(f"Parsed dice: {input} -> {', '.join(str(d) for d in dice)} {'+' if modifier > 0 else ''}{modifier}")
            return (dice, modifier)
        self.log.debug(f"Parsed dice: {input} -> {', '.join(str(d) for d in dice)}")
        return (dice, None)

    def roll_die(self, faces):
        result = secrets.randbelow(faces) + 1
        self.log.info(f"Rolling a d{faces}...{result}")
        if result == 1 and faces == 20:
            self.log.egg("That's a natural one.")
        if result == 20 and faces == 20:
            self.log.egg("NATURAL TWENTY!!!")
        elif result >= 18 and faces == 20:
            self.log.egg(f"Hey, natural {result}!")
        return result

    def roll_dice(self, input):
        return [
            self.roll_die(ii)
            for ii in input
        ]

    def get_roll_result(self, dice, modifier=None, roll_with=None):
        modifier = modifier or 0
        rolled = self.roll_dice(dice)
        if roll_with:
            self.log.info(f"Second roll ({roll_with})")
            other_roll = self.roll_dice(dice)
            if roll_with == 'advantage' and sum(other_roll) > sum(rolled):
                rolled = other_roll
            if roll_with == 'disadvantage' and sum(other_roll) < sum(rolled):
                rolled = other_roll
        dice_sum = sum(rolled)
        modifier_disp = ''
        if modifier:
            if modifier > 0:
                modifier_disp = f' + {modifier}'
            else:
                modifier_disp = f' - {abs(modifier)}'
            modifier_disp += f' = {dice_sum + modifier}'
        self.log.info(f"Rolled {' + '.join(str(r) for r in rolled)} = {dice_sum}{modifier_disp}")
        if len(dice) > 1 and dice_sum / sum(dice) < 0.2:
            self.log.egg(f"Uhhhh, not good. {dice_sum}")
        if len(dice) > 1 and dice_sum / sum(dice) > 0.66:
            self.log.egg(f"Okay, okay, not bad. {dice_sum}.")
        return dice_sum + modifier
