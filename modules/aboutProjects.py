#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# title: aboutProjects
# file: aboutProjects.py
# description: returns information about the varoius projects
# language: python
# 
# authors: Cameron Jeffries (camservo@gmail.com)
# date: 10.7.12
# version: 1.0.0
# notes: .
#
# keywords: about, elephant
#
# # # # # # # # # # # # # # # # # # # # # #
import sys
import os
import csv

progName = sys.argv[0]
phoneNum = sys.argv[1]
srcLat = sys.argv[2]
srcLon = sys.argv[3]
argList = sys.argv[4:]
argCount = len(argList)
messageList=[]
messageStr=''


for i in range(argCount):
    messageList.append(argList[i])

for item in messageList:
    messageStr += str(item) + ' '

messageStr=messageStr[:-1]


key = messageStr
dataPath = "%s/data/aboutProjects" % (os.getcwd())
data = open(dataPath, 'r')
ret=''


dataDict={}

with open(dataPath, 'r') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        try:
            if str(row[0]).lower() == key.lower() or row[1].lower() == key.lower():                
                ret = row[2]
        except IndexError:
            continue

if ret == '':
    print 'Project does not exist.  Please see project list and enter by ID or by name as printed.'
else:
    print ret