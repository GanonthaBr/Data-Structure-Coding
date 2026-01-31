def array_transform(a):
    b = [0 for _ in range(len(a))]
    for i in range(len(a)):
        b[i] = a[i]
        if i > 0:
            b[i] += a[i-1]
        if i < len(a) - 1:
            b[i] += a[i+1]
        

    return b



if __name__ == "__main__":
    arrb = array_transform([4,0,1,-2,3])
    print(arrb)