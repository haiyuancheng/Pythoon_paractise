#!/usr/bin/python
#-*- coding: UTF-8 -*-
#Prompting and Passing

from sys import argv

script, user_name, gender, job = argv
#promt = '>'
promt = '#'

print "Hi %s, I'm the %s script, My gender is %s and My job is %s " % (user_name, script, gender, job)
print "I'd like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(promt)

print "Where do you live %s?" % user_name
lives = raw_input(promt)

print "What kind of computer do you have?"
computer = raw_input(promt)

print "How old are you?"
age = raw_input(promt)

print "What kind of girl do you like?"
form = raw_input(promt)



print """
Alright, so you said %r about like me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice,I heard
your are %r, like %r girl, right?
""" % (likes, lives, computer, age, form)


