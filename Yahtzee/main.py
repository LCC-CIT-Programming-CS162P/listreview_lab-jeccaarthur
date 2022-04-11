from time import sleep
import os
import random

import constants
import scoring
import scorecard
import playing

def main():
    """
    create a list of lists for the scorecard
    set userTurn to false
    call resetScorecard

    while there are still empty items in either scorecard
        swap players
        call updateScorecard
        call displayScorecard
        if it's the user's turn
            print a message and pause briefly
            call userPlay
        else
            print a message and pause breifly
            call computerPlay
        end if
     end while
     call updateScorecard
     call displayScorecard
     determine who won and display a message

    """

    # create a list of lists for the scorecard
    uScoreCard = [0] * 16
    cScorecard = [0] * 16
    gameScorecard = [uScoreCard, cScorecard]

    # set userTurn to false
    userTurn = False

    # reset the scorecard
    scorecard.resetScorecard(gameScorecard)

    while uScoreCard.count(constants.EMPTY) > 0 or cScorecard.count(constants.EMPTY) > 0:
        # swap players
        userTurn = not userTurn

        # update and display the scorecard
        scorecard.updateScorecard(gameScorecard)
        scorecard.displayScorecards(gameScorecard)

        if userTurn:
            print("User's turn")
            sleep(2)
            playing.userPlay(uScoreCard)
        else:
            print("Computer's turn")
            sleep(2)
            playing.computerPlay(cScorecard)

    # update and display the scorecard
    scorecard.updateScorecard(gameScorecard)
    scorecard.displayScorecards(gameScorecard)

    # determine and display winner
    if gameScorecard[constants.USER][constants.TOTAL] > gameScorecard[constants.COMPUTER][constants.TOTAL]:
        print("User wins!")
    elif gameScorecard[constants.USER][constants.TOTAL] < gameScorecard[constants.COMPUTER][constants.TOTAL]:
        print("Computer wins!")
    else:
        print("It's a tie!")




# this block is the same all of the time
# when the name of the file is main, call main
if __name__ == '__main__':
    main()
