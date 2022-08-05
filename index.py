import pygame
import numpy as np
black = (0,0,0)
white = (255,255,255)

def game_rules(old_grid,rows,columns): 
    to_update = []
    for row in range(rows):
        for column in range(columns):
            number_of_alive_neighbours = (old_grid[row][(column-1)%columns] + old_grid[row][(column+1)%columns] +
                         old_grid[(row-1)%rows][column] + old_grid[(row+1)%rows][column] +
                         old_grid[(row-1)%rows][(column-1)%columns] + old_grid[(row-1)%rows][(column+1)%columns] +
                         old_grid[(row+1)%rows][(column-1)%columns] + old_grid[(row+1)%rows][(column+1)%columns])
            if(old_grid[row][column] == 0 and number_of_alive_neighbours == 3):
               to_update.append([row,column,1])
            elif(old_grid[row][column] == 1 and (number_of_alive_neighbours < 2 or number_of_alive_neighbours > 3)):
               to_update.append([row,column,0])
    for every_list in to_update:
        row = every_list[0]
        column = every_list[1]
        status = every_list[2]
        old_grid[row][column] = status
    return old_grid

def draw_grid(grid,rows_of_grid,columns_of_grid,width_of_eachcell,height_of_eachcell,margin,screen):
    for row in range(rows_of_grid):
        for column in range(columns_of_grid):
            color = black
            if grid[row][column] == 1:
               color = white
            pygame.draw.rect(screen,
                            color,
                            pygame.Rect((margin + width_of_eachcell) * column + margin,
                            (margin + height_of_eachcell) * row + margin,
                           width_of_eachcell,
                             height_of_eachcell))
            
def main() :
    i=0
    width_of_eachcell = 20
    height_of_eachcell = 20
    columns_of_grid = int(input("Select the number of rows of grid you want to play(must be greater than or equal to 4) :"))
    rows_of_grid = int(input("Select the number of coloums of grid you want to play (must be greater than or equal to 4) :"))
    margin = 2
   
    grid = np.zeros((rows_of_grid,columns_of_grid))
    grid=np.random.randint(2,size=(rows_of_grid,columns_of_grid))
    pygame.init()
   
    size_of_window = [(margin + width_of_eachcell) * rows_of_grid +margin ,
                                (margin + height_of_eachcell) * columns_of_grid +margin ]

    screen = pygame.display.set_mode(size_of_window)

    pygame.display.set_caption("conways game of life ")
   
    while i>=0:
             grid = game_rules(grid,rows_of_grid,columns_of_grid)
             screen.fill(black)
             draw_grid(grid,rows_of_grid,columns_of_grid,width_of_eachcell,height_of_eachcell,margin,screen)
             pygame. display.update()
             pygame.time.delay(500)
    
    sys.exit(0)
    pygame.quit()
    
    

main()
