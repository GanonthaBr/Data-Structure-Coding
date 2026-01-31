def pattern_matching(pattern, source):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    new_source = ''
    count = 0
    for char in source:
        if char in vowels:
            new_source += '0'
        else:
            new_source += '1'
    k = len(pattern)
    matches = [new_source[i:i+k] for i in range(0,len(new_source),1)]
    for i in matches:
        if i == pattern:
            count+=1
    return count



if __name__ == "__main__":
    string1 = pattern_matching('010','amazing')
    print(string1)
    string2 = pattern_matching('100','codesignal')
    print(string2)