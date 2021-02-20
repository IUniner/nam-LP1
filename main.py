# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math
import copy


def MyFunction(x):
    return x - math.sin(1 / x)


def MyDerivative(x):
    return 1 + math.cos(1 / x) / (x * x)


def MyIteration(x0, iterations):
    i = 0
    x = float(copy.deepcopy(x0))
    while i < iterations:
        # result = x
        x = (MyFunction(x) - x) / (-1)
        i += 1
    return x


def MyNewton(x0, iterations):
    i = 0
    x = float(copy.deepcopy(x0))
    while i < iterations:
        x = x - float(MyFunction(x) / MyDerivative(x))
        i += 1
    return x


result = [MyIteration(1, 100000), MyNewton(1, 100000)]
print(result[0])
print(result[1])

print(result)
file = open("table.txt", "w")
string = "+-------------+"
for _ in range(max(len(str(result[0])), len(str(result[1])))):
    string += "-"
string += "--+\n| MyIteration | " + str(result[0])
if max(len(str(result[0])), len(str(result[1]))) == len(str(result[1])):
    for _ in range(abs(len(str(result[0])) - len(str(result[1])))):
        string += " "
string += " |\n"
string += "+-------------+"
for _ in range(max(len(str(result[0])), len(str(result[1])))):
    string += "-"
string += "--+\n| MyNewton    | " + str(result[1])
if max(len(str(result[0])), len(str(result[1]))) == len(str(result[0])):
    for _ in range(abs(len(str(result[0])) - len(str(result[1])))):
        string += " "
string += " |\n"
string += "+-------------+"
for _ in range(max(len(str(result[0])), len(str(result[1])))):
    string += "-"
string += "--+"
file.write(string)
file.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
