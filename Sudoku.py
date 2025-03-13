



import sys, pygame
import random
import requests
pygame.init()

url = "https://sudoku-api.vercel.app/api/dosuku"
response = requests.get(url)
solution_lists = response.json()['newboard']['grids'][0]['solution']
solution = []
output_lists = response.json()['newboard']['grids'][0]['value']
output = []
for i in range(len(solution_lists)):
    solution.extend(solution_lists[i])

for i in range(len(output_lists)):
    output.extend(output_lists[i])

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
incor = ''
collapsed = True
game_over = False
empty_indexes = []

for i in range(len(output)):
    if output[i] == 0:
        output[i] = 10
#down means sideways
nums = output
true_nums = solution

#massive list of rows and columns
if collapsed == True:
    #input boxes by x,y
    box_1_1 = [nums[0],nums[1],nums[2],nums[9],nums[10],nums[11],nums[18],nums[19],nums[20]]
    box_1_2 = [nums[3],nums[4],nums[5],nums[12],nums[13],nums[14],nums[21],nums[22],nums[23]]
    box_1_3 = [nums[6],nums[7],nums[8],nums[15],nums[16],nums[17],nums[24],nums[25],nums[26]]
    box_2_1 = [nums[27],nums[28],nums[29],nums[36],nums[37],nums[38],nums[45],nums[46],nums[47]]
    box_2_2 = [nums[30],nums[31],nums[32],nums[39],nums[40],nums[41],nums[48],nums[49],nums[50]]
    box_2_3 = [nums[33],nums[34],nums[35],nums[42],nums[43],nums[44],nums[51],nums[52],nums[53]]
    box_3_1 = [nums[54],nums[55],nums[56],nums[63],nums[64],nums[65],nums[72],nums[73],nums[74]]
    box_3_2 = [nums[57],nums[58],nums[59],nums[66],nums[67],nums[68],nums[75],nums[76],nums[77]]
    #solution boxes by x,y
    sol_box_1_1 = [true_nums[0],true_nums[1],true_nums[2],true_nums[9],true_nums[10],true_nums[11],true_nums[18],true_nums[19],true_nums[20]]
    sol_box_1_2 = [true_nums[3],true_nums[4],true_nums[5],true_nums[12],true_nums[13],true_nums[14],true_nums[21],true_nums[22],true_nums[23]]
    sol_box_1_3 = [true_nums[6],true_nums[7],true_nums[8],true_nums[15],true_nums[16],true_nums[17],true_nums[24],true_nums[25],true_nums[26]]
    sol_box_2_1 = [true_nums[27],true_nums[28],true_nums[29],true_nums[36],true_nums[37],true_nums[38],true_nums[45],true_nums[46],true_nums[47]]
    sol_box_2_2 = [true_nums[30],true_nums[31],true_nums[32],true_nums[39],true_nums[40],true_nums[41],true_nums[48],true_nums[49],true_nums[50]]
    sol_box_2_3 = [true_nums[33],true_nums[34],true_nums[35],true_nums[42],true_nums[43],true_nums[44],true_nums[51],true_nums[52],true_nums[53]]
    sol_box_3_1 = [true_nums[54],true_nums[55],true_nums[56],true_nums[63],true_nums[64],true_nums[65],true_nums[72],true_nums[73],true_nums[74]]
    sol_box_3_2 = [true_nums[57],true_nums[58],true_nums[59],true_nums[66],true_nums[67],true_nums[68],true_nums[75],true_nums[76],true_nums[77]]

    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []
    col_5 = []
    col_6 = []
    col_7 = []
    col_8 = []
    col_9 = []
    sol_col_1 = []
    sol_col_2 = []
    sol_col_3 = []
    sol_col_4 = []
    sol_col_5 = []
    sol_col_6 = []
    sol_col_7 = []
    sol_col_8 = []
    sol_col_9 = []
    row_1 = [nums[0],nums[9],nums[18],nums[27],nums[36],nums[45],nums[54],nums[63],nums[72]]
    row_2 = [nums[1],nums[10],nums[19],nums[28],nums[37],nums[46],nums[55],nums[64],nums[73]]
    row_3 = [nums[2],nums[11],nums[20],nums[29],nums[38],nums[47],nums[56],nums[65],nums[74]]
    row_4 = [nums[3],nums[12],nums[21],nums[30],nums[39],nums[48],nums[57],nums[66],nums[75]]
    row_5 = [nums[4],nums[13],nums[22],nums[31],nums[40],nums[49],nums[58],nums[67],nums[76]]
    row_6 = [nums[5],nums[14],nums[23],nums[32],nums[41],nums[50],nums[59],nums[68],nums[77]]
    row_7 = [nums[6],nums[15],nums[24],nums[33],nums[42],nums[51],nums[60],nums[69],nums[78]]
    row_8 = [nums[7],nums[16],nums[25],nums[34],nums[43],nums[52],nums[61],nums[70],nums[79]]
    row_9 = [nums[8],nums[17],nums[26],nums[35],nums[44],nums[53],nums[62],nums[71],nums[80]]
    sol_row_1 = [nums[0],nums[9],nums[18],nums[27],nums[36],nums[45],nums[54],nums[63],nums[72]]
    sol_row_2 = [nums[1],nums[10],nums[19],nums[28],nums[37],nums[46],nums[55],nums[64],nums[73]]
    sol_row_3 = [nums[2],nums[11],nums[20],nums[29],nums[38],nums[47],nums[56],nums[65],nums[74]]
    sol_row_4 = [nums[3],nums[12],nums[21],nums[30],nums[39],nums[48],nums[57],nums[66],nums[75]]
    sol_row_5 = [nums[4],nums[13],nums[22],nums[31],nums[40],nums[49],nums[58],nums[67],nums[76]]
    sol_row_6 = [nums[5],nums[14],nums[23],nums[32],nums[41],nums[50],nums[59],nums[68],nums[77]]
    sol_row_7 = [nums[6],nums[15],nums[24],nums[33],nums[42],nums[51],nums[60],nums[69],nums[78]]
    sol_row_8 = [nums[7],nums[16],nums[25],nums[34],nums[43],nums[52],nums[61],nums[70],nums[79]]
    sol_row_9 = [nums[8],nums[17],nums[26],nums[35],nums[44],nums[53],nums[62],nums[71],nums[80]]
    
    for i in range(0,9):
        col_1.append(nums[i])
        col_2.append(nums[i+9])
        col_3.append(nums[i+18])
        col_4.append(nums[i+27])
        col_5.append(nums[i+36])
        col_6.append(nums[i+45])
        col_7.append(nums[i+54])
        col_8.append(nums[i+63])
        col_9.append(nums[i+72])
        sol_col_1.append(nums[i])
        sol_col_2.append(nums[i+9])
        sol_col_3.append(nums[i+18])
        sol_col_4.append(nums[i+27])
        sol_col_5.append(nums[i+36])
        sol_col_6.append(nums[i+45])
        sol_col_7.append(nums[i+54])
        sol_col_8.append(nums[i+63])
        sol_col_9.append(nums[i+72])

        




background_color = pygame.Color(232, 196, 144)
color = pygame.Color(120,95,30)

#grid
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

#user inputted numbers
def print_numbers():
    
    font = pygame.font.SysFont(None, 24)
    i = 0
    for x in range(10, grid_width + 10, sudokuBlockSize):
        for y in range(10, grid_height + 10, sudokuBlockSize):
            if nums[i] == 10:
                empty_indexes.append(i)
                i+=1
                continue
            else:
                img = font.render(str(nums[i]), True, pygame.Color(120,95,30))
                screen.blit(img, (x+27, y+25))
                i+=1
            
#main loop          
running = True
while running:
    
    for event in pygame.event.get():
            #exits
            if event.type == pygame.QUIT: 
                running = False
            #on key press
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_0:
                    key_var = 10              
                if event.key == pygame.K_1:
                    key_var = 1              
                if event.key == pygame.K_2:
                    key_var = 2      
                if event.key == pygame.K_3:
                    key_var = 3
                if event.key == pygame.K_4:
                    key_var = 4
                if event.key == pygame.K_5:
                    key_var = 5
                if event.key == pygame.K_6:
                    key_var = 6
                if event.key == pygame.K_7:
                    key_var = 7
                if event.key == pygame.K_8:
                    key_var = 8
                if event.key == pygame.K_9:
                    key_var = 9
                if event.key == pygame.K_g:
                    game_over = True
            
            #putting inputted number into correct cell
            if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    for item in rect_list:
                        if item.collidepoint(mouse_pos):
                            for i in range(len(nums)):
                                if i == rect_list.index(item):
                                    nums[i]=key_var
                                    #checking if number inputted matches number in solution
                                    if nums[i] == true_nums[i]:
                                        incor = 'correct'
                                    else:
                                        incor = 'input is incorrect!'
                                
                            break
                        else:
                            continue
            
            if game_over == True:
                a = 0
                b = len(empty_indexes)
                for i in range(len(nums)):
                    if a == b:
                        break
                    if empty_indexes[a] == i:
                        nums[i] = 10
                    a +=1
                game_over = False

            
            screen.fill(background_color)
            drawSudokuGrid()
            # sol_generator()
            print_numbers()
            
            #text info to the right of board
            font = pygame.font.SysFont(None, 17)
            secondary_font = pygame.font.SysFont(None, 22)
            tertiary_font = pygame.font.SysFont(None, 14)

            selected_text = font.render('selected number: ', True, color)
            screen.blit(selected_text, (620,20))

            if key_var == 10:
                text_surface = secondary_font.render('0', True, color)
                screen.blit(text_surface, (720,18))
            else:
                text_surface = secondary_font.render(str(key_var), True, color)
                screen.blit(text_surface, (720,18))

            selected_text = tertiary_font.render('(click 0 to clear cell)', True, color)
            screen.blit(selected_text, (620,35))

            if incor == 'input is incorrect!':
                in_correct = font.render(incor, True, color)
                screen.blit(in_correct, (620,60))

            if nums == true_nums:
                win_display = font.render('win', True, color)
                screen.blit(win_display, (620,100))
            pygame.display.flip()

pygame.quit()