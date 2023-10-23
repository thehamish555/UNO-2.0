"""
Welcome version two of the Pass & Play version of UNO.

The game has no affiliation with Mattel Games, the current owners of UNO.
The game is a project I am using to help improve my python skills while
creating a fun game many of my friends know of. I own zero of the rights to
UNO and do not intend to make money off of the project as this is stealing
from Mattel Games. This project aims to be a pass & play version of the
popular online version made by Ubisoft, however once again, I am not
affiliated with Ubisoft and their work.

GitLab: https://gitlab.com/hamish555
GitHub: https://github.com/thehamish555

Thank you for supporting my project.
"""
from cards import Cards
import argument_control as ac
cards = Cards()
ac.check_arguments()

if __name__ == '__main__' and not len(vars(ac.args)) > 0:
    cards.generate_cards()
    cards.deal_cards()
    print(cards.player_cards)
