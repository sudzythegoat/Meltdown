from colorama import Fore, Style
from requests import get
import os
class Color:
    WARNING = Fore.RED
    OK = Fore.GREEN
    DEFAULT = Style.RESET_ALL 
    
def main():
    global cmd
    cmd = input("[>] ")
    
def parse():
    global cmd
    if cmd.startswith("-g"):
        url = cmd[3:]
        counter = 0
        for _ in range(config.amount):
            check = get(url)
            counter += 1
            os.system("clear")
            if check.statuscode == "200":
                print(f"{Color.OK}Sent Requests: {counter}{Color.DEFAULT}")
            else:
                print(f"{Color.WARNING}Sent Requests: {counter}{Color.DEFAULT}")
    elif cmd.startswith("-p"):
        url = cmd[3:]
        counter = 0
        for _ in range(config.amount):
            os.system(f"ping {url}")
            print(f"{Color.OK}Sent Requests: {counter}{Color.DEFAULT}")
