import time
import sys


class Player:
    def __init__(self):
        self.name = ''
        self.area = ''
        self.points = ''


def welcome():
    delay_print(Color.BOLD + "Welcome!\n" + Color.END)
    delay_print(Color.BOLD + "Begin game? Y or N\n" + Color.END)
    response = input(">")
    begin = ['y','yes','start']
    end = ['n', 'no']
    if response.lower() in begin:
        introduction()
    elif response.lower() in end:
        goodbye()
    else:
        delay_print("Sorry I did not understand your command :(\n")
        welcome()

def introduction():
    delay_print(Color.BOLD + "What is your name young muggle?" + Color.END)
    Player.name = input('\n>')
    delay_print(Color.BOLD + Player.name + " eh? There's just something magical about you...\n You seem different.." + Color.END)
    print("\n\n")
    start_game()



def start_game():
    fast_print(Player.name + ", The Floor, Hut-on-the-Rock, The Sea.\n\nHOGWARTS SCHOOL of WITCHCRAFT and WIZARDRY\n\nHeadmaster: ALBUS DUMBLEDORE (Order of Merlin, First Class, Grand Sorc., Chf. Warlock, Supreme Mugwump, International Confed. of Wizards)\n\n"
                "Dear Mr. Potter,\n\nWe are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry. \n\nPlease find enclosed a list of all necessary books and equipment.\n\n"
                "Term begins on September 1.\n\nWe await your owl by no later than July 31.\n\nYours sincerely, Minerva McGonagall, Deputy Headmistress")




def credits():
    delay_print("Thank you for playing")


def goodbye():
    delay_print("goodbye! see you again :)")


def delay_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


def fast_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.015)


class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



#Initialize game
welcome()