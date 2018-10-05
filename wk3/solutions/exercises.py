print("### EXERCISE 1 ###")
# Using a for loop, for each number 0-9, print out "3 squared is 9" etc
for n in range(10):
    print(str(n) + ' squared is ' + str(n * n))

print("### EXERCISE 3 ###")
# Using a list comprehension, get the squares of numbers from 0-9
squared_numbers = [n * n for n in range(10)]
print(squared_numbers)


print("### EXERCISE 2 ###")
# Using a list comprehension, get the even numbers from 0-9
even_numbers = [n for n in range(10) if n % 2 == 0]
print(even_numbers)


print("### EXERCISE 3 ###")
# Using a list comprehension, get the squares of even numbers from 0-9
squared_even_numbers = [n * n for n in range(10) if n % 2 == 0]
print(squared_even_numbers)


print("### EXERCISE 4 ###")
# Using a list comprehension, get all names that include an 'a'
names = ['Jared', 'Ian', 'Nigel', 'Ove', 'Nyquist', 'Tristram']
filtered_names = [name for name in names if 'a' in name]
print(filtered_names)


print("### EXERCISE 5 ###")
# Using a list comprehension, collect the upper-cased versions of all names
# that do *not* include an 'a'
names = ['Jared', 'Ian', 'Nigel', 'Ove', 'Nyquist', 'Tristram']
filtered_names = [name.upper() for name in names if 'a' not in name]
print(filtered_names)
