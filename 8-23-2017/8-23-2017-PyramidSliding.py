import numpy as np
"""
Notes:
    -need to make the pyramid structure
        -2D array
        -use numpy
        -input comprehension, use a text file much easier
    -implement the path choosing algorithm
        -recursively find all sums?
            -highly inefficent when getting into large pyramids
"""


# given lines of numbers, make a 2D matrix out of it
# assume text is correct matrix for now
# first line tells n number of rows, therefore ever only need matrix[n][n]
# first line in matrix always 1 number
# returns a numpy array
def matrix_maker(file):
    f = open(file,'r')
    m_size = int(f.readline())
    matrix = np.zeros((m_size, m_size), dtype=np.int64)
    for x in range(0, m_size):
        txt_list = (f.readline()).split( )
        while len(txt_list) < m_size:
            txt_list += [0]
        matrix[x] = txt_list
    return matrix

def shortest_sum(matrix):
    #return simple_recur_matrix(matrix, (0,0), 0)
    return dfs_recur_matrix(matrix)

#simple algorithm, from any position, pick the next smaller number, prolly need to use dps or bps
#pass in a matrix, and position, sum to path
# return same matrix, position, sum to path
def simple_recur_matrix(matrix, tuple_pos, sum ):
    if tuple_pos[0]== 0 and tuple_pos[1] == 0:
        sum += matrix[0][0]
    if tuple_pos[0]+1 == matrix.shape[0]:
        return sum
    row = tuple_pos[0]
    col = tuple_pos[1]
    left = matrix[row+1][col]
    right = matrix[row+1][col+1]
    if left < right:
        return simple_recur_matrix(matrix, (row+1,col), left+sum)
    else:
        return simple_recur_matrix(matrix, (row+1, col+1), right+sum)

#ineffecient
def dfs_recur_matrix(matrix):
    stack = []
    sum_list = []
    stack.append((0,0,0))
    while len(stack) is not 0:
        node_tup = stack.pop()
        row = node_tup[0]
        col = node_tup[1]
        new_sum = matrix[row,col] + node_tup[2]
        #push all neighbors
        if row+1 == matrix.shape[0]:
            sum_list.append(new_sum)
        else:
            stack.append((row+1,col,new_sum))
            stack.append((row+1,col+1,new_sum))
    return min(sum_list)





def main():
    if shortest_sum(matrix_maker("8-23-2017-InputText0")) != 7:
        print("Failed Test 1");
    if shortest_sum(matrix_maker("8-23-2017-InputText2")) != 447:
         print("Failed Test 2");
    if shortest_sum(matrix_maker("bigchallengenosol.txt")) != 130572:
        print("Failed test 3")

if __name__ == "__main__":
    main()
