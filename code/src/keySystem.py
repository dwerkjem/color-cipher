import random
from tableOfValues import key_freq_dict


def weightedRandomChoice(choices: dict, amount: int) -> list:
    """
    Given a dictionary of choices and their weights, this function will return a list of choices based on their weights.
    """
    total = sum(choices.values())
    result = []
    for _ in range(amount):
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices.items():
            upto += w
            if upto > r:
                result.append(c)
                break
    return result


def generateKey(key_length: int) -> str:
    """
    Given a key length, this function will generate a key based on the key_freq_dict.
    """
    return "".join(weightedRandomChoice(key_freq_dict(), key_length))
