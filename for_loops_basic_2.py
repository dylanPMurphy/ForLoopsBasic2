global_list = [123,12,2,-23,2,-123,23,-12,-23,-534,2]

# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#     Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def positiveIntsToBig(list):
    for i in range(0,len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
print(positiveIntsToBig(global_list))
# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#     Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#     Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#     Example: sum_total([1,2,3,4]) should return 10
#     Example: sum_total([6,3,-2]) should return 7
def sumTotal(list):
    sum = 0
    for i in range(0,len(list)):
        sum+=list[i]
    return sum

print(sumTotal([2,3,4,5]))

# Average - Create a function that takes a list and returns the average of all the values.
#     Example: average([1,2,3,4]) should return 2.5

def avg(list):
    return sumTotal(list)/len(list)
print(avg([2,3,4,5]))

# Length - Create a function that takes a list and returns the length of the list.
#     Example: length([37,2,1,-9]) should return 4
#     Example: length([]) should return 0
def lengthofList(list):
    return len(list)
global_list = [123,12,2,-23,2,-123,23,-12,-23,-534,2]

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#     Example: minimum([37,2,1,-9]) should return -9
#     Example: minimum([]) should return False
def minInList(list):
    if not list:
        print("ERROR: input cannot be empty")
    min = list[0]
    for i in range(0,len(list)):
        if list[i] < min:
            min = list[i]
    return min
print(minInList(global_list))
# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#     Example: maximum([37,2,1,-9]) should return 37
#     Example: maximum([]) should return False
def maxInList(list):
    if not list:
        print("ERROR: input cannot be empty")
    max = list[0]
    for i in range(0,len(list)):
        if list[i] > max:
            max  = list[i]
    return max

print(maxInList(global_list))
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#     Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def listAnalysis(list):
    analyticObject = {
        "sumTotal":sumTotal(list),
        "average":avg(list),
        "minimum":minInList(list),
        "maximum":maxInList(list),
        "length":lengthofList(list)
    }
    return analyticObject
print(listAnalysis(global_list))
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#     Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(list):
    for i in range(0,len(list)):
        if i >= len(list)-(i+1):
            break
        temp = list[i]
        list[i] = list[len(list)-(i+1)]
        list[len(list)-(i+1)]= temp
    return list
print(reverse_list(global_list))