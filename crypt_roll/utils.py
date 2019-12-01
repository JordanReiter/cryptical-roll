def parse_roll(input):
    count, diceFaces = input.split('d')
    if not count:
        count = 1
    count = int(count)
    return count * [int(diceFaces)]