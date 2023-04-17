## -*- coding: utf-8 -*-
import os
import time
import requests
from colorama import Fore
    
    
def menu():
  Domain = requests.get(URL)

  print(Fore.LIGHTYELLOW_EX + """ _   _ _____
| | | |_   _|   _ _ __   ___ _ __
| |_| | | || | | | '_ \ / _ \ '__|
|  _  | | || |_| | |_) |  __/ |
|_| |_| |_| \__, | .__/ \___|_|
          |___/|_|
  """)
  print(Fore.LIGHTWHITE_EX + "            V1.5    (beta)         ")

  if Domain:
       print("Status:")
       print(Domain.status_code)
       print(Fore.LIGHTGREEN_EX + "Conection acepted")
  else:
       print("Status:")
       print(Domain.status_code)
       print(Fore.LIGHTRED_EX + "Conection refused")

  print(Fore.LIGHTWHITE_EX + "\nSeeing:" + URL)
  print(Fore.LIGHTBLACK_EX + "Do you want to...?")
  print(Fore.LIGHTCYAN_EX + "1.See request cookies           2.See headers          3.See html code")
  print(Fore.LIGHTCYAN_EX + "\n4.Osint everything")
  int = input(Fore.LIGHTWHITE_EX + "\n>>")

  if int=="1" or int=="cookies":
      print(Domain.cookies)
      input("\nPress to back")
      os.system("clear")
      os.system("cls")
      menu()

  if int=="2" or int=="headers":
      print(Domain.headers)
      input("\nPress to back")
      os.system("clear")
      os.system("cls")
      menu()
    
  if int=="3" or int=="html code":
      print(Domain.text)
      input("\nPress to back")
      os.system("clear")
      os.system("cls")
      menu()
  
  if int=="4" or int=="osint":
      print(Fore.LIGHTBLUE_EX + "saving source code in source.txt\n")
      sourcecode = Domain.text
      f = open("source.txt", "w")
      f.write(URL + ":\n")
      f.write(sourcecode)
      f.close()
      print(Fore.LIGHTGREEN_EX + "\nCookies injected:")
      print(Domain.cookies)
      print(Fore.LIGHTWHITE_EX + "\nHeaders:")
      print(Domain.headers)

      input("\nPress enter to back")
      os.system("clear")
      os.system("cls")
      menu()
  
  else:
     print("ERROR")
     print("Restarting...")
     time.sleep(1)
     os.system("clear")
     os.system("cls")
     menu()

def seturl():
  global URL
  print(Fore.LIGHTBLUE_EX + "The url need to contain https:// or http://")
  URL  = input(Fore.LIGHTRED_EX + "\nURL:")
  if (len(URL) <= 13):
     print("Invalid url")
     time.sleep(3)
     os.system("clear")
     os.system("cls")

  menu()

# Install requirements
def setup():
 os.system("pip install requests")
 os.system("pip install colorama")
 os.system("clear")
 os.system("cls")
 seturl()

setup()