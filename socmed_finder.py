# Social Media Finder using Username
# Coded by fathan0x1
# 06 May 2019

import requests
from colorama import Fore, Back, Style

print(""" __                               _   ___ _           _           
/ _\ ___   ___ _ __ ___   ___  __| | / __(_)_ __   __| | ___ _ __ 
\ \ / _ \ / __| '_ ` _ \ / _ \/ _` |/ _\ | | '_ \ / _` |/ _ | '__|
_\ | (_) | (__| | | | | |  __| (_| / /   | | | | | (_| |  __| |   
\__/\___/ \___|_| |_| |_|\___|\__,_\/    |_|_| |_|\__,_|\___|_|
                                         v1.1 - Author: @fathan0x1                                                              
""")

username = input("[?] Input Username: ")
print("[*] Finding",Style.BRIGHT+Fore.YELLOW+username+Style.RESET_ALL+"'s socmed ...\n")

def main(username):
    sites = ['https://www.facebook.com/',
            'https://www.instagram.com/',
            'https://wwww.ask.fm/',
            'https://www.twitter.com/',
            'https://www.pinterest.com/',
            'https://www.flickr.com/']

    for i in sites:
        r = requests.get(i+"{}".format(username))
        if r.status_code == 200:
            print("[+] "+i+"{} --> ".format(username) + Fore.GREEN + "Found!"+ Style.RESET_ALL)
        else:
            print("[+] "+i+"{} --> ".format(username) + Fore.RED + "Not Found!"+ Style.RESET_ALL)

main(username)
