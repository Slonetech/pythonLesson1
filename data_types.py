# string data types

# literal assignment
first = 'Gordon'
last = 'Freeman'

# print(type(first))
# print(type(last) == str)
# print(isinstance(first,str))


# #constructor function

# pizza = str('Pepperoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza,str))


# #string concatenation 

# full_name = first + ' ' + last
# print(full_name)    

# full_name += "!"
# print(full_name)

# #casting a number to a string

# decade = str(2001)
# print(type(decade))
# print(decade)

# statement = " The start of " + decade + " brought the release of the first Harry Potter movie."
# print(statement)

multiline ='''
hey how are you?

i was just checking in 

             all good
'''
print(multiline)

#escaping special characters

sentence = 'I\'m back at work ! \t Hey ! \n\n where\'s this at \\ located ?'
print (sentence)