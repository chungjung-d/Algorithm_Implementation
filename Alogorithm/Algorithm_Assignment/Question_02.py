def rotateMat(mat):
    for index in range(len(mat)):
        mat[index] = list(reversed(mat[index]))
    mat = list(reversed(mat))    
    print(mat)