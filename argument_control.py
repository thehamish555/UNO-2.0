import argparse
from cards import Cards


def check_arguments():
    if hasattr(args, 'colors'):
        if len(args.colors) != 4:
            parser.error(message=f'''
argument --colors: requires four choices (choose from {', '.join(["'"+arg+"'"
                                                       for arg in arg_list
                                                       ['colors'].choices])})
'''.strip())
        Cards().change_setting('Colors', args.colors)
    if hasattr(args, 'playerCount'):
        Cards().change_setting('PlayerCount', args.playerCount)


arg_list = {}

parser = argparse.ArgumentParser(
    prog='UNO 2',
    description='''
                Below is a list of arguments that can be used to change\n
                settings without opening the game. This also allows you to\n
                change hidden settings, just be careful with what you change
                ''',
    epilog='''This script is not affiliated with Mattel in any way''')

arg_list['colors'] = parser.add_argument(
    '--colors', type=str, nargs="*", default=argparse.SUPPRESS,
    help='Change the color of the cards',
    choices=['Red', 'Green', 'Blue', 'Yellow', 'White', 'Light Gray', 'Gray',
             'Black', 'Brown', 'Red', 'Orange', 'Lime', 'Cyan', 'Light Blue',
             'Purple', 'Magenta', 'Pink'])

arg_list['playerCount'] = parser.add_argument(
                          '--playerCount', type=int, default=argparse.SUPPRESS,
                          help='Change the player count (Number of Players)',
                          choices=range(2, 11))

args = parser.parse_args()
