board = [ [7,8,0,4,0,0,1,2,0],
          [6,0,0,0,7,5,0,0,9],
          [0,0,0,6,0,1,0,7,8],
          [0,0,7,0,4,0,2,6,0],
          [0,0,1,0,5,0,9,3,0],
          [9,0,4,0,6,0,0,0,5],
          [0,7,0,3,0,0,0,1,2],
          [1,2,0,0,0,7,4,0,0],
          [0,4,9,2,0,6,0,0,7]]



def solve(bord):

    find = find_empty_block(bord) #to find empty place if not find we have done
    #base case to find empty place
    if not find:
        return True   
    else:
        row, col = find #empty place position  

    for i in range(1,10):
        if validate_number(bord,i,(row,col)):
            bord[row][col] = i

            if solve(bord):
                return True

            bord[row][col] = 0

    return False



def validate_number(bord, num, pos): #pos is tuple of row and col

    #checking row
    for i in range(len(bord[0])):
        if bord[pos[0]][i] == num and pos[1]!=i: #as we have insterted num already so to ignore the place at which we have inserted the num wwe have used pos[0]!=i
            return False
    
    #check column
    for i in range(len(bord)):
        if bord[i][pos[1]] == num and pos[0]!=i:
            return False

    #check box
    box_x = pos[1]//3 #this give value 0,1,2 whixh show no of box of col no
    box_y = pos[0]//3 #this give value 0,1,2 whixh show no of box of row no
    
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3,box_x*3 + 3):
            if bord[i][j] == num and (i,j) != pos:
                return False


    return True

def print_board(bord):

    for i in range(len(bord)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - - ")
        
        for j in range(len(bord[0])):
            if j%3==0 and j!=0:
                print(" | ",end ="")

            if j == 8:
                print(bord[i][j]) 
            else:
                print(str(bord[i][j]) + " ",end="")

#print(print_board(board))

def find_empty_block(bord):

    for i in range(len(bord)):
        for j in range(len(bord[0])):
            if bord[i][j]==0:
                return (i,j) # tuple of row and column


    return None



print(print_board(board))
solve(board)
print("-------------------------------------------------------------------------------------")
print(print_board(board))