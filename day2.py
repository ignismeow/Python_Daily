#Problem 1
simple_message = "Hello How are you?"
print(simple_message)
simple_message = "You do like change"
print(simple_message)

#Problem 2
name = input("Please Enter your name: ").title().strip()
famous_quote = f'''\tAlbert Einstein once said, “A person who never made a mistake never tried anything new.”'''
message = f"Hello {name}, would you like to learn python today?\nDo you know once famous person said:\n{famous_quote}"
print(message)


name = input("Please Enter your name: ").title().lstrip()
famous_quote = f'''\tAlbert Einstein once said, “A person who never made a mistake never tried anything new.”'''
message = f"Hello {name}, would you like to learn python today?\nDo you know once famous person said:\n{famous_quote}"
print(message)

filename = 'python_notes.txt'
filename = filename.removesuffix('.txt')
print(filename)
