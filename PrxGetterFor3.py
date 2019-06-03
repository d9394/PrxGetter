# -*- coding: utf-8 -*-
import requests as r
import re
from bs4 import BeautifulSoup
from random import randint
import urllib.request, urllib.error, urllib.parse
import socket

def putfile(filename, content):
    file_ = open(filename, 'a')
    file_.write(content)
    file_.close()

print("""
   ___          _____    __  __            
  / _ \_____ __/ ______ / /_/ /____ ____   
 / ___/ __\ \ / (_ / -_/ __/ __/ -_/ __/   
/_/  /_/ /_\_\\___/\__/\__/\__/\__/_/      
                                           
""")

url = "http://www.httptunnel.ge/ProxyListForFree.aspx"
rx  = r.get(url)
data = rx.text
features="html.parser"
soup = BeautifulSoup(data,features)
goodprxs = []
for link in soup.find_all('a'):
    a = link.get('href')
    if "ProxyChecker" in a:
        b = a.split("?p=")
        if len(b) > 1:
            goodprxs.append(b[1])

def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://www.google.com')
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as detail:
        return True
    return False

outname = "output"+str(randint(1,199999))+".txt"

def main():
    socket.setdefaulttimeout(1)
    proxyList = goodprxs
    for currentProxy in proxyList:
        if is_bad_proxy(currentProxy) == False:
            dab = "LIVE / %s" % (currentProxy)+"\n"
            putfile(outname,dab)

if __name__ == '__main__':
    main()

print("Output saved on "+outname)
