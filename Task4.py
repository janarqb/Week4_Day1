my_str = 'Civic'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("True")
else:
   print("False")