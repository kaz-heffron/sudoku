import sys, pygame
import random
import requests
pygame.init()


nums = []
true_nums = []
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
key_var = None
incor = ''
game_over = False
empty_indexes = []
mistakes = 0
selected_rect = None
game_start = True
easy = pygame.Rect(300,300,50,50)
medium = pygame.Rect(400,300,50,50)
hard = pygame.Rect(500,300,50,50)
marking = False
mark_button = pygame.Rect(620,130,40,30)
new_g_button = pygame.Rect(43,623,80,23)
p_num = 0
marked_list = [[0,0,0,0,0,0,0,0,0,] for _ in range(81)]



rows = [
    [0,  9, 18, 27, 36, 45, 54, 63, 72],
    [1, 10, 19, 28, 37, 46, 55, 64, 73],
    [2, 11, 20, 29, 38, 47, 56, 65, 74],
    [3, 12, 21, 30, 39, 48, 57, 66, 75],
    [4, 13, 22, 31, 40, 49, 58, 67, 76],
    [5, 14, 23, 32, 41, 50, 59, 68, 77],
    [6, 15, 24, 33, 42, 51, 60, 69, 78],
    [7, 16, 25, 34, 43, 52, 61, 70, 79],
    [8, 17, 26, 35, 44, 53, 62, 71, 80]
]
 
columns = [
    [ 0,  1,  2,  3,  4,  5,  6,  7,  8],
    [ 9, 10, 11, 12, 13, 14, 15, 16, 17],
    [18, 19, 20, 21, 22, 23, 24, 25, 26],
    [27, 28, 29, 30, 31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40, 41, 42, 43, 44],
    [45, 46, 47, 48, 49, 50, 51, 52, 53],
    [54, 55, 56, 57, 58, 59, 60, 61, 62],
    [63, 64, 65, 66, 67, 68, 69, 70, 71],
    [72, 73, 74, 75, 76, 77, 78, 79, 80]
]
 
quadrants = [
    [ 0,  1,  2,  9, 10, 11, 18, 19, 20],
    [ 3,  4,  5, 12, 13, 14, 21, 22, 23],
    [ 6,  7,  8, 15, 16, 17, 24, 25, 26],
    [27, 28, 29, 36, 37, 38, 45, 46, 47],
    [30, 31, 32, 39, 40, 41, 48, 49, 50],
    [33, 34, 35, 42, 43, 44, 51, 52, 53],
    [54, 55, 56, 63, 64, 65, 72, 73, 74],
    [57, 58, 59, 66, 67, 68, 75, 76, 77],
    [60, 61, 62, 69, 70, 71, 78, 79, 80]
]


background_color = pygame.Color(232, 196, 144)
color = pygame.Color(120,95,30)
for x in range(10, grid_width + 10, sudokuBlockSize):
        for y in range(10, grid_height + 10, sudokuBlockSize):
            rect = pygame.Rect(x, y, sudokuBlockSize, sudokuBlockSize)
            rect_list.append(rect)
            
#grid
def drawSudokuGrid():
    for rect in rect_list:
        pygame.draw.rect(screen, color, rect, 1)
    cor = 10
    for i in range(4):
        pygame.draw.line(screen, pygame.Color(8, 8, 8), (10,cor), (603,cor),width=2)
        pygame.draw.line(screen, pygame.Color(8, 8, 8), (cor,10), (cor,603),width=2)
        cor += 197
    pygame.draw.rect(screen, color, new_g_button, 1)
    font = pygame.font.SysFont(None, 16)
    new_g_text = font.render('NEW GAME', True, color)
    screen.blit(new_g_text, (50,630))

    
def drawMarkButton():
    if marking: 
        pygame.draw.rect(screen, color, mark_button, 5)
        font = pygame.font.SysFont(None, 17)
        mark_text = font.render('mark', True, (51, 29, 6))
        screen.blit(mark_text, (mark_button.x+6,mark_button.y+8))
    else:
        pygame.draw.rect(screen, color, mark_button, 1)
        font = pygame.font.SysFont(None, 17)
        mark_text = font.render('mark', True, color)
        screen.blit(mark_text, (mark_button.x+6,mark_button.y+8))


def difficulty_screen():
    screen.fill(background_color)
    font = pygame.font.SysFont(None, 17)
    easy = pygame.Rect(300,300,50,50)
    medium = pygame.Rect(400,300,50,50)
    hard = pygame.Rect(500,300,50,50)
    pygame.draw.rect(screen,color,easy,1)
    pygame.draw.rect(screen,color,medium,1)
    pygame.draw.rect(screen,color,hard,1)
    choose_text = font.render('choose difficulty level', True, pygame.Color(8, 8, 8))
    screen.blit(choose_text, (350, 250))
    easy_text = font.render('easy', True, pygame.Color(8, 8, 8))
    screen.blit(easy_text, (312,318))
    medium_text = font.render('medium', True, pygame.Color(8, 8, 8))
    screen.blit(medium_text, (404,318))
    hard_text = font.render('hard', True, pygame.Color(8, 8, 8))
    screen.blit(hard_text, (512,318))
    pygame.display.flip()

#user inputted numbers
def get_solution(url_difficulty):
    
    pi_url = f'https://api.api-ninjas.com/v1/sudokugenerate?difficulty={url_difficulty}'
    response = requests.get(pi_url, headers={'X-Api-Key': '0D+nsuUABvU9bHDcJytEag==khTAs59PpAVAGQRE'})
    if response.status_code == 200:

        solution_lists = response.json()['puzzle']
        solution = []
        output_lists = response.json()['solution']
        output = []
        for i in range(len(solution_lists)):
            solution.extend(solution_lists[i])

        for i in range(len(output_lists)):
            output.extend(output_lists[i])
  
        for i in range(len(solution)):
            if solution[i] == None:
                solution[i] = 10
        
        return solution, output
    else:
        print("api down")
        quit()

def print_numbers():
    
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = 10
    
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
    
def get_section():
    for section in quadrants:
        if rect_list.index(selected_rect) in section:
            return section

def get_row():
    for row in rows:
        if rect_list.index(selected_rect) in row:
            return row

def get_column():
    for col in columns:
        if rect_list.index(selected_rect) in col:
            return col

def markups():
    a = 0
    if a < 81:
        for rect in rect_list:
            if nums[rect_list.index(rect)] != 10:
                continue
            x = rect.x + 8
            y = rect.y + 8
            font = pygame.font.SysFont(None, 17)
            current_marks = marked_list[rect_list.index(rect)]
            for i in range(9):
                if current_marks[i] == 0:
                    marks = font.render(str(current_marks[i]), True, background_color)
                else:
                    marks = font.render(str(current_marks[i]), True, color)
                screen.blit(marks, (x,y))

                if i == 2:
                    x += 22
                    y = rect.y + 8
                elif i == 5:
                    x += 22
                    y = rect.y + 8
                else:
                    y += 22   
            a += 1
    
def clean_marks(key_var):
    current_section = get_section()
    current_row = get_row()
    current_column = get_column()

    for index in current_section:
        for index2 in range(len(marked_list[index])):
            if marked_list[index][index2] == key_var:
                marked_list[index][index2] = 0
    for index in current_row:
        for index2 in range(len(marked_list[index])):
            if marked_list[index][index2] == key_var:
                marked_list[index][index2] = 0
    for index in current_column:
        for index2 in range(len(marked_list[index])):
            if marked_list[index][index2] == key_var:
                marked_list[index][index2] = 0



#main loop     

running = True
while running:
    
    while game_start == True:
        #difficulty level screen
        difficulty_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy.collidepoint(mouse_pos):
                    nums, true_nums = get_solution('easy')
                    game_start = False
                if medium.collidepoint(mouse_pos):
                    nums, true_nums = get_solution('medium')
                    game_start = False
                if hard.collidepoint(mouse_pos):
                    nums, true_nums = get_solution('hard')
                    game_start = False
            

    if game_start == False:
        for event in pygame.event.get():
            #exits
            if event.type == pygame.QUIT: 
                pygame.quit()
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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if mark_button.collidepoint(mouse_pos):
                        marking = not marking
                    for item in rect_list:
                        if item.collidepoint(mouse_pos):
                            selected_rect = item
                            if not marking:
                                for i in range(len(nums)):
                                    if i == rect_list.index(item):
                                        #checking if number inputted matches number in solution
                                        if key_var:
                                            nums[i]=str(key_var)
                                            nums[i]=key_var
                                            if nums[i] == true_nums[i]:
                                                incor = 'correct'
                                                clean_marks(key_var)
                                            else:
                                                incor = 'input is incorrect!'
                                                mistakes+=1
                                            
                            else:
                                if key_var == 1:
                                    marked_list[rect_list.index(selected_rect)][0] = 1
                                if key_var == 2:
                                    marked_list[rect_list.index(selected_rect)][1] = 2
                                if key_var == 3:
                                    marked_list[rect_list.index(selected_rect)][2] = 3
                                if key_var == 4:
                                    marked_list[rect_list.index(selected_rect)][3] = 4
                                if key_var == 5:
                                    marked_list[rect_list.index(selected_rect)][4] = 5
                                if key_var == 6:
                                    marked_list[rect_list.index(selected_rect)][5] = 6
                                if key_var == 7:
                                    marked_list[rect_list.index(selected_rect)][6] = 7
                                if key_var == 8:
                                    marked_list[rect_list.index(selected_rect)][7] = 8
                                if key_var == 9:
                                    marked_list[rect_list.index(selected_rect)][8] = 9


                            break
                        else:
                            continue
            
            
            
            
    
    z = 0
    # sol_generator()

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
    drawMarkButton()
    if z == 0:
        markups()
        z += 1
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
        screen.blit(win_display, (620,120))
    mis_display = font.render(str(mistakes)+' / 3 mistakes', True, color)
    screen.blit(mis_display, (620,100))
    if mistakes == 3:
        lose_display = font.render('lose', True, color)
        screen.blit(lose_display, (620,120))
    pygame.display.flip()

pygame.quit()