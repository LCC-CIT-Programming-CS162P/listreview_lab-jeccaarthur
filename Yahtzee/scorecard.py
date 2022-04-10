"""
    This module contains all of the functions related to working with the scorecard
"""

import constants
from playing import clear

def resetScorecard(scorecard):
    """ takes the 2-d list that represents the scorecard as it's parameter and
    sets each of the individual values for the user and the computer to the constant empty.
    The subtotal, bonus and total should be set to 0.
    It does not return a value but the scorecard is altered by the function
    """
    for card in scorecard:
        card[constants.ONES] = constants.EMPTY
        card[constants.TWOS] = constants.EMPTY
        card[constants.THREES] = constants.EMPTY
        card[constants.FOURS] = constants.EMPTY
        card[constants.FIVES] = constants.EMPTY
        card[constants.SIXES] = constants.EMPTY
        card[constants.THREE_OF_A_KIND] = constants.EMPTY
        card[constants.FOUR_OF_A_KIND] = constants.EMPTY
        card[constants.FULL_HOUSE] = constants.EMPTY
        card[constants.SMALL_STRAIGHT] = constants.EMPTY
        card[constants.LARGE_STRAIGHT] = constants.EMPTY
        card[constants.CHANCE] = constants.EMPTY
        card[constants.YAHTZEE] = constants.EMPTY
        card[constants.SUBTOTAL] = 0
        card[constants.BONUS] = 0
        card[constants.TOTAL] = 0

def updateScorecard(scorecard):
    """ takes the 2-d list that represents the scorecard as it's parameter and
    calculates the subtotal, bonus and total for both the user and the computer.
    It does not return a value but the scorecard is altered by the function
    """
    for card in scorecard:
        card[constants.SUBTOTAL] = 0
        card[constants.BONUS] = 0
        card[constants.TOTAL] = 0

        # count all scores on card up to subtotal
        for i in range(constants.SUBTOTAL):
            if card[i] != constants.EMPTY:
                card[constants.SUBTOTAL] += card[i]

        # if subtotal is 63 or more, award bonus
        if card[constants.SUBTOTAL] >= 63:
            card[constants.BONUS] += 35

        # calculate total
        card[constants.TOTAL] = card[constants.SUBTOTAL] + card[constants.BONUS]

def formatCell(value):
    return "" if value < 0 else str(value)


def displayScorecards(scorecard):
    labels = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
              "3 of a Kind", "4 of a Kind", "Full House", "Small Straight", "Large Straight",
              "Chance", "Yahtzee", "Sub Total", "Bonus", "Total Score"]
    lineFormat = "| {3:2s} {0:<15s}|{1:>8s}|{2:>8s}|"
    border = '-' * 39
    uScorecard = scorecard[constants.USER]
    cScorecard = scorecard[constants.COMPUTER]

    #clear()
    print(border)
    print(lineFormat.format("", "  You   ", "Computer", ""))
    print(border)

    for i in range(constants.ONES, constants.SIXES + 1):
        print(lineFormat.format(labels[i], formatCell(uScorecard[i]), formatCell(cScorecard[i]), str(i)))

    print(border)
    print(lineFormat.format(labels[constants.SUBTOTAL], formatCell(uScorecard[constants.SUBTOTAL]), formatCell(cScorecard[constants.SUBTOTAL]), ""))
    print(border)
    print(lineFormat.format(labels[constants.BONUS], formatCell(uScorecard[constants.BONUS]), formatCell(cScorecard[constants.BONUS]), ""))
    print(border)

    for i in range(constants.THREE_OF_A_KIND, constants.YAHTZEE + 1):
        print(lineFormat.format(labels[i], formatCell(uScorecard[i]), formatCell(cScorecard[i]), str(i)))

    print(border)
    print(lineFormat.format(labels[constants.TOTAL], formatCell(uScorecard[constants.TOTAL]), formatCell(cScorecard[constants.TOTAL]), ""))
    print(border)




