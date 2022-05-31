# write a function to count how many times a substring appears in a string using recursion

# I can only get this to work with single characters! :(

def check(string, ch):
      if not string:
        return 0
      elif string[0] == ch:
            return 1 + check(string[1:], ch)
      else:
            return check(string[1:], ch)
string="how's she cutting Sheila?"
ch="h"
print(check(string, ch))