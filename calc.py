import numpy as np
from sympy import Matrix
def input_matrix(size):
    print(f"Enter the elements of {size}x{size} matrix row by row:")
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            value = int(input(f"Enter value for element [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for i in matrix:
        print(i)
    print()
    
def diagonalize(matrix, size):
    matrix = Matrix(matrix)
    lin_inp =find_eigenspaces(matrix)
    if(lin_inp == size):
        P, D = matrix.diagonalize()
        P=P.tolist()
        D=D.tolist()
        print("A is diagonalizeable")
        print()
        print("P = ")
        print_matrix(P)
        print()
        print("D = ") 
        print_matrix(D)
        return P, D
    else:
        print("The matrix is not diagonalizable")
        return None

def find_eigenspaces(matrix):
    tempMatrix = Matrix(matrix)
    eigenvectors = tempMatrix.eigenvects()
    total_independent_eigenvectors = sum(len(v[2]) for v in eigenvectors)
    
    return total_independent_eigenvectors

def orth_diagonalizable(matrix):
    matrix = Matrix(matrix)
    matrixTranspose = matrix.T
    matrixTranspose = matrixTranspose.tolist()
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i,j] != matrixTranspose[i][j]:
                return False
    return True
    

def Gram_Schmidt(matrix, size):
    print("incomplete for now")
def main():
    while True:
        try:
            size = int(input("Enter the size of the square matrix (2 or 3))? "))
            if size not in [2, 3]:
                print("Please enter either 2 or 3!")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number (2 or 3).")
    
    matrix = input_matrix(size)
    print("A = ")
    print_matrix(matrix)
    diagonalize(matrix, size)
    if(orth_diagonalizable(matrix) == False):
        print("A is not orthogonally diagonalizable")
    else:
        print("A is orthogonally diagonalizable")
        print()

    


if __name__ == "__main__":
    main()
    
