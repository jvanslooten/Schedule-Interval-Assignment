"""

Title: Algorithm Analysis Individual Project 1
Author: Jack VanSlooten
Date: 12 September 2021

"""

# Ask user which algorithm to run
algorithmChoice = input("Enter 1 to run standard interval algorithm, enter 2 to run weighted interval algorithm: ")

# Check input
while algorithmChoice != "1" and algorithmChoice != "2":
    print("Invalid input, please try again.")
    algorithmChoice = input("Enter 1 to run standard interval algorithm, enter 2 to run weighted interval algorithm: ")

"""
* Standard Interval Schedule *
This solution uses an input file containing a single list of integers. 
I am basing the algorithm on the assumption that any given integer in the file stands for the time length of a specific 
interval.
The user input represents the total amount of time that the intervals must fit into.
My algorithm chooses the shortest time interval first
"""

if algorithmChoice == "1":
    # Open file
    with open("/Users/jvanslooten/Desktop/AlgorithmAnalysis/IndividualProject1/Standard.txt", "rt") as standardIntervalFile:
        # Convert input file into an array
        standardStringArray = standardIntervalFile.read().splitlines()

    # Get user input and display it
    resourceNumber = input("Standard interval input collected, please enter the amount of time available: ")
    print("Resources available: " + resourceNumber + "\nRunning standard interval algorithm...")
    resourceNumber = int(resourceNumber)

    # Remove quotations from array
    standardIntegerArray = []
    for item in standardStringArray:
        standardIntegerArray.append(int(item))

    # Sort array
    standardIntegerArray.sort()

    # Initialize variables
    standardScheduleTotal = 0
    finalStandardSchedule = []
    i = 0
    # Use while loop to print as many smallest interval values as possible
    # That add up to less than the user specified constraint
    while standardScheduleTotal < resourceNumber:
        finalStandardSchedule.append(standardIntegerArray[i])
        standardScheduleTotal += standardIntegerArray[i]
        i += 1

    print("These are the time lengths of the intervals, in the order that they should be picked.")
    print("(Least time taken to greatest)")
    print(finalStandardSchedule)

"""
* Weighted Interval Schedule *
This solution uses an input file containing two lists of integers.
I am basing the algorithm on the assumption that any given integer in the first line stands for the time length of a 
specific interval.
The second line of integers refers to the weight of each interval in the first line.
The user input represents the total amount of time that the intervals must fit into.
My algorithm chooses the shortest time interval first, taking weights into account.
"""
if algorithmChoice == "2":
    import csv

    # Open file
    with open("/Users/jvanslooten/Desktop/AlgorithmAnalysis/IndividualProject1/Weighted.csv", "rt") as weightedIntervalFile:
        csv_reader = csv.reader(weightedIntervalFile)
        # Convert input file into two arrays
        for line_no, line in enumerate(csv_reader, 1):
            if line_no == 1:
                weightedStringArray = line
            else:
                arrayWeightsStringLine = line

    # Get user input and display it
    resourceNumber = input("Weighted interval input collected, please enter the amount of time available: ")
    print("Resources available: " + resourceNumber + "\nRunning weighted interval algorithm...")
    resourceNumber = int(resourceNumber)

    # Remove quotations from arrays
    weightedIntegerArray = []
    arrayWeightsIntegerLine = []
    for item in weightedStringArray:
        weightedIntegerArray.append(int(item))
    for item in arrayWeightsStringLine:
        arrayWeightsIntegerLine.append(int(item))

    # Defines a function that creates one sorted array, using the weights for each value
    combinedWeightedArray = []
    tempArray = []
    def array_sort(weight):
        count = 0
        while count < (len(arrayWeightsIntegerLine)):
            if arrayWeightsIntegerLine[count] == weight:
                tempArray.append(weightedIntegerArray[count])
            count += 1
        tempArray.sort()
        combinedWeightedArray.extend(tempArray)

    # Call the sorting function for each of the four weights
    # Clear temp array in between each function call; for some reason clearing in function resulted in bugs
    array_sort(1)
    tempArray.clear()
    array_sort(2)
    tempArray.clear()
    array_sort(3)
    tempArray.clear()
    array_sort(4)

    # Initialize variables
    weightedScheduleTotal = 0
    finalWeightedSchedule = []
    i = 0
    # Use while loop to print as many smallest interval values as possible
    # That add up to less than the user specified constraint
    while weightedScheduleTotal < resourceNumber:
        finalWeightedSchedule.append(combinedWeightedArray[i])
        weightedScheduleTotal += combinedWeightedArray[i]
        i += 1

    print("These are the time lengths of the weighted intervals, in the order that they should be picked.")
    print("(Least time taken to greatest)")
    print(finalWeightedSchedule)
