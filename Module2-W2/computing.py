import numpy as np

#compute len of vector
def compute_vector_length(vector):
    return np.sqrt(np.sum(vector ** 2))

#compute dot product
def compute_dot_product(vector1, vector2):
    return np.sum(vector1 * vector2)

#compute matrix multi vector
def matrix_multi_vector(matrix, vector):
    return np.dot(matrix, vector)

#compute matrix multi matrix
def matrix_multi_matrix(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

#inverse matrix
def invert_matrix22(matrix):
    #find determinant
    det = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    
    #deteriminant !=0 >> matrix is invertible
    if det !=0:
        #find inverse
        temp_matrix = [[matrix[1, 1], -matrix[0, 1]], [-matrix[1, 0], matrix[0, 0]]]
        temp_matrix = np.array(temp_matrix)
        return np.dot(1/det, temp_matrix)
    else:
        return None

A= np.array([[-2,6],[8,-4]])
print(A)
print(invert_matrix22(A))

# find eigenvalues and eigenvectors of a matrix
def compute_eigenvalues_eigenvectors ( matrix ) :
    # Compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    # Normalize the eigenvectors
    eigenvectors = eigenvectors / np.linalg.norm(eigenvectors, axis=0)
    
    return eigenvalues, eigenvectors

B = np.array([[0.9, 0.2],[0.1, 0.8]])
print(compute_eigenvalues_eigenvectors(B))

#find Cosine Similarity
def compute_cosine (v1 , v2):
  return compute_dot_product(v1, v2)/(compute_vector_length(v1)*compute_vector_length(v2))

v1 = np.array([1, 2, 3, 4])
v2 = np.array([1, 0, 3, 0])
print(compute_cosine(v1, v2))