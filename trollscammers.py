import requests
import random
import string
import os

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

with open("1names.txt") as f:
    numedefamilie = f.readlines()

numedefamilie = [x.strip() for x in numedefamilie]

with open("lnames.txt") as f:
    prenume = f.readlines()

prenume = [x.strip() for x in prenume]

while True:


    numef_n = random.choice(numedefamilie)
    prenume_n = random.choice(prenume)

    username = numef_n + prenume_n
    username = username.lower()

    password = randomString()

    url = 'https://casesun.xyz/auth/login'
    obj = {'username' : username, 'password' : password}

    r = requests.post(url, data=obj)

    print("POST Request made.")
    print(r.status_code, r.reason)
    print("\n")