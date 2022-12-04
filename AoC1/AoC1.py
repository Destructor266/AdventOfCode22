"""
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

values = []

results = []

for value in open("E:/Programacion/Python/AdventOfCode/AoC1/ElfCalories.txt", "r"):
    if(value == "\n"):
        value = " "
    value = value[:-1]
    if (not(value == '')):
        value = int(value)
    values.append(value)
#print("\nValues: ", values)

result = 0

temp = 0

for value in range(len(values)):
    if (values[value] == ''):
        temp = result
        results.append(temp)
        result = 0
    else:
        result += values[value]
#print("\nResults: ", results)


for number in range(len(results)):
    for number2 in range(len(results)-1-number):
        if (results[number2] > results[number2 + 1]):
            results[number2], results[number2 + 1] = results[number2 + 1], results[number2]
print("The Elf with most calories carries", max(results), "kcal") 

"""
In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

print("Calories of the last three Elfs %d" % sum(results[-3:]), "kcal")