# Social Media Finder using Username
# Coded by Fathan
# 06 May 2019

import requests
from colorama import Fore, Back, Style

username = input("Input username: ")

sites = ['https://www.facebook.com/',
        'https://www.instagram.com/',
        'https://wwww.ask.fm/',
        'https://www.twitter.com/',
        'https://www.pinterest.com/']

for i in sites:
    r = requests.get(i+"{}".format(username))
    if r.status_code == 200:
        print(i+"{} --> ".format(username) + Fore.GREEN + "found!"+ Style.RESET_ALL)
    else:
        print(i+"{} --> ".format(username) + Fore.RED + "not found!"+ Style.RESET_ALL)