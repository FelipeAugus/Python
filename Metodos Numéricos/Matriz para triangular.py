def setPivo(mat, L):
    for c in range(len(mat)): 
        if(mat[L][c] != 0): 
            return [L, c]

def triang(mat):
    """
    Converte uma matriz quadrada qualquer para triangular inferior
    """
    for L in range(len(mat)):   
        pivo = setPivo(mat, L)
        
        #if (L!=len(mat)-1):
        for l in range(L+1, len(mat)):
            det = (mat[l][pivo[1]] / mat[pivo[0]][pivo[1]])
            
            for c in range(len(mat)): 
                mat[l][c] -= mat[pivo[0]][c]*det 
           
    return mat

M = [[1,2,3],[4,5,6],[7,8,10]]

N = [[0, 324, 123], [0, 0, 57], [31, 45, 97]]
print (triang(N))