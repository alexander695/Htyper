import os
import sys
import time
import requests
from colorama import Fore

print(Fore.LIGHTBLUE_EX + "The url need to contain https:// o http://")

URL  = input(Fore.LIGHTRED_EX + "\nURL:")


if (len(URL) <= 13):
    print("Invalid url")
    time.sleep(3)
    os.system("clear")
    
    
def menu():
  Domain = requests.get(URL)

  print(Fore.LIGHTYELLOW_EX + """ _   _ _____
| | | |_   _|   _ _ __   ___ _ __
| |_| | | || | | | '_ \ / _ \ '__|
|  _  | | || |_| | |_) |  __/ |
|_| |_| |_| \__, | .__/ \___|_|
          |___/|_|
  """)
  print(Fore.LIGHTWHITE_EX + "            V1              ")


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
  int = input(Fore.LIGHTBLUE_EX + "\n>>")

  if int=="1":
      print(Domain.cookies)
      input("\nPress to back")
      os.system("clear")
      menu()

  if int=="2":
      print(Domain.headers)
      input("\nPress to back")
      os.system("clear")
      menu()
    
  if int=="3":
      print(Domain.text)
      input("\nPress to back")
      os.system("clear")
      menu()
    
    
try:
      menu()
except Exception as e:
    print(menu)
    pass

else:
    print("ERROR")
    print("Restarting...")
    time.sleep(1)
    os.system("clear")
    pass  