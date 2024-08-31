import pyfiglet
import time
import colorama
from colorama import Fore, Style
import webbrowser
import os

colorama.init(autoreset=True)

text = "Alone Stand Larka"
f = pyfiglet.Figlet(font='slant')

for char in f.renderText(text):
    print(Fore.RED + char + Style.RESET_ALL, end='', flush=True)
    time.sleep(0.01)

print(Fore.GREEN + "Welcome in Cyber Tricks World...")

# Open YouTube channel
print(Fore.GREEN + "Opening YouTube channel...")
webbrowser.open("http://www.youtube.com/@TeamAloneStandLarka")

# Print options with color blue
print(Fore.BLUE + "Select Attack Number:")
for i in range(1, 8):
    if i == 1:
        print(Fore.BLUE + f"{i}. Android Camera Hacking (With Link)")
    elif i == 2:
        print(Fore.BLUE + f"{i}. Gallery Hacking")
    elif i == 3:
        print(Fore.BLUE + f"{i}. SMS Hacking")
    elif i == 4:
        print(Fore.BLUE + f"{i}. WhatsApp Hacking")
    elif i == 5:
        print(Fore.BLUE + f"{i}. Location")
    elif i == 6:
        print(Fore.BLUE + f"{i}. Banner")
    elif i == 7:
        print(Fore.BLUE + f"{i}. All Social Media Hacking")

# Get user input
choice = input(Fore.GREEN + "Enter your choice: ")

# Handle user input
if choice == "1":
    print(Fore.GREEN + "Opening link...")
    webbrowser.open("https://t.me/YouCanTrackRobot")
    print(Fore.GREEN + "Camera Hacking Close")
elif choice == "2":
    print(Fore.GREEN + "Opening link...")
    webbrowser.open("https://youtu.be/fIzh24yhhoA?si=nxRzmDMiN5aCZ3wQ")
    print(Fore.GREEN + "Gallery Hacking Close")
elif choice == "3":
    print(Fore.GREEN + "Opening link...")
    webbrowser.open("https://youtu.be/fIzh24yhhoA?si=nxRzmDMiN5aCZ3wQ")
    print(Fore.GREEN + "Setup Same of Gallery and Sms Hacking So comment")
elif choice == "4":
    print(Fore.GREEN + "Opening link...")
    webbrowser.open("https://youtu.be/AXc_W2UssEI?si=IeB1oKyEsOJ9WEan")
    print(Fore.GREEN + "WhatsApp Hacking Close")
elif choice == "5":
    print(Fore.GREEN + "Opening link...")
    webbrowser.open("https://iplogger.org/")
    print(Fore.GREEN + "Location Hacking Close")
elif choice == "6":
    print(Fore.GREEN + "Opening link...")
    os.system("pkg install python -y && pip install termux-banner && banner")
    print(Fore.GREEN + "Setup Same of Gallery and Sms Hacking So comment")
elif choice == "7":
    print(Fore.GREEN + "Opening link...")
    os.system("pkg update -y && pkg install wget -y && wget -qO- https://github.com/Bhaviktutorials/shark/raw/master/setup | bash")
    print(Fore.GREEN + "Gallery Hacking Close")
else:
    print(Fore.RED + "Invalid choice. Please try again.")

# Print running commands with color green
print(Fore.GREEN + "Running commands...")
# Add your commands here
print(Fore.GREEN + "Commands executed successfully!")
