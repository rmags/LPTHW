#Creating a string embedded with a number, stored into a variablex = "There are %d types of people." % 10# Storing strings in very similar variable names binary = 'binary'do_not = "don't"# Line 10 is first time string is put inside string#Creating a string embedded with two additional strings, stored in a variable. y = "Those who know %s and those who %s." % (binary,do_not)#Prints the two formatted strings stored in easily callable variables from earlierprint xprint y# LIne 18 is second, and line 19 is the third time a string is being put inside a string# With a previously added string already in it# Creating a new string, and embedding it with previously 'formatted' strings;. print "I said: %r." % xprint " I also said: '%s'." % y# Storing a Boolean in a variable called 'hilarious'hilarious = False# Creating the first part of an embedded string w/o specifying what the string isjoke_evaluation = "Isn't that joke so funny?! %r"# prints the first half of the embedded string, plus the second half, which is inserting a # Boolean into the string.print joke_evaluation % hilarious# Creating two strings, that will be concatenated and printedw = "This is the left side of..."e = "a string with a right side."print w + e