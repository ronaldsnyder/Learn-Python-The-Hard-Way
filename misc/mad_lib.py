#Name:    Mad_lib.py
#Date:    1/12/2014
#Author:  Ron Snyder
#Purpose: Just a quick project taking information from the first 21 chapters of LPTHW

#get user input for the variables
person_name = raw_input("Please enter your name: ")
game_name = raw_input("Please enter a game: ")
first_verb = raw_input("Please enter a verb in the present tense (don't add ing or ed to the end): ")
first_adj = raw_input("Please enter an adjective: ")
first_noun = raw_input("Please enter a noun: ")
profession = raw_input("Please enter a profession (Pilot, Programmer, Teacher, etc:) ")
second_adj = raw_input("Please enter an adjective: ")
third_adj = raw_input("Please enter another adjective: ")
second_profession = raw_input("Please enter a profession (Pilot, Programmer, Teacher, etc: ")

#person name

#print the mad lib

mad_lib = """

I have a friend, their name is %s.  We are the 
best friends in the whole wide world.  We like to play %s 
together.  %s likes to pretend that they can %s a %s %s.

When %s grows up (s)he want to be a %s.  %s is going to be a %s 
%s .  I really don't want to be a %s.  I would rather be a %s %s. 
""" % (person_name, game_name, person_name,
       first_verb, first_adj, first_noun, person_name,
       profession, person_name, second_adj, profession,
       profession, third_adj, second_profession)

print "Here is your story!"
print mad_lib