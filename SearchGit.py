#!/usr/bin/env python3

from colorama import Fore
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

print(Fore.CYAN)
print("""
╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╭━━━╮╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱┃╭━╮┣╯╰╮
┃╰━━┳━━┳━━┳━┳━━┫╰━╮╱╱┃┃╱╰╋╮╭╯
╰━━╮┃┃━┫╭╮┃╭┫╭━┫╭╮┣━━┫┃╭━╋┫┃
┃╰━╯┃┃━┫╭╮┃┃┃╰━┫┃┃┣━━┫╰┻━┃┃╰╮
╰━━━┻━━┻╯╰┻╯╰━━┻╯╰╯╱╱╰━━━┻┻━╯""")
print("Search any Git-Repo from your LINUX terminal.")
print()
print("""If you type more then one word, add a '+' in between.
Example: 'Windows+hacking' = 'windows hacking'. """)
print()

def menu():
    print(Fore.RED)
    search = str(input("Type Git To Search: "))
    url = urlopen(f'https://github.com/search?q={search}')
    print()
    soup = BeautifulSoup(url.read(), 'lxml')
    links = []

    for link in soup.find_all('a', class_="v-align-middle"):

        links.append(link.get('href'))

    print("List of top ten Repos:")
    print()
    print(*links, sep = '\n')
    print()
    print(Fore.CYAN)
    print("Options:\n\nExplore a 'Git README' press [1].\nLoad a 'Git' press [2].\nSearch again? Press [3].\n\nPress [4] to exit.")
    print()
    choice = input()

    if choice == '1':
        print()
        print(Fore.RED)
        add = str(input("Add repo here: "))
        url1 = urlopen(f"https://raw.githubusercontent.com/{add}/master/README.md")
        soup = BeautifulSoup(url1.read(), 'lxml')
        link = soup.find_all('p')
        print(link)
        print()
        print(Fore.CYAN)
        
        def menu1():
            print("Options:\n\nGit clone the repo press [1].\nNew search press [2].")
            print()
            choice2 = input()

            if choice2 == '1':
                print(Fore.RED)
                clone1 = os.system(f'git clone https://github.com{add}.git')
                exit()
            
            if choice2 == '2':
                menu()

        menu1()

    if choice == '2':
        clone = os.system(f'git clone https://github.com{add}.git')
        exit()

    if choice == '3':
        menu()

    if choice == '4':
        exit()
menu()
