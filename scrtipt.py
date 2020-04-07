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
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = csvreader.next()

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
originalsys=sys.stdout
sys.stdout=open(ip, "w")
for row in rows:
#     # parsing each column of a row
    print(row[1])
sys.stdout.close()
sys.stdout=originalsys
catip=commands.getoutput('cat ip_tmp.log')
print(catip)
