def centuryFromYear(year):
    # Divide the year by 100
    # if answer if not a whole number, we round it to the next integer
    
    if year % 100 != 0:
        return year // 100 + 1
    else:
        return year // 100
    

if __name__ == "__main__":
    print(centuryFromYear(1905))  # expected output: 20
    print(centuryFromYear(1700))  # expected output: 17