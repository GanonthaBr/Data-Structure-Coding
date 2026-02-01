


def palindrom(word):
    
    """
        - we use two pointers i and j
        - we start i from the beginning of the word
        - we start j from the end of the word
        - at each iteration, if word[i] is the same word[j]
        - we have a palindrom, else we dont have
    """
    check = True
    word = word.lower()
    i = 0
    
    while check and i < len(word):
        j = i + 1
        if word[i] == word[-j]:
            check = True
            i += 1
            
        else:
            check = False
            break

    return check


if __name__ == "__main__":
    print(palindrom('aabaa'))