#!/usr/bin/env python3

from colorama import Fore
import os
import itertools

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
print(Fore.BLUE)
print("This script only works with firefox.")

for i in itertools.count(1,1):
    print()
    print(Fore.RED)
    search = str(input("Type Git To Search: "))
    url = os.system(f"firefox https://github.com/search?q={search}")
    print()