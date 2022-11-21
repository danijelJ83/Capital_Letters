'''
Write a function named capital_indexes.
The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in the string that have capital letters.
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''

upper_indexes = []
upper_letters = []


def capital_indexes(check_string):
    for count, item in enumerate(check_string):
        if item.isupper():
            upper_indexes.append(count)
            upper_letters.append(item)
    return


check_string = input('Give me a string with upper and lower cases: ')
capital_indexes(check_string)
print('')
print(check_string)
print(upper_indexes)
print(upper_letters)

