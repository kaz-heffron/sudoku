

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
key_var = ''
nums = ['','','','','','','','','', #indexes 0-8
            '','','','','','','','','', #indexes 9-17
            '','','','','','','','','',#indexes 18-26
            '','','','','','','','','', #indexes 27-35
            '','','','','','','','','', #indexes 36-44
            '','','','','','','','','', #indexes 45-53
            '','','','','','','','','', #indexes 54-62
            '','','','','','','','','', #indexes 63-71
            '','','','','','','','',''] #indexes 72-80
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
    
    font = pygame.font.SysFont(None, 24)
    i = 0

    #nums
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

            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_0:
                    key_var = ''               
                if event.key == pygame.K_1:
                    key_var = '1'               
                if event.key == pygame.K_2:
                    key_var = '2'      
                if event.key == pygame.K_3:
                    key_var = '3'
                if event.key == pygame.K_4:
                    key_var = '4'
                if event.key == pygame.K_5:
                    key_var = '5'
                if event.key == pygame.K_6:
                    key_var = '6'
                if event.key == pygame.K_7:
                    key_var = '7'
                if event.key == pygame.K_8:
                    key_var = '8'
                if event.key == pygame.K_9:
                    key_var = '9'
                

            if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    for item in rect_list:
                        if item.collidepoint(mouse_pos):
                            for i in range(len(nums)):
                                if i == rect_list.index(item):
                                    nums[i]=str(key_var)
                                
                            print(str(item))
                            print(str(nums))
                            break
                        else:
                            continue
            screen.fill(pygame.Color(232, 196, 144))
            drawSudokuGrid()
            print_numbers()
            
            font = pygame.font.SysFont(None, 17)
            secondary_font = pygame.font.SysFont(None, 22)
            tertiary_font = pygame.font.SysFont(None, 14)

            selected_text = font.render('selected number: ', True, color)
            screen.blit(selected_text, (620,20))

            text_surface = secondary_font.render(key_var, True, color)
            screen.blit(text_surface, (720,18))

            selected_text = tertiary_font.render('(click 0 to clear cell)', True, color)
            screen.blit(selected_text, (620,35))

            pygame.display.flip()

pygame.quit()