#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################
#                        #
#Emre Yılmaz (delosemre) #
#                        #
##########################

import sys
import argparse
import os
import time
import httplib
import subprocess
import re, urllib2
import socket
import urllib,sys,json
import telnetlib
import glob
import random
import Queue 
import threading
import base64
from getpass import getpass
from commands import *
from sys import argv
from platform import system
from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep

print ( """\033[1;91m
 _  __                    _ ____  _             
| |/ /___ _ __ _ __   ___| | __ )| | ___   __ _ 
| ' // _ \ '__| '_ \ / _ \ |  _ \| |/ _ \ / _` |
| . \  __/ |  | | | |  __/ | |_) | | (_) | (_| |
|_|\_\___|_|  |_| |_|\___|_|____/|_|\___/ \__, |
                                          |___/ .org\033[1;m
\033[1;93mKernelBlog | delosemre\033[1;m 

     \033[1;91m
     KernelBlog.org
     En.kernelblog.org
     ---
     KernelBlog devepoler team
     Kernelblog geliştirici ekibi\033[1;m
      """)


print("   \033[1;91mBirkaç Düzenleme Yapıyoruz...\033[1;m")
print("   \033[1;91mRepo Ekleniyor...\033[1;m")
time.sleep(1)
os.system("apt-get clean")
os.system("touch /etc/apt/sources.list.d/delosemre.list")
repo = open('/etc/apt/sources.list.d/delosemre.list','r+')
repo.write('##delosemre-siber güvenlik aracı için repo \ndeb http://deb.parrotsec.org/parrot stable main contrib non-free \n#deb-src http://deb.parrotsec.org/parrot stable main contrib non-free')
print(" ")
os.system("apt-get clean")
print("   \033[1;91mrepo Güncelleniyor...\033[1;m")
print(" ")
time.sleep(1)
os.system("apt-get update")
repo.close()
print("   \033[1;91mRepo Eklendi.\033[1;m")
print("	\033[1;91mGerekli Yazılımlar yükleniyor....\033[1;m")
time.sleep(1)
os.system("apt-get install git")

print("\033[1;91mUyarı: BİLGİSAYARINIZIN SAĞLAM KALMASI AÇISINDAN LÜTFEN UPGRADE ÇEKMEYİNİZ.\033[1;m")
print("\033[1;91mİşlem bitti artık kali linux reposuna sahipsiniz...\033[1;m")
