# fonction de l'exercice 3 du tp 1
# Nathan Chopin
# 19/09/24

def multiplication(A,B):
    '''multiplication de matrice carrée'''
    C = [[0]*len(A)]*len(A)
    for a in range(len(A)):
        for b in range(len(B)):
            for c in range(len(A)):
                C[b][a] += A[b][c] * B[c][a]
    return C