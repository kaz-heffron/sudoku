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


        print('solution:  ' + str(solution))
        print('output:  ' + str(output))

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
    


print(empty_indexes)     
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
                    print('easy')
                    nums, true_nums = get_solution('easy')
                    game_start = False
                if medium.collidepoint(mouse_pos):
                    print('medium')
                    nums, true_nums = get_solution('medium')
                    game_start = False
                if hard.collidepoint(mouse_pos):
                    print('hard')
                    nums, true_nums = get_solution('hard')
                    game_start = False
            

    if game_start == False:
        for event in pygame.event.get():
            #exits
            if event.type == pygame.QUIT: 
                pygame.quit()
            #on key press
            if event.type == pygame.KEYDOWN:  
                if selected_rect:
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
                    for item in rect_list:
                        if item.collidepoint(mouse_pos):
                            selected_rect = item
    #after here, this stuff goes in key press function
                            for i in range(len(nums)):
                                if i == rect_list.index(item):
                                    #checking if number inputted matches number in solution
                                    if key_var:
                                        nums[i]=str(key_var)
                                        nums[i]=key_var
                                        if nums[i] == true_nums[i]:
                                            incor = 'correct'
                                        else:
                                            incor = 'input is incorrect!'
                                            mistakes+=1
                                        
                                
                            break
                        else:
                            continue
            
            
            
            screen.fill(background_color)
            drawSudokuGrid()
            print_numbers()
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