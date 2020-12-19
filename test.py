# _*_ coding: utf-8 _*_
import os,sys

with open(r'C:\Users\57884\Desktop\广州芯泰通信技术有限公司加班管理办法.docx','r') as f:
    for line in f.readlines():
        print(line.strip())
