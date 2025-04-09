import random
from colorama import Fore, Back, Style

n = 100
print("GAME DETAILS - \nThe computer will have a number between 1 to 100(You can change that through game difficulty option coming up).\nYou are expected to figure out the number.")
print("If you are closer the you see red color or else you see blue colored text.")
print("Choose your Game difficulty(The number till which you want to guess). DEFAULT = 100 - Press Enter if you want to play default mode")
s = input("Level Please : ")
if s != "":
    n = int(s)
my_int = random.randint(1, n)
print("If you ever want to stop in between just type 'exit'.")
print("Lets Begin.\nGuess the number")
previous = n
# print(my_int)
while True:
    y = input("Your Number please : ")
    if (y == "exit"):
        print("THANKS FOR PLAYING!")
        break
    else:
        x = int(y)
    diff = abs(x - my_int)
    if (diff == 0):
        print(Fore.CYAN + "BINGO!")
        print(Style.RESET_ALL)
        print("THANKYOU FOR PLAYING!")
        break
    elif (diff < previous):
        print(Fore.RED + "I think you are a bit closer.")
        print(Style.RESET_ALL)
    elif (diff == previous):
        print(Fore.GREEN + "Maybe you are stupid or you are smart")
        print(Style.RESET_ALL)
    elif (diff > previous):
        print(Fore.BLUE + "I think you are walking down the wrong path.")
        print(Style.RESET_ALL)
    previous = diff

