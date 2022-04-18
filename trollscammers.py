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

    url = 'https://csitem.xyz/auth/login'
    obj = {'username' : username, 'password' : password, 'code' : ''}
    headers = {'authority' : 'csitem.xyz', 'method' : 'POST', 'path' : '/auth/login', 'scheme' : 'https', 'accept' : '*/*', 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36', 'accept-encoding' : 'gzip, deflate, br', 'accept-language' : 'ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7,el-GR;q=0.6,el;q=0.5,it;q=0.4', 'content-length' : '31', 'content-type' : 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie' : '__cfduid=d26f26c2e8da5a49287e00a3600b8386c1590141842; url=csitem.xyz; style=steamcommunity.com%2Flogin; session=s%3A4jhscWHDAW8c8T5BBjJTSN0d5PJL0OC6.XN5yZS7FGqnbbdwdgvfbUh99fapU1I62qf5JOw9FRE8; timezoneOffset=10800,0; _ga=GA1.2.31338087.1590141852; _gid=GA1.2.1488509076.1590141852', 'origin' : 'https://csitem.xyz', 'referer' : 'https://csitem.xyz/openid/login?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.sreg=http%3A%2F%2Fopenid.net%2Fextensions%2Fsreg%2F1.1&openid.sreg.optional=nickname%2Cemail%2Cfullname%2Cdob%2Cgender%2Cpostcode%2Ccountry%2Clanguage%2Ctimezone&openid.ns.ax=http%3A%2F%2Fopenid.net%2Fsrv%2Fax%2F1.0&openid.ax.mode=fetch_request&openid.ax.type.fullname=http%3A%2F%2Faxschema.org%2FnamePerson&openid.ax.type.firstname=http%3A%2F%2Faxschema.org%2FnamePerson%2Ffirst&openid.ax.type.lastname=http%3A%2F%2Faxschema.org%2FnamePerson%2Flast&openid.ax.type.email=http%3A%2F%2Faxschema.org%2Fcontact%2Femail&openid.ax.required=fullname%2Cfirstname%2Clastname%2Cemail&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.return_to=https%3A%2F%2Fcsitem.xyz%2Fauth%2Fsteam%2Fmiddleware&openid.realm=https%3A%2F%2Fcsitem.xyz', 'sec-fetch-dest' : 'empty', 'sec-fetch-mode' : 'cors', 'sec-fetch-site' : 'same-origin', 'x-requested-with' : 'XMLHttpRequest'} #if needed

    r = requests.post(url, data=obj, headers=headers)

    print("POST Request made.")
    print(r.status_code, r.reason)
    print("\n")
