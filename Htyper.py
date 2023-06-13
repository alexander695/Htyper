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
  print(Fore.LIGHTWHITE_EX + "            V1.8    (beta)         ")

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
  print(Fore.LIGHTCYAN_EX + "\n4.Osint everything          5. Make post requests (for formularies)")
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
  
  if int =="5" or int=="post":
     print(Fore.LIGHTBLUE_EX + "looks like https://website /post <-- formulary")
     pURL = input(Fore.LIGHTWHITE_EX + "POST URL:")
     postr = requests.post(pURL)
     postr.text 
     input()
  
  else:
     print("ERROR")
     print("Restarting...")
     time.sleep(1)
     os.system("clear")
     os.system("cls")
     menu()

def seturl():
  try:
    global URL
    print(Fore.LIGHTBLUE_EX + "The url need to contain https:// or http://")
    with open("histo.txt", "r+") as his:
       histo = his.readlines()[0:2]
       historial = "".join(histo)
  
    if historial == "None":
      print(Fore.LIGHTYELLOW_EX + "No scraps maked, Passing")
      URL  = input(Fore.LIGHTRED_EX + "\nURL:")
      elimina_lineas("nhisto.txt", "histo.txt", 1)
      with open("histo.txt", "r+") as f:
         f.readlines()
       
         f.write(URL)
      menu()   
    
    print("The last page you scraped: " + historial)  
    restoress = input("\nscrap " + historial + "?: ")
  
    if restoress =="y" or restoress =="yes":
       URL = historial
       elimina_lineas("nhisto.txt", "histo.txt", 1)
       with open("histo.txt", "r+") as f:
         f.readlines()
       
         f.write(URL)
       menu() 
    URL  = input(Fore.LIGHTRED_EX + "\nURL:")

    elimina_lineas("nhisto.txt", "histo.txt", 1)
    with open("histo.txt", "r+") as f:
       f.readlines()
       
       f.write(URL)
  
    menu()
  except:
     print(Fore.LIGHTRED_EX + "Error making the requests")
     input(Fore.LIGHTYELLOW_EX + "")
     os.system("clear")
     os.system("cls")
     seturl()


  menu()

# Install requirements
def setup():
 if os.name=="nt":
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("clear")
 else:
    os.system("pip3 install requests")
    os.system("pip3 install colorama")
    os.system("cls")
 seturl()

def elimina_lineas(entrada, salida, linea_eliminar):
       with open(entrada, "rt") as arch_in:
        with open(salida, "wt") as arch_out:
            nro_linea = 1
            for linea_in in arch_in:
                if nro_linea != linea_eliminar:
                    arch_out.write(linea_in)
                nro_linea += 1

setup()