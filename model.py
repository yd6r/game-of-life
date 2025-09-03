import random

height=100
width=100

#Iterate through each xy coordinate on the grid and randomize its state to 0 or 1
def randomize(grid, width, height):
    for i in range(height):
        for j in range(width):
            grid[i][j]=random.randint(0,1)

#Create two lists of lists representing a 100x100 grid and then randomize the values
grid_model=[0] * height
next_grid_model=[0] * height

for i in range(height):
    grid_model[i]=[0]*width
    next_grid_model[i]=[0] * width

randomize(grid_model, width, height)

#Generate the next generation of cells using the basic rules of the Game of Life
def next_gen():
    global grid_model, next_grid_model

    for i in range(height):
        for j in range(width):
            cell=0
            count = count_neighbors(grid_model, i, j)

            if grid_model[i][j]==0:
                if count==3:
                    cell=1
            elif grid_model[i][j]==1:
                if count==2 or count==3:
                    cell=1
            next_grid_model[i][j]=cell
    temp=grid_model
    grid_model=next_grid_model
    next_grid_model=temp

#Count the number of neighbors surrounding a given cell
def count_neighbors(grid, row, col):
    count=0

    if row-1>=0:
        count+=grid[row-1][col]
    if (row-1>=0) and (col-1>=0):
        count+=grid[row-1][col-1]
    if (row-1>=0) and (col+1<width):
        count+=grid[row-1][col+1]
    if col-1>=0:
        count+=grid[row][col-1]
    if col+1<width:
        count+=grid[row][col+1]
    if row+1<height:
        count+=grid[row+1][col]
    if (row+1<height) and (col-1>=0):
        count+=grid[row+1][col-1]
    if (row+1<height) and (col+1<width):
        count+=grid[row+1][col+1]
    return count

glider_pattern=[[0,0,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,0,0]]

glider_gun_pattern=glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#Loads the sellected pattern to the grid
def load_pattern(pattern, x_offset=0, y_offset=0):
    global grid_model

    for i in range(height):
        for j in range(width):
            grid_model[i][j]=0

    j=y_offset

    for row in pattern:
        i=x_offset
        for value in row:
            grid_model[i][j]=value
            i+=1
        j+=1

if __name__=='__main__':
    next_gen()
