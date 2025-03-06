

#imports and initializes
import sys, pygame
pygame.init()

#sets size of display window
size = width, height = 800, 700

#sets name of window
pygame.display.set_caption('sudoku!')

#creates the display object
screen = pygame.display.set_mode(size)

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
grid_width = 300
grid_height = 300
sudokuBlockSize = 33
rect_list= []
color = pygame.Color(120,95,30)

def drawSudokuGrid():
    for x in range(10, grid_width + 10, sudokuBlockSize):
        for y in range(10, grid_height + 10, sudokuBlockSize):
            rect = pygame.Rect(x, y, sudokuBlockSize, sudokuBlockSize)
            rect_list.append(rect)
            pygame.draw.rect(screen, color, rect, 1)
    



pygame.display.flip()


running = True
while running:
    
    for event in pygame.event.get():
            #exits
            
            if event.type == pygame.QUIT: 
                running = False
    screen.fill(pygame.Color(232, 196, 144))
    drawSudokuGrid()
    pygame.display.flip()

pygame.quit()
