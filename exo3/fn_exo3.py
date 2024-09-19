# fonction de l'exercice 3 du tp 1
# Nathan Chopin
# 19/09/24
# pas fini


def multiplication(A,B):
    '''multiplication de matrice carrée'''
    C = [[0]*len(A)]*len(A)
    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(A)):
                C[i][j] += A[i][k] * B[k][j]
    return C