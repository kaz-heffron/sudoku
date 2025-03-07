

import sys, pygame
pygame.init()

size = width, height = 800, 700
pygame.display.set_caption('sudoku!')
screen = pygame.display.set_mode(size)

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
grid_width = 550
grid_height = 550
sudokuBlockSize = 66
rect_list= []
nums = [0,0,0,0,0,0,0,0,0, #indexes 0-8
            0,0,0,0,0,0,0,0,0, #indexes 9-17
            0,0,0,0,0,0,0,0,0, #indexes 18-26
            0,0,0,0,0,0,0,0,0, #indexes 27-35
            0,0,0,0,0,0,0,0,0, #indexes 36-44
            0,0,0,0,0,0,0,0,0, #indexes 45-53
            0,0,0,0,0,0,0,0,0, #indexes 54-62
            0,0,0,0,0,0,0,0,0, #indexes 63-71
            0,0,0,0,0,0,0,0,0,] #indexes 72-80
color = pygame.Color(120,95,30)

def drawSudokuGrid():
    for x in range(10, grid_width + 10, sudokuBlockSize):
        for y in range(10, grid_height + 10, sudokuBlockSize):
            rect = pygame.Rect(x, y, sudokuBlockSize, sudokuBlockSize)
            rect_list.append(rect)
            pygame.draw.rect(screen, color, rect, 1)
            
    cor = 10
    for i in range(4):
        pygame.draw.line(screen, pygame.Color(8, 8, 8), (10,cor), (603,cor),width=2)
        pygame.draw.line(screen, pygame.Color(8, 8, 8), (cor,10), (cor,603),width=2)
        cor += 197

def print_numbers():
    #one row represents on COLUMN
    
    font = pygame.font.SysFont(None, 24)
    i = 0

    for x in range(10, grid_width + 10, sudokuBlockSize):
        for y in range(10, grid_height + 10, sudokuBlockSize):
            img = font.render(str(nums[i]), True, pygame.Color(120,95,30))
            screen.blit(img, (x+27, y+25))
            i+=1
            
running = True
while running:
    
    for event in pygame.event.get():
            #exits
            
            if event.type == pygame.QUIT: 
                running = False
    
            elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    for item in rect_list:
                        if item.collidepoint(mouse_pos):
                            chosen_num = input("input #")
                            for i in range(len(nums)):
                                if i == rect_list.index(item):
                                    nums[i]=chosen_num
                                
                            print(str(item))
                            print(str(nums))
                            break
                        else:
                            continue
            screen.fill(pygame.Color(232, 196, 144))
            drawSudokuGrid()
            print_numbers()
            pygame.display.flip()

pygame.quit()