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
import re
import operator

filename=('ip_client2.csv')
fields = []
rows = []
ip = ('/home/hamsteraimbot/ip_tmp.log')
client = ('/home/hamsteraimbot/client_tmp.log')
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
# def scan():
#     with open('ip_tmp.log') as f:
#         lines=f.read().split('\n')
#         lines.remove('')
#         print lines
#         with open('client_tmp.log') as fp:
#             clients=fp.read().split('\n')
#             clients.remove('')
#
#             #for ip in lines:
#             files = os.listdir(path)
#             for name in files:
#                 commands.getoutput('cd /home/hamsteraimbot/clients/%s && touch %s.log'%(name, lines))
#
#                     # commands.getoutput('shodan host %s >> scan_ip_list.log' %ip)
# def readFileClient():
#     rd = open (client, "r")
#     # Read list of lines
#     while True:
#         # Read next line
#         out = rd.readline()
#         # If line is blank, then you struck the EOF
#         if not out :
#             break;
#         # print(out.strip())
#
#     # Close file
#     rd.close()
#     return out
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
# with open(filename, 'r') as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)
#
#     # extracting field names through first row
#     fields = csvreader.next()
#
#     # extracting each data row one by one
#     for row in csvreader:
#         rows.append(row)
#
# sys_ip=open(ip, "w")
# for row in rows:
#   sys_ip.write(row[1])
#   sys_ip.write("\n")
# sys_ip.close()
#
# sys_client=open(client, "w")
# for row in rows:
#   sys_client.write(row[0])
#   sys_client.write("\n")
# sys_client.close()

# scan()
# mkdir_client()

# clt = open(client)
# clts=clt.read().split('\n')
# clts.remove('')
# print clts
#
# ip = open(ip)
# ips=ip.read().split('\n')
# ips.remove('')
# print ips

# import pandas as pd
#
# df = pd.read_csv("ip_client.csv", usecols = ['client','ip'])
# print(df)

# data = csv.reader(open('ip_client.csv'),delimiter=',')
# sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort
# print sortedlist

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

# Define a function for
# validate an Ip addess


class GetData:

    def __init__(self, path):
        self.path = path

    def read_matrix(self):
        with open(self.path, 'r') as matrix:
            csv_reader = csv.reader(matrix, delimiter=',')
            # csv_reader.remove('')
            # fields=csv_reader.next()
            n=0
            for row in csv_reader:
                # print row
                # print ', '.join(row)
                for i, cell in enumerate(row):
                    if not len(cell)==0:
                        if not (re.search(regex, cell)):
                            # print cell
                            # commands.getoutput('shodan host {cell}'.format(**locals()))
                            # os.system('echo %s >>scan_matrix.log' %scancsv)
                        # if i==1:
                            n=n+1
                            print "cell[{i}]={cell}".format(**locals())
                            for i in enumerate(n):
                                print i
                                print n
                                os.chdir('%s/%s' %(path, cell))
                                pwd=commands.getoutput('pwd')
                                print pwd
            print n

    def read_matrix_2(self):
        with open(self.path, 'r') as matrix:
            csv_reader = csv.reader(matrix, delimiter=',')
            return [ row for row in csv_reader]


test = GetData('ip_client2.csv')
test.read_matrix()

# print "This will give you a matrix"
# matrix = test.read_matrix_2()
# print matrix
# print matrix[2][1]


# with open("ip_txt.txt", "wb") as f:
#
#     fileWriter = csv.writer(f, delimiter=',')
#     for row in sortedlist:
#         fileWriter.writerow(row)


# for client in clts:
#     for ip in ips:
#         if
