"""
Docstring for make_array_consecutive
 - get the max and min of the given array
 - fill in all consecutive integers between min and max and store in an array
 - return the difference of len of the new array with the original
"""

def makeArrayConsecutive(a):
    min_a, max_a = min(a), max(a)
    new_array = []
    for i in range(min_a,max_a+1):
        new_array.append(i)

    return len(new_array) - len(a)


if __name__ == "__main__":
    arr = makeArrayConsecutive([6,2,3,8])
    print(arr)