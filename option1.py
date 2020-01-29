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

def readFileIp():
    rd = open (ip, "r")
    # Read list of lines
    while True:
        # Read next line
        out = rd.readline()
        # If line is blank, then you struck the EOF
        if not out :
            break;
        # print(out.strip())
    # Close file
    rd.close()
    return out
def scan():
    with open('ip_tmp.log') as f:
        lines=f.read().split('\n')
        lines.remove('')
        print lines
        with open('client_tmp.log') as fp:
            clients=fp.read().split('\n')
            clients.remove('')

            #for ip in lines:
            files = os.listdir(path)
            for name in files:
                commands.getoutput('cd /home/hamsteraimbot/clients/%s && touch %s.log'%(name, lines))

                    # commands.getoutput('shodan host %s >> scan_ip_list.log' %ip)
def readFileClient():
    rd = open (client, "r")
    # Read list of lines
    while True:
        # Read next line
        out = rd.readline()
        # If line is blank, then you struck the EOF
        if not out :
            break;
        # print(out.strip())

    # Close file
    rd.close()
    return out
# def mkdir_client():
#     with open('client_tmp.log') as f:
#         # def identique():
#         #     lines_strip=lines.strip('\n')
#         #     content_strip=content.strip('\n')
#         #     if content_strip==lines_strip:
#         #         print "les variables sont identiques"
#         lines=f.read().split('\n')
#         if os.path.exists("clients")==True:
#             os.chdir('clients')
#             os.system("rename 'y/A-Z/a-z/' *")
#             content=commands.getoutput('ls')
#             content=content.split('\n')
#             print content
#             lines.remove('')
#             print lines
#             # identique()
#             lines_set= set(lines)
#             content_set= set(content)
#             # compare=lines_set - content_set      # vrai ligne
#             compare= content_set - lines_set
#             if content==lines:
#                 print "les variables sont identiques"
#             if compare==('set([])'):
#                 print "zrgfzrgzerg"
#             print compare
#         else:
#             commands.getoutput('mkdir clients')
#             mkdir_client()
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = csvreader.next()

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

sys_ip=open(ip, "w")
for row in rows:
  sys_ip.write(row[1])
  sys_ip.write("\n")
sys_ip.close()

sys_client=open(client, "w")
for row in rows:
  sys_client.write(row[0])
  sys_client.write("\n")
sys_client.close()
scan()
# mkdir_client()
