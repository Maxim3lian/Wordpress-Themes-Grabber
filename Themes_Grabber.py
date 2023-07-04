#!/usr/bin/env python2
# Author: Maxim3lian

import sys, os, re, socket, requests, random
from re import findall as reg
os.system('cls')
print('''
  __  __            _           ____  _ _ _             
 |  \/  |          (_)         |___ \(_) (_)            
 | \  / | __ ___  ___ _ __ ___   __) |_| |_  __ _ _ __  
 | |\/| |/ _` \ \/ / | '_ ` _ \ |__ <| | | |/ _` | '_ \ 
 | |  | | (_| |>  <| | | | | | |___) | | | | (_| | | | |
 |_|  |_|\__,_/_/\_\_|_| |_| |_|____/|_|_|_|\__,_|_| |_|
                                                        t.me/Maxim3lian

[>] WEBSITES GRABBER BY WORDPRESS THEMES <FREE>''')

def open_link(url):
    url = url.replace(' ', r'\ ')
    if os.name == 'nt':
        command = 'start {0}'.format(url)
    elif os.name == 'posix':
        command = 'xdg-open {0}'.format(url)
    else:
        raise OSError('Unsupported operating system: {0}'.format(os.name))
    os.system(command)
urlx = 'https://t.me/Maxim3lian_Channel'
open_link(urlx)
themename = raw_input('\n\t[>] Theme Name: ')
themepages = raw_input('\n\t[>] N.O.P: ')
maxi1 = '\n\t\t[!] Contact : t.me/Maxim3lian_Channel [!]'
for page in range(1, int(themepages)):
	state = ['us1', 'us2', 'us3', 'us4', 'us5', 'us6', 'us7', 'us8', 'us9', 'us10', 'us11', 'us12', 'us13', 'us14', 'us15', 'eu1', 'eu2', 'eu3', 'eu4', 'eu5', 'eu6', 'eu7', 'eu8', 'eu9', 'eu10']
	proxy = random.choice(state)
	ua = {'Origin': 'https://' + proxy + '.proxysite.com', 
	'Upgrade-Insecure-Requests': '1',
	'Referer': 'https://' + proxy + '.proxysite.com/process.php?d=d5ww0usE5q1XyjorWQH7sw%3D%3D&b=1&f=norefer',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Content-Type': 'application/x-www-form-urlencoded',
	'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
	'Cookies': '_ga=GA1.2.589987225.1610038351; __gads=ID=bffe8a3c85dbe9de-228786b28fc5007f:T=1610038351:RT=1610038351:S=ALNI_Mbo8XuMGTbG0cfECZhdrpKMLkcBLA; _gid=GA1.2.1432847235.1623704158; c[themetix.com][/][IDE]=AHWqTUl0Im-eLYq4upcs9o_5nQC64Q4uAjr0LgWExpANROqkTn8bXVdImvD2PNcP'
	}
	data = {'allowCookies': 'on',
	'd': 'https://themetix.com/' +themename+'/'+str(page)}
	test = requests.post('https://' + proxy + '.proxysite.com/includes/process.php?action=update', data=data, headers=ua, timeout=10)
	if 'site' in test.content:
		print(maxi1) 
		domen = reg('<p style="margin-bottom: 20px">(.*?)</p>', test.content)
		for webs in domen:
			print('\n\t\t[+] Grabbed : '+str(webs))
			open('Grabbed.txt','a').write('http://'+webs+'\n')