from colorama import Fore, Style
from requests import get, post
import os
import random
import string

class Color:
    WARNING = Fore.RED
    OK = Fore.GREEN
    DEFAULT = Style.RESET_ALL 

def color_text(text, colors):
    colored_text = ""
    color_index = 0
    for char in text:
        if char != ' ':
            colored_text += f"\033[38;2;{colors[color_index][0]};{colors[color_index][1]};{colors[color_index][2]}m{char}\033[0m"
            color_index = (color_index + 1) % len(colors)
        else:
            colored_text += char
    return colored_text

# Create a gradient of colors from orange to red
colors = [
    (255, 165, 0),  # Orange
    (255, 140, 0),
    (255, 69, 0),   # Dark Orange
    (255, 0, 0)     # Red
]

ascii_art = """
                                                                   .-'''-.                             
                                    .---.         _______         '   _    \                           
 __  __   ___         __.....__     |   |         \  ___ `'.    /   /` '.   \                 _..._    
|  |/  `.'   `.   .-''         '.   |   |          ' |--.\  \  .   |     \  '       _     _ .'     '.  
|   .-.  .-.   ' /     .-''"'-.  `. |   |     .|   | |    \  ' |   '      |  '/\    \\   //.   .-.   . 
|  |  |  |  |  |/     /________\   \|   |   .' |_  | |     |  '\    \     / / `\\  //\\ // |  '   '  | 
|  |  |  |  |  ||                  ||   | .'     | | |     |  | `.   ` ..' /    \`//  \'/  |  |   |  | 
|  |  |  |  |  |\    .-------------'|   |'--.  .-' | |     ' .'    '-...-'`      \|   |/   |  |   |  | 
|  |  |  |  |  | \    '-.____...---.|   |   |  |   | |___.' /'                    '        |  |   |  | 
|__|  |__|  |__|  `.             .' |   |   |  |  /_______.'/                              |  |   |  | 
                    `''-...... -'   '---'   |  '.'\_______|/                               |  |   |  | 
                                            |   /                                          |  |   |  | 
                                            `'-'                                           '--'   '--' 
                                                             https://github.com/sudzythegoat/Meltdown
"""

class Config:
    amount = 50
    
def parse():
    global cmd
    
    if cmd.startswith("-g"): # Get Requests spam
        url = cmd[3:]
        counter = 0
        for _ in range(Config.amount):
            check = get(url)
            counter += 1
            os.system("cls" if os.name == "nt" else "clear")
            if check.status_code == 200:
                print(f"{Color.OK}Sent Requests: {counter}{Color.DEFAULT}")
            else:
                print(f"{Color.WARNING}Sent Requests: {counter}{Color.DEFAULT}")
                
    elif cmd.startswith("-p"): # Packet spam
        url = cmd[3:]
        counter = 0
        for _ in range(Config.amount):
            os.system(f"ping {url} >/dev/null 2>&1" if os.name != "nt" else f"ping {url} >nul 2>&1")
            counter += 1
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{Color.OK}Sent Requests: {counter}{Color.DEFAULT}")
            
    elif cmd.startswith("-o"): # Post requests spam
        url = cmd[3:]
        counter = 0
        data = {
            'random_string': ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            'random_number': random.randint(0, 1000),
            'random_text': 'lorem ipsum dolor sit amet'
        }
        for _ in range(Config.amount):
            try:
                response = post(url, data=data)
                counter += 1
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{Color.OK}Sent Data: {counter}{Color.DEFAULT}")
            except requests.exceptions.RequestException:
                print(f"{Color.WARNING}Sent Data: {counter}{Color.DEFAULT}")
            
    elif cmd.startswith("-c"):  # Config stuff
        try:
            change = int(input(f"Current Amount: {Config.amount}\nNew Amount:\n[>] "))
            Config.amount = change
        except ValueError:
            print("Error: input is NaN")
    else:
        
    elif cmd.startswith("-h"): # Help
        print("Commands:")
        print(f"-g 'url' sends {Config.amount} get requests to the specified url")
        print(f"-o 'url' sends {Config.amount} post requests to the specified url")
        print(f"-p 'url' sends {Config.amount} packets to the specified url")
        print("-h displays help info")
        
    if __name__ == "__main__":
        global cmd
        print(color_text(ascii_art, colors))
        while True:
            cmd = input("[>] ")
            parse()
