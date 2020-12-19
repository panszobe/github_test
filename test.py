# _*_ coding: utf-8 _*_
import os,sys
count = 0
with open(r'C:\Users\57884\Desktop\11111111.txt','r') as f:
    for line in f.readlines():
        print(line.strip())
<<<<<<< Updated upstream
=======
        print(count)
        count += 1


print("hello, world")
>>>>>>> Stashed changes
