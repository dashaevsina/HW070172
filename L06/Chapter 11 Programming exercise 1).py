# Chapter 11, programming exercise 1
# This program calculates the statistics
# and provides more flexibility when 
# computing the mean and/or standard deviation.

from math import sqrt

def getNumbers():
    nums = [] # start with an empty list

    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)      # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums

def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)

def stdDev(nums, xbar):
    xbar = mean(nums)
    sumDevSq = 0.0
    for num in nums:
        dev = xbar - num
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(nums)-1))

def meanStdDev(nums):
    xbar = mean(nums)
    std = stdDev(nums, xbar)
    return xbar, std

def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        med = (nums[midPos] + nums[midPos-1]) / 2
    else:
        med = nums[midPos]
    return med

def main():
    print("This program computes the mean, median, and standard deviation.")
    num = input("Enter a series of whole numbers (separated by commas): ")
    nums = num.split(",")
    for i in range(len(nums)):
        nums[i] = eval(nums[i])

    x = 0
    while x != "":

        x = (input("Type 'mean', 'med', 'std' or 'meanStdDev' to print \n the results. Press <Enter> to exit. "))
        if x == "mean":
            print("\nThe mean is", mean(nums), ".\n")
        elif x == "med":
            print("\nThe median is", median(nums), ".\n")
        elif x == "std":
            print("\nThe standard deviation is", stdDev(nums, mean), ".\n")
        elif x == "meanStdDev":
            print("\nThe mean and the standard deviation is", meanStdDev(nums), "respectively.\n")
        elif x == "":
            break
        else:
            print("Please type a valid input.")

if __name__ == '__main__': main()
