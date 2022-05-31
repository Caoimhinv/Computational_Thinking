def substrings(string):
    if len(string) <= 3:
        return [string]
    else:
        remainder = len(string) % 3
        end = len(string) - remainder
        beginning = string[:3]
        remaining = string[3:end]         
        return [beginning] + substrings(remaining)

        

print(substrings("We are in isolation"))
print(substrings("cinimod"))
print(substrings("Follow the process"))