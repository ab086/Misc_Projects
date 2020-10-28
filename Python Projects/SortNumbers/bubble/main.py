import random

print("How many numbers do you want to sort?")

try:
    int_input = int(input())
    fillArray(int_input)

except Exception as ex:
    print("Error: {}".format(type(ex).__name__))
    print("Only numbers are allowed.")

def fillArray(int_input):
    i = 0
    array_number = []

    while(i < int_input):
        array_number[i] = returnRandom()
        i += 1


def returnRandom():
    return random.randint(0,999)