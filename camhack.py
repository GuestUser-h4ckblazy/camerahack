import random
import os
import time

def get_random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    if lines:
        return random.choice(lines).strip()
    else:
        return None

filename = 'cameras.txt'
random_line = get_random_line(filename)

os.system('clear')
print("""
      
============================
     DEATHTEAM CAMHACK
============================
    
[1] Camera Hack
      """)
user_input = input("Yinede yaz amk: ")

if user_input == "1":
    print(f"""Helal la doğru yazdın al sana lolipop
====================================
{random_line}
====================================""")
    time.sleep(10)
    os.system('clear')
    os.system("python camhack.py")
else:
    print('Lan APTAL Burda Nasıl Doğru Yazamıyon 1 Yazcan aptal')
    time.sleep(10)
    os.system('clear')
    os.system("python camhack.py")
