import pyfiglet
import time
import colorama
from colorama import Fore, Style
import webbrowser
import os

colorama.init(autoreset=True)

text = "Alone Stand Larka"
f = pyfiglet.Figlet(font='slant')

# Print ASCII art with color and delay
for char in f.renderText(text):
    print(Fore.RED + char + Style.RESET_ALL, end='', flush=True)
    time.sleep(0.01)

print(Fore.GREEN + "Welcome to Cyber Tricks World...")

# Open YouTube channel
print(Fore.GREEN + "Opening YouTube channel...")
webbrowser.open("http://www.youtube.com/@TeamAloneStandLarka")

# Print options with color blue
print(Fore.BLUE + "Select Attack Number:")
options = [
    "Android Camera Hacking (With Link)",
    "Gallery Hacking",
    "SMS Hacking",
    "WhatsApp Hacking",
    "Location",
    "Banner",
    "All Social Media Hacking",
    "3 Tools",
    "Basics Download",
    "All Social Media Hacking"
]

for i, option in enumerate(options, 1):
    print(Fore.BLUE + f"{i}. {option}")

# Get user input
choice = input(Fore.GREEN + "Enter your choice: ")

# Handle user input
links = {
    "1": "https://t.me/YouCanTrackRobot",
    "2": "https://youtu.be/fIzh24yhhoA?si=nxRzmDMiN5aCZ3wQ",
    "3": "https://youtu.be/fIzh24yhhoA?si=nxRzmDMiN5aCZ3wQ",
    "4": "https://youtu.be/AXc_W2UssEI?si=IeB1oKyEsOJ9WEan",
    "5": "https://iplogger.org/",
}

commands = {
    "6": "pkg install python -y && pip install termux-banner && banner",
    "7": "pkg update -y && pkg install wget -y && wget -qO- https://github.com/Bhaviktutorials/shark/raw/master/setup | bash",
    "8": "apt update && apt upgrade && git clone https://github.com/AloneStandLarkaAnas/3-Tools.git && cd 3-Tools && python3 Tools.py",
    "9": "apt update && git clone https://github.com/AloneStandLarkaAnas/Basics.git && cd Basics && python3 Basics.py",
    "10": "apt update && git clone https://github.com/AloneStandLarkaAnas/Basics.git && cd Basics && python3 Basics.py",
}

if choice in links:
    print(Fore.GREEN + "Opening link...")
    webbrowser.open(links[choice])
    print(Fore.GREEN + f"{options[int(choice) - 1]} Close")
elif choice in commands:
    print(Fore.GREEN + "Executing command...")
    os.system(commands[choice])
    print(Fore.GREEN + f"{options[int(choice) - 1]} Close")
else:
    print(Fore.RED + "Invalid choice. Please try again.")
