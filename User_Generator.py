import random
import time
import os

userName = os.getlogin()
numbers = '0123456789'
abc = 'abcdefghijklmnopqrstuvwxyz_.'
all = numbers + abc
passList = []
cwd = os.getcwd()
cwd = cwd + "/user.txt"

# <!---------------------------------------- >
# Pervent ValueError:
try:
  print("\n\n GITHUB @2quu  |   Discord @2qu!")
  while True:
    try:
      times = int(input('[FOR SAIFO] How Many User >> '))
      break
    except:
      print("[+] GITHUB @2quu")
  while True:
    try:
      chr = int(input('[GITHUB MRZOQis] How many Character >> '))
      break
    except:
      print("[+] Input Number Only!")
  # Passwords Generator:
  print("\n")
  for i in range(times):
    password = "".join(random.sample(all, chr))
    passList.append(password)
  print("\n")

  for i in passList:
    i = i + "\n"
    with open(cwd, 'a') as f:
      f.write(i)
  input(F"[+] Lists Saved in [user.txt].\n\nPress Enter To exit . . .")
except KeyboardInterrupt:
  print("\nScript Stopped.")
# <!---------------------------------------- >


