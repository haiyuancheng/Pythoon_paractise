#!/usr/bin/python 
#-*- coding: UTF-8  -*- 

#This script is used by binary search algorithm

def binary_search(number):
#numbers_list = range(20, 200)
numbers_list = range(20, 200)
i = 0
j = len(numbers_list)
while i < j:
	middle = int((i +j) / 2)
   	if number > numbers_list[middle]:
		i = middle + 1
	else:
		j = middle
return 'the index is ' + str(i) 


#binary_search(100)
