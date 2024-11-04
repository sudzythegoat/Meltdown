from colorama import Fore, Style

class Color:
    WARNING = Fore.RED
    OK = Fore.GREEN
    DEFAULT = Style.RESET_ALL 
    
def main():
    global c
    c = input("[>] ")

def parse():
    global c
    if c.startswith("-p"):
        p = c[5:]