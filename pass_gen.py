# pass generator by Laughing_fox

import secrets
import string
import getpass as gp
from datetime import datetime
import pyperclip
import colorama
import os
from colorama import init
from colorama import Fore, Back, Style
init()

os.system('cls' if os.name == 'nt' else 'clear')
# preview
print(colorama.Style.BRIGHT + colorama.Fore.RED + '=============================================')
# format time
MY_TIME = datetime.now().strftime('%Y.%m.%d %H.%M.%S')
# get username
USER_NAME = gp.getuser()
# create file for passwords
a_file = open(f'C:/Users/{USER_NAME}/Desktop/pass_list.txt', 'a')
# account name or url
site = input(colorama.Style.BRIGHT + colorama.Fore.RED + 'Please enter account name or url: ')
# account nickname
nickname = input(colorama.Style.BRIGHT + colorama.Fore.RED + 'Please enter nickname: ')
# length of account password
try:
    pass_len = int(input((colorama.Style.BRIGHT + colorama.Fore.RED +
                          'Please enter length of password: ')))
except ValueError:
    pass_len = int(0)

# usually required password symbols
additional_len = (pass_len - 4)
# list of special characters
char = secrets.choice(['!', '@', '#', '$', '%', '&', ';', ':', '+', '-', '*', '?'])
# random number
num = str(secrets.choice(range(0, 9)))
# random uppercase letter
u_letter = secrets.choice(string.ascii_uppercase)
# random lowercase letter
l_letter = secrets.choice(string.ascii_lowercase)
# generate string of first 4 characters of password
min_passwd = f'{u_letter}{l_letter}{char}{num}'
# string for full password
full_pass = str(min_passwd)
# add random symbols for required length of password
while len(full_pass) < pass_len:
    full_pass += secrets.choice([secrets.choice(string.ascii_uppercase), secrets.choice(string.ascii_lowercase),
                                 str(secrets.choice(range(0, 9))),
                                 secrets.choice(['!', '@', '#', '$', '%', '&', ';', ':', '+', '-', '*', '?'])])
# save nickname, site and password to file
print(f'Used:\n{MY_TIME}\nAccount:\n{site}\nNickname:\n{nickname}\nPassword:\n{full_pass}\n==========', file=a_file)
a_file.close()

# print password to console
print(colorama.Style.BRIGHT + colorama.Fore.GREEN + full_pass)
print(colorama.Style.BRIGHT + colorama.Fore.RED + '=============================================')
# clear clipboard
pyperclip.copy(' ')
# copy password to clipboard
clipboard_content = pyperclip.copy(full_pass)
input()
