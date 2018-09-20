print(5)


print(2.3)


print('Hello')


print(True)


print(False)


print(1 + 2)


print((1 + 2) * 4)


print(7 / 5)


print(7 // 5)


print(7 % 5)


print('Ove' + 'Arup')


print(True and False)


print(True or False)


print(True and True)


print(7 == 5)


print(7 > 5)


print(7 == 7)


print(1 + 2 == 3)


print(0.1 + 0.2)


print(0.1 + 0.2 == 0.3)


a = 3
print(a)


b = 4
print(b / 5)


x = 6
y = 3 + 4
print(x * y)


a = 5
print(a)
a = 7
print(a)


values = [3, 1, 2]
print(values[0])
print(values[1])
print(values[2])


values = [3, 1, 2]
values[2] = 4
print(values)


actions = {'red': 'stop', 'green': 'go'}
print(actions['red'])


actions = {'red': 'stop', 'green': 'go'}
actions['yellow'] = 'proceed with caution'
print(actions['yellow'])


actions = {'red': 'stop', 'green': 'go', 'yellow': 'proceed with caution'}
actions['yellow'] = 'STOMP ON IT'
print(actions['yellow'])


a = 3
if a > 4:
    print('Bigger')
else:
    print('Not bigger')


a = 5
if a < 0:
    print('Negative')
elif a < 3:
    print('Small')
elif a < 10:
    print('Not too big')
else:
    print('YOOGE')


for x in [3, 1, 2]:
    print(x)


# Perhaps not what you think!
for i in range(5):
    print(i)


for i in range(10):
    if i % 3 == 0:
        print(i)


num = 10
while num > 0:
    print(num)
    num = num - 2


num = 10
while num > 0:
    num = num - 2
    print(num)


n = len('Nyquist')
print(n)


values = [10, 20, 30]
n = len(values)
print(n)


print(len([]))


print(len(''))


print(abs(-12))


print('arup'.upper())


print('Ove Arup'.split())


street_name = 'Water'
print(street_name.startswith('Wat'))
print(street_name.startswith('w'))


values = [2, 1, 3]
values.append(4)
print(values)


values = [2, 1, 3]
values.sort()
print(values)


values = []
i = 2
while i < 6:
    values.append(i)
    i = i + 1
print(values)


import math
print(math.pi)
print(math.sqrt(16))
print(math.cos(math.pi))


def say_hello_to(name):
    print('Hello, ' + name + '!');

say_hello_to('Jared')
say_hello_to('Ian')


def greeting(name):
    return 'Hi ' + name + '!'

text = greeting('Nigel')
print(text)


def bigger(x, y):
    if x > y:
        return x
    else:
        return y

print(bigger(8, 9))
print(bigger(3, -4))


# Little bit tricky!
a = 'Python'
b = a
print(b)
a = 'JavaScript'
print(b)


a = [1, 2, 3]
b = a
print(b)
a = [10, 20, 30]
print(b)


# More tricky!
a = [1, 2, 3]
b = a
print(b)
a.append(4)
print(b)
b.append(5)
print(a)


file = open('input.txt')
for line in file:
    print(line)
file.close()


file = open('input.txt')
for line in file:
    print(line.strip())
file.close()



file = open('input.txt')
lines = file.readlines()
print(lines)
file.close()


file = open('input.txt')
lines = file.read().splitlines()
print(lines)
file.close()
