import requests
import os
import random
import string
import json
import re
import time

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))


url = 'http://raiffiesen.blogspot.com/'
# old URL
# url = 'http://booklogic.biz/.well-known/acme-challenge/raiffeisen/lograiffeisenFull/uz1.php'


# URL 20.7.2020
#url1 = 'https://ucim.eu/mein-elba/lograiffeisenFull/uz1.php'
#url2 = 'https://ucim.eu/mein-elba/lograiffeisenFull/uz2.php'
#url3 = 'https://ucim.eu/mein-elba/lograiffeisenFull/uz3.php'
#url4 = 'https://ucim.eu/mein-elba/lograiffeisenFull/uz4.php'


# URL 21.7.2020
# They change the url when I attack them.
# To fix that I follow the scam from the beginning and use the relative url
rel_url1 = 'uz1.php'
rel_url2 = 'uz2.php'
rel_url3 = 'uz3.php'
rel_url4 = 'uz4.php'




verf_countries = {
        'Burgenland':'ELVIE-33-V', 
        'Niederösterreich':'ELVIE-32-V',
        'Steiermark':'ELVIE-38-V',
        'Vorarlberg':'ELVIE-37-V',
        'Vorarlberg':'ELVIE-37-V',
        'Kärnten':'ELOOE-03-V',
        'Vorarlberg':'ELVIE-37-V',
        'Oberösterreich':'ELOOE-01-V',
        'Salzburg':'ELOOE-05-V',
        'Tirol':'ELOOE-11-V',
        'Oberöstrreich/bankdirekt.at':'ELVIE-01-V',
        'Vorarlberg':'ELVIE-37-V',
        }

country = random.choice(list(verf_countries.keys()))
verf_nummer = verf_countries[country] + ('2V-') + ''.join(random.choice(string.digits) for i in range(6))
pin = ''.join(random.choice(string.digits) for i in range(5))
submit = 'Weiter'

#print(f'verf_nummer = {verf_nummer}, country={country}, pin={pin}')




for x in range(5000):
    form_count = random.randint(1,4)
    print(f'form_count = {form_count}')
    resp = requests.get(url)
    search_string=r'.* window.location.href = "(https://\S+)"; </script>'
    re.search(search_string, resp.text)
    match = re.search(search_string, resp.text)
    if match:
        scam_1_url = match.group(1)
        resp = requests.get(scam_1_url)
    else:
        print("no scam redirect javascript found")
        exit(1)
    print(resp.url)

    url1 = f'{resp.url}{rel_url1}'
    url2 = f'{resp.url}{rel_url2}'
    url3 = f'{resp.url}{rel_url3}'
    url4 = f'{resp.url}{rel_url4}'

    print(url1)
    print(url2)
    print(url3)
    print(url4)
    

    country = random.choice(list(verf_countries.keys()))
    verf_nummer = verf_countries[country] + ('2V-') + ''.join(random.choice(string.digits) for i in range(6))
    pin = ''.join(random.choice(string.digits) for i in range(5))
    submit = 'Weiter'
    smsTAN = ''.join(random.choice(string.digits) for i in range(4))
    submit2 = 'Senden'
    creditcardnumber = ''.join(random.choice(string.digits) for i in range(16))
    date_month = random.choice(range(1,12))
    date_year = random.choice(range(20,26))
    date_str = f'{date_month}/{date_year}'
    cvv = ''.join(random.choice(string.digits) for i in range(3))
    #Kartennummer: 1234567812345678
    #Ablaufdatum: 0699
    #CVV: 345
    #submit: Senden

    # First Form
    #time.sleep(random.randint(10,180))
    print(f"uz1: verf_nummer = {verf_nummer}, country={country}, pin={pin}")
    response = requests.post(url1, allow_redirects=False, data={
    	'verfueger': country,
    	'Verfügernummer': verf_nummer,
    	'Pin': pin,
    	'submit': submit,
    })
    print(response)
    if form_count == 1:
        continue
    
    # Second Form
    #time.sleep(random.randint(10,20))
    print(f"uz2: smsTAN = {smsTAN}")
    response = requests.post(url2, allow_redirects=False, data={
    	'smsTAN': smsTAN,
    	'submit': submit2,
    })
    print(response)
    if form_count == 2:
        continue
    

    smsTAN = ''.join(random.choice(string.digits) for i in range(4))
 
    #Third Form
    #time.sleep(random.randint(10,20))
    print(f"uz3: smsTAN = {smsTAN}")
    response = requests.post(url3, allow_redirects=False, data={
    	'smsTAN': smsTAN,
    	'submit': submit2,
    })
    print(response)
    if form_count == 3:
        continue
    
 
    # Fourth Form
    #time.sleep(random.randint(10,20))
    print(f"uz4: creditcardnumber = {creditcardnumber}, date_str = {date_str}, cvv = {cvv}")
    #Kartennummer: 1234567812345678
    #Ablaufdatum: 0699
    #CVV: 345
    #submit: Senden
    response = requests.post(url4, allow_redirects=False, data={
    	'Kartennummer': creditcardnumber,
    	'Ablaufdatum': date_str,
        'CVV': cvv,
        'submit' : 'Senden'
    })
    print(response)
    if form_count == 4:
        continue
    

