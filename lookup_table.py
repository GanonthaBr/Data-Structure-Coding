def is_power_of_two(n):
    # A power of 2 must be positive and have exactly one bit set
    return n > 0 and n.bit_count() == 1

def look_up(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):  # Start from i to include same-element pairs
            if is_power_of_two(numbers[i] + numbers[j]):
                count += 1
    return count


if __name__ == "__main__":
    result1 = look_up([1,-1,2,3]) # Expected: 5
    print(result1)
    result2 = look_up([2])    # Expected: 1
    print(result2)