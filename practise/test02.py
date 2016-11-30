#!/usr/bin/python 
#-*- coding: UTF-8 -*-

def binary_search(number):
	numbers_list=range(20, 100)
	i = 0
	j = len(numbers_list)
	#print j
	while i < j:
    		middle = int((i + j) / 2)
		#print numbers_list[middle]
    		if number > numbers_list[middle]:
        		i = middle + 1
		else:
       			j = middle
		print i, j
	print 'the index is ' + str(i) + '\n' + 'the value is ' + str(j) + '\n'
	return 'the index is '+ str(i)
	return 

binary_search(100)
