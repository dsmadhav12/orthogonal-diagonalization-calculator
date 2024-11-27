import numpy as np

def input_matrix(size):
    print(f"Enter the elements of {size}x{size} matrix row by row:")
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            value = float(input(f"Enter value for element [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for i in matrix:
        print(i)
    print()
def diagonalize(matrix,size):
    numpyMatrix=np.array(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(numpyMatrix)
    
    if(eigenvectors.shape[1] ==size):
        D = np.diag(eigenvalues)
        P = eigenvectors
        print("P: " +str(P))
        print()
        print("D: " +str(D)) 
        return P, D
    else:
        print("The matrix is niot diagnolizable")
        return None, None
    

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
    print_matrix(matrix)
    diagonalize(matrix, size)

if __name__ == "__main__":
    main()
    