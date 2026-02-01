def firstDuplicate(a):
    new_list = [a[0]]
    for i in range(len(a)-1):
        if a[i+1] in new_list:
            return a[i+1]
        else:
            new_list.append(a[i+1])
    return -1



if __name__ == "__main__":
    case3 = firstDuplicate([2,1,3,5,3,2]) # expected: 3
    print(case3)
    case2 = firstDuplicate([2,2])
    print(case2)
    case_1 = firstDuplicate([2,4,3,5,1])
    print(case_1)