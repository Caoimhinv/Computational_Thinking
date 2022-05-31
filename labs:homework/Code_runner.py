def duplicates(string):
    if not string:
        return ""
    if len(string) == 1:
        return string
    if string[0] == string[1]:
        return duplicates(string[1:])
    return string[0] + duplicates(string[1:])


print(duplicates('DDDDomiiIIIIIIiiinnnnniccXXccc'))