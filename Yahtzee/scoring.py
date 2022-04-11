"""
    This module contains all of the functions related to scoring
"""
import constants

def getCounts(dice):
    """ this helper function takes a list of 5 dice as its parameter and returns an list
        The list contains the number of 1, 2, 3, 4, 5 and 6 represented in the dice
    """

    # create list to store number of counts
    counts = []

    # check each die rolled and count values
    value = 1
    for die in dice:
        count = 0

        # add count to list
        counts.append(count)

        # increase value
        value += 1
    
    return counts

def getTotal(counts):
    """ this helper function takes the list of counts as its parameter and returns the sum of the values of the dice
    """
    total = 0
    value = 1

    # calculate sum of counts with corresponding values
    for c in counts:
        total += c * value
        value += 1

    return total


def hasCount(howMany, counts):
    """ this helper function takes and integer and the list of counts as its parameters.
    It returns true if any of the values in count match the integer parameter.
    This function is used in scoreThreeOfAKind (for example) to determine if there are 3 of any number.
    """
    hasNumCounts = False

    for c in counts:
        if howMany == c:
            hasNumCounts = True

    return hasNumCounts


def scoreOnes(counts):
    """ this function should be used as a model for scoring 2 - 6
    """
    return counts[constants.ONES] * 1


def scoreTwos(counts):
    return counts[constants.TWOS] * 2


def scoreThrees(counts):
    return counts[constants.THREES] * 3


def scoreFours(counts):
    return counts[constants.FOURS] * 4


def scoreFives(counts):
    return counts[constants.FIVES] * 5


def scoreSixes(counts):
    return counts[constants.SIXES] * 6

def scoreThreeOfAKind(counts):
    """ this function should be used as a model for scoring 4 of a kind, yahtzee and full house
    """
    if hasCount(3, counts):
        return getTotal(counts)
    else:
        return 0


def scoreFourOfAKind(counts):
    if hasCount(4, counts):
        return getTotal(counts)
    else:
        return 0


def scoreFullHouse(counts):
    if hasCount(3, counts) and hasCount(2, counts):
        return getTotal(counts)
    else:
        return 0


def scoreSmallStraight(counts):
    for i in range(constants.THREES, constants.FOURS + 1):
        if counts[i] == 0:
            return 0
    if (counts[constants.ONES] >= 1 and counts[constants.TWOS] >= 1) \
        or (counts[constants.TWOS] >= 1 and counts[constants.FIVES] >= 1) \
            or (counts[constants.FIVES] >= 1 and counts[constants.SIXES] >= 1):
        return 30
    else:
        return 0


def scoreLargeStraight(counts):
    for i in range(constants.TWOS, constants.FIVES + 1):
        if counts[i] == 0:
            return 0
    if counts[constants.ONES] == 1 or counts[constants.SIXES] == 1:
        return 40
    else:
        return 0


def scoreYahtzee(counts):
    return 0


def scoreChance(counts):
    return 0


def score(whichElement, dice):
    counts = getCounts(dice)
    if whichElement == constants.ONES:
        return scoreOnes(counts)
    elif whichElement == constants.TWOS:
        return scoreTwos(counts)
    elif whichElement == constants.THREES:
        return scoreThrees(counts)
    elif whichElement == constants.FOURS:
        return scoreFours(counts)
    elif whichElement == constants.FIVES:
        return scoreFives(counts)
    elif whichElement == constants.SIXES:
        return scoreSixes(counts)
    elif whichElement == constants.THREE_OF_A_KIND:
        return scoreThreeOfAKind(counts)
    elif whichElement == constants.FOUR_OF_A_KIND:
        return scoreFourOfAKind(counts)
    elif whichElement == constants.FULL_HOUSE:
        return scoreFullHouse(counts)
    elif whichElement == constants.SMALL_STRAIGHT:
        return scoreSmallStraight(counts)
    elif whichElement == constants.LARGE_STRAIGHT:
        return scoreLargeStraight(counts)
    elif whichElement == constants.CHANCE:
        return scoreChance(counts)
    elif whichElement == constants.YAHTZEE:
        return scoreYahtzee(counts)
    else:
        return 0