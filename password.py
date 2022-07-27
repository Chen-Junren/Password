from xpinyin import Pinyin
from rich import print
from rich.progress import track
from rich import *
from rich.progress import *
import rich
import string
import sys
import os
import pyperclip
import time
import random


def pwd_reinforcer():
    for i in track(range(714), description='Launching Program...'):
        time.sleep(0.009)
    punc = string.punctuation
    print('''[red]
 _____                             _            _     ___                     
|  _  |___ ___ ___ _ _ _ ___ ___ _| |   ___ ___|_|___|  _|___ ___ ___ ___ ___ 
|   __| .'|_ -|_ -| | | | . |  _| . |  |  _| -_| |   |  _| . |  _|  _| -_|  _|
|__|  |__,|___|___|_____|___|_| |___|  |_| |___|_|_|_|_| |___|_| |___|___|_|                                                                
[/red]''')
    p = Pinyin()
    site=input('Enter the site for which you want to generate a password,it\'s ok of 中文 and numbers')
    if site == '':
        print("[bold red]Null value detected and about to exit[/bold red]")
        for i in track(range(12), description='Exiting...'):
            time.sleep(0.03)
        #exit(0)
        os._exit(1)
    pwd = input('Enter your basic password:')
    if pwd == '':
        print("[bold red]Null value detected and about to exit[/bold red]")
        for i in track(range(12), description='Exiting...'):
            time.sleep(0.03)
        #exit(0)
        os._exit(1)
    pwd = pwd.capitalize()
    result = p.get_pinyin(f'{site}',' ')  
    head = result[0]
    foot = result[-1]
    num = 2
    li1 = []
    tmp = ''
    li = []
    tim = [0.08,0.14,0.03,0.22,0.16]
    ran = [164,241,412,121,314,389]
    num1 = random.randint(0,10000)
    num2 = random.randint(10000,100000)
    for i in track(range(random.choice(ran)), description='Processing Password...'):
        time.sleep(random.choice(tim))
    for i in range(num):
        rand = random.randint(0,len(punc)-1)
        if rand > len(punc):
            rand = random.randint(0,len(punc)-1)
        li1.append(punc[rand])
    li.append(head)
    li.append(li1[0])
    li.append(str(num1))
    li.append(pwd)
    li.append(str(num2))
    li.append(li1[1])
    li.append(foot)
    tmp = tmp.join(li)
    print(f'[bold]Your password is：[/bold][green i]{tmp}[/green i]\nIt has been automatically copied to the [bold white]clipboard[/bold white]\n[bold red]The program will exit automatically after 20 seconds')
    pyperclip.copy(tmp)
    for i in track(range(20), description=f'{20-i}seconds left...'):
        time.sleep(1)
    #exit(0)
    print('''[red] _____                              _____ _     _     _         _ 
|  _  |___ ___ ___ ___ ___ _____   |   __|_|___|_|___| |_ ___ _| |
|   __|  _| . | . |  _| .'|     |  |   __| |   | |_ -|   | -_| . |
|__|  |_| |___|_  |_| |__,|_|_|_|  |__|  |_|_|_|_|___|_|_|___|___|
              |___|                                               [/red]''')
    os._exit(0)


def pwd_creator():
    for i in track(range(714), description='Launching Program...'):
        time.sleep(0.009)
        
    print('''[red] _____                             _                    _           
|  _  |___ ___ ___ _ _ _ ___ ___ _| |   ___ ___ ___ ___| |_ ___ ___ 
|   __| .'|_ -|_ -| | | | . |  _| . |  |  _|  _| -_| .'|  _| . |  _|
|__|  |__,|___|___|_____|___|_| |___|  |___|_| |___|__,|_| |___|_|  [/red]''')

    src_digits = string.digits             
    src_uppercase = string.ascii_uppercase
    src_lowercase = string.ascii_lowercase
    print('''[bold red]This program will create an 8-digit password that must with contain numbers, uppercase and lowercase letters[/bold red]''')
    digits_num = random.randint(1,6)
    uppercase_num = random.randint(1,8-digits_num-1)
    lowercase_num = 8 - (digits_num + uppercase_num)
    password = random.sample(src_digits,digits_num) + random.sample(src_uppercase,uppercase_num) + random.sample(src_lowercase,lowercase_num)
    
    tim = [0.08,0.14,0.03,0.22,0.16]
    ran = [164,241,412,121,314,389]
    for i in track(range(random.choice(ran)), description='Processing Password...'):
        time.sleep(random.choice(tim))
    random.shuffle(password)
    
    new_password = ''.join(password)
    print(f'[bold]Your password is：[/bold][green i]{new_password}[/green i]\nIt has been automatically copied to the [bold white]clipboard[/bold white]\n[bold red]The program will exit automatically after 20 seconds')
    pyperclip.copy(new_password)
    i=0
    for i in track(range(20), description=f'{20-i}seconds left...'):
        time.sleep(1)
    print('''[red] _____                              _____ _     _     _         _ 
|  _  |___ ___ ___ ___ ___ _____   |   __|_|___|_|___| |_ ___ _| |
|   __|  _| . | . |  _| .'|     |  |   __| |   | |_ -|   | -_| . |
|__|  |_| |___|_  |_| |__,|_|_|_|  |__|  |_|_|_|_|___|_|_|___|___|
              |___|                                               [/red]''')
    os._exit(0)
    
    
def main():
    for i in track(range(98), description='Launching BIOS...'):
        time.sleep(0.01)
    print('''[bold yellow] _____ _____ _____ _____    _____                           
| __  |     |     |   __|  |  _  |___ ___ ___ ___ ___ _____ 
| __ -|-   -|  |  |__   |  |   __|  _| . | . |  _| .'|     |
|_____|_____|_____|_____|  |__|  |_| |___|_  |_| |__,|_|_|_|
                                         |___|              [/bold yellow]''')
    time.sleep(0.4)
    print('''[bold red]Enter the program that you want to launch\n\n1.Password Creator\n2.Password Reinforcer\nElse exit\n\nYou can enter the whole name(like "Password Creator") or even the serial numbers[/bold red]''')
    chose = input('')
    if chose == 'Password Creator' or chose == '1':
        pwd_creator()
    elif chose == 'password Reinforcer' or chose == '2':
        pwd_reinforcer()
    else:
        time.sleep(0.06)
        os._exit(0)
        
        
def pwd_checker():
    pwd = input('Enter your password')
    letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter_cap = [letter[x].caplize]
    
    
if __name__ == '__main__':
    main()
