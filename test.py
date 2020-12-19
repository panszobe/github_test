# _*_ coding: utf-8 _*_
import os,sys

with open(r'C:\Users\57884\Desktop\log4j.properties','r') as f:
    for line in f.readlines():
        print(line.strip())
