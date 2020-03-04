#!/usr/bin/env python

import os
import re
import sys
import code 
import time
import urllib
import textwrap 
import requests
import clipboard
import webbrowser
from bs4 import BeautifulSoup

if len(sys.argv) == 1 :
    print("Type query after executable (e.g. ./poi.py how to append to array in java)")
    sys.exit()

_, width = list(map(int,os.popen('stty size', 'r').read().split()))
pbar_width = width - 7
text_width = int(width * 0.85)
trunc_flag = False
urls, infos, qs, code_blocks = [], [], [], {}
sys.argv[0] = "https://www.google.com/search?q=site:https://stackoverflow.com"  
headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
s = requests.Session()
links = BeautifulSoup(s.get('+'.join(sys.argv), headers=headers_Get).text, "html.parser")

def print_pbar(i):
    j = i/5
    sys.stdout.write('\r')
    sys.stdout.write(f"[{'-' * int(pbar_width * j):{pbar_width}s}] {int(100 * j)}%")
    sys.stdout.flush()


for i, result in enumerate(links.findAll('div', attrs={'class':'r'})):
    if i == 5:
        break

    result = result.select_one("a")['href'] 
    print_pbar(i+1)
    soup = BeautifulSoup(urllib.request.urlopen(result), 'html.parser')

    try:
        ans = soup.select_one(".accepted-answer").select_one(".post-text")
    except:
        ans = soup.select_one('.answer').select_one(".post-text")

    infos.append(list(filter(lambda x: x.parent.name == "div" or x.parent.name == "pre", ans.find_all(['p','code']))))
    urls.append(result)
    qs.append(soup.select_one(".question-hyperlink").getText())

if len(infos) == 0:
    print("Sorry, no results found - exiting")
    sys.exit()

print('\n')

for i in range(len(infos)):
    output = []
    code_counter = 1

    output.append(str(i+1))
    output.append(": ") 
    output.append(qs[i])
    output.append('\n')
    output.append(("~" * (len(''.join(output))-1)))
    output.append('\n')
    
    for line in infos[i]:
        text = line.getText()
        if line.name == 'p':
            for l in textwrap.wrap(text, text_width):
                output.append('\n')
                output.append('\t')
                output.append(l)
                
            output.append('\n')

        else:
            code_blocks[((i+1)*10)+code_counter] = line.getText()
            for loc in line.getText().split('\n')[:-1]:
                if len(loc) > text_width:
                    trunc_flag = True
                    loc = loc[:text_width-3] + '...'
                output.append('\n') 
                output.append('\t')
                output.append(str(code_counter))
                output.append('\t')
                output.append(loc)

            output.append('\n')
            code_counter += 1

    print(''.join(output))

if trunc_flag:
    print(textwrap.fill("Some code blocks have been truncated. Please expand screen size or visit link to see full text", text_width))
prompt = textwrap.fill("Copy (c) and/or Visit (v)? (e.g. c32v4 to copy block 2 in option 3 and visit option 4, c21, c4, ...) ", text_width)
command = input(prompt)

if re.match('(c)[1-5]{2}(v)[1-5]|^(v)[1-5]|(c)[1-5]{2}',command):
    n = len(command)
    if n == 5:
        if command[0] == 'c':
            try:
                clipboard.copy(code_blocks[int(command[1]+command[2])])
            except:
                print("Index error - exiting")
                sys.exit()
            webbrowser.open_new_tab(urls[int(command[-1])-1])

        else:
            try:
                clipboard.copy(infos[int(command[-2]+command[-1])])
            except:
                print("Index error - exiting")
                sys.exit()

            webbrowser.open_new_tab(urls[int(command[1])-1])
        print("Copied and opening tab")

    elif n == 3:
        try:
            clipboard.copy(code_blocks[int(command[-2]+command[-1])])
        except:
            print("Index error - exiting")
            sys.exit()

        print("Copied")

    elif n == 2:
        webbrowser.open_new_tab(urls[int(command[1])-1])
        print("Opening tab")
        
    else:
        print("Error - exiting")

else:
    print("Input not recognized - exiting")
