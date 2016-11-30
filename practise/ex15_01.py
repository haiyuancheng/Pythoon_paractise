#!/usr/bin/python
#-*- coding: UTF-8 -*- 
#Reding files

#from sys import argv
#script, filename = argv

txt = open("ex15_sample.txt", "r")
#print "Here's your file %r:" % filename
print txt.read()


#print "Type the filename again:"
file_again = raw_input('> ')

txt_again = open(file_again, "r")

print txt_again.read()
#print txt_again

txt.close()
txt_again.close()

