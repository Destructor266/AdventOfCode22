charFirstHalf = ""
charSecondHalf = ""

priority = 0
SumOfPriorities = 0

for line in open("E:/Programacion/Python/AdventOfCode/AoC3/Ruckssacks.txt", "r"):

    FirstHalfLine = line[:len(line)//2]
    SecondHalfLine = line[(len(line)//2)+1:]
    print(FirstHalfLine + " " + SecondHalfLine)

    for char1 in range(len(FirstHalfLine)):
        charFirstHalf = FirstHalfLine[char1]

        for char2 in range(len(SecondHalfLine)):
            charSecondHalf = SecondHalfLine[char2]

            if (charFirstHalf == charSecondHalf):
                priority += ord(charFirstHalf)

    SumOfPriorities += priority

print(SumOfPriorities)
