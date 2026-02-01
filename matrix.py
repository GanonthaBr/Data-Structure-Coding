

"""
- we will create a bunch of arrays corresponding to each col of our matrix
- then we will sum each array elts until we reach a 0
- finally we sum up all results

"""

def matrix_sum(matrix):
    vector_col = [[] for _ in range(len(matrix[0]))]
    for vector in matrix:
        for j in range(len(vector)):
            vector_col[j].append(vector[j])

    total = 0
    for col in vector_col:
        for item in col:
            if item == 0:
                break
            else:
                total += item
    return total



if __name__ == "__main__":
    matrix = [
    [0,1,1,2],
    [0,5,0,0],
    [2,0,3,3]
]
    total = matrix_sum(matrix)
    print(total)