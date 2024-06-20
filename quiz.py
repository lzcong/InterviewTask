
def reverse_list(l:list):

    """

    TODO: Reverse a list without using any built in functions

 

    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """
    if len(l) <= 1:
        return l

    # Split the list into two halves
    mid = len(l) // 2
    left_half = l[:mid]
    right_half = l[mid:]

    # Recursively sort the left and right halves
    left_half = reverse_list(left_half)
    right_half = reverse_list(right_half)

    # Merge the sorted halves
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_list.append(left_half[left_index])
            left_index += 1
        else:
            sorted_list.append(right_half[right_index])
            right_index += 1

    # Add any remaining elements from the left or right half
    while left_index < len(left_half):
        sorted_list.append(left_half[left_index])
        left_index += 1

    while right_index < len(right_half):
        sorted_list.append(right_half[right_index])
        right_index += 1

    return sorted_list

 

def solve_sudoku(matrix):

    """

    TODO: Write a programme to solve 9x9 Sudoku board.

 

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

 

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """
    def find_empty(bo):
        """
        Finds the next empty cell in the Sudoku board.
        
        Args:
            bo (list of lists): The Sudoku board.
            
        Returns:
            tuple: The row and column indices of the next empty cell, or (None, None) if the board is full.
        """
        for i in range(9):
            for j in range(9):
                if bo[i][j] == 0:
                    return i, j
        return None, None
    
    def is_valid(bo, num, pos):
        """
        Checks if a number is valid in the given position on the Sudoku board.
        
        Args:
            bo (list of lists): The Sudoku board.
            num (int): The number to check.
            pos (tuple): The row and column indices of the cell to check.
            
        Returns:
            bool: True if the number is valid, False otherwise.
        """
        # Check row
        for i in range(9):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False
        
        # Check column
        for i in range(9):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False
        
        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if bo[i][j] == num and (i,j) != pos:
                    return False
        
        return True
    
    def solve(bo):
        """
        Recursively solves the Sudoku board.
        
        Args:
            bo (list of lists): The Sudoku board.
            
        Returns:
            bool: True if the board is solved, False otherwise.
        """
        find = find_empty(bo)
        if find[0] is None:
            return True
        
        row, col = find
        
        for i in range(1, 10):
            if is_valid(bo, i, (row, col)):
                bo[row][col] = i
                
                if solve(bo):
                    return True
                
                bo[row][col] = 0
        
        return False
    
    solve(matrix)
    return matrix

def print_sudoku(board):
    """
    Prints a 9x9 Sudoku board in a formatted manner.
    
    Args:
        board (list of lists): The Sudoku board to be printed.
    """
    print("+-----------------------+")
    for i in range(9):
        print("| ", end="")
        for j in range(9):
            print(board[i][j], end=" ")
            if (j + 1) % 3 == 0:
                print("| ", end="")
        print()
        if (i + 1) % 3 == 0:
            print("+-----------------------+")

# Test function - reverse_list
my_list = [5, 2, 8, 1, 9, 3]
sorted_list = reverse_list(my_list)
print(sorted_list)

string_list = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_string_list = reverse_list(string_list)
print(sorted_string_list) 

# Test function - solve_sudoku
board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]
print_sudoku(board)
solved_board = solve_sudoku(board)
print_sudoku(solved_board)