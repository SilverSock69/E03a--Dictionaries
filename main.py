
birthdays = {
    'Barack Obama' : '8/4/1961',
    'Kim Jong Un' : '1/8/1984',
    'Jason Francis' : '9/16/2000 ;)',
    'Travis Scott' : '4/30/1991'
}

print('Hello! Welcome to the best 4-person birthday dictionary in the world')
print('We know the birthdays of:')
for name in birthdays:
    print(name)
print("Who's birthday do you want to know?")
name = input()
if name in birthdays:
    print('{}\'s birthday is {}.'.format(name, birthdays [name]))
