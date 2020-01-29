#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shodan
import time
import os
import subprocess
import shutil
import datetime
import sys
import csv
import commands

filename=('ip_client.csv')
fields = []
rows = []
ip = ('ip_tmp.log')
client = ('client_tmp.log')
scan_ip_list = ("scan_ip_list.log")
path = ("/home/hamsteraimbot/clients")


files = os.listdir(path)
i=0
for name in files:
    print(name)
    commands.getoutput('cd /home/hamsteraimbot/clients/%s && touch fichier_ip.log'%name)
    # commands.getoutput('touch fichier_ip.log')
    i=i+1
print i
