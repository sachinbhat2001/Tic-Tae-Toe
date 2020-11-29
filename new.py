
import pygame
print("X - Player1")
print("O - Player2")


pygame.init() #activate all the pygame modules

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

pygame.display.set_caption("Tic Tae Toe")  # To give title for the window
window=pygame.display.set_mode((550,550)) #creates a window of dimension 550X550 pixel

#pygame.draw.rect(surface, color, rect)

#ROW 1
first=pygame.draw.rect(window,(255,255,255), (25,25,150,150))
second=pygame.draw.rect(window,(255,255,255), (200,25,150,150))
third=pygame.draw.rect(window,(255,255,255), (375,25,150,150))
#ROW 2
fourth = pygame.draw.rect(window, (255,255,255), (25,200,150,150))
fifth = pygame.draw.rect(window, (255,255,255), (200,200,150,150))
sixth = pygame.draw.rect(window, (255,255,255), (375,200,150,150))
#ROW 3
seventh = pygame.draw.rect(window, (255,255,255), (25,375,150,150))
eighth = pygame.draw.rect(window, (255,255,255), (200,375,150,150))
ninth = pygame.draw.rect(window, (255,255,255), (375,375,150,150))

draw_ob="x"
first_open=True
second_open=True
third_open=True
fourth_open=True
fifth_open=True
sixth_open=True
seventh_open=True
eight_open=True
ninth_open=True
run= True
won=False
def win_check(num):

#to check if player has won by matching pair horizontally

    for row in board:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True
#to check if player has won by matching pair vertically

    for column in range(3):
        for row in board:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True
    
#to check if player has won by matching pair diagonally
    for tile in range(3):
        if board[tile][tile] == num:
            continue
        else:
            break
    else:
        return True
    
    
    for tile in range(3):
        if board[tile][2-tile] == num:
            continue
        else:
            break
    else:
        return True


while run:
    
    pygame.time.delay(100) #pause the window for 100ms
    
    for event in pygame.event.get(): #get the opertion from the user like moving the cursor, right arrow etc.
        if event.type==pygame.QUIT:  # when we click on close button the window closes
            #print(board)
            run=False
        # To make sure board is reset when spacebar is clicked
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                first_open=True
                second_open=True
                third_open=True
                fourth_open=True
                fifth_open=True
                sixth_open=True
                seventh_open=True
                eight_open=True
                ninth_open=True
                run= True  
                first=pygame.draw.rect(window,(255,255,255), (25,25,150,150))
                second=pygame.draw.rect(window,(255,255,255), (200,25,150,150))
                third=pygame.draw.rect(window,(255,255,255), (375,25,150,150))
                #ROW 2
                fourth = pygame.draw.rect(window, (255,255,255), (25,200,150,150))
                fifth = pygame.draw.rect(window, (255,255,255), (200,200,150,150))
                sixth = pygame.draw.rect(window, (255,255,255), (375,200,150,150))
                #ROW 3
                seventh = pygame.draw.rect(window, (255,255,255), (25,375,150,150))
                eighth = pygame.draw.rect(window, (255,255,255), (200,375,150,150))
                ninth = pygame.draw.rect(window, (255,255,255), (375,375,150,150))
        
        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            if won!=True:
                if first.collidepoint(pos) and first_open:#this loop is executed if first box is clicked
                    #print("working.....")
                    
                    if draw_ob =='x':
                        first_box_x1=pygame.draw.line(window,(255,0,0),(50,50),(150,150),10)
                        first_box_x2=pygame.draw.line(window,(255,0,0),(50,150),(150,50),10)
                        draw_ob ='O'
                        board[0][0]=1
                    else:    
                        pygame.draw.circle(window, (0,255,0), (100,100), 50)
                        draw_ob ='x'
                        board[0][0]=2
                    first_open=False
                
                
                if second.collidepoint(pos) and second_open:
                    if draw_ob =='x':
                        second_box_x1=pygame.draw.line(window,(255,0,0),(225,50),(325,150),10)
                        second_box_x2=pygame.draw.line(window,(255,0,0),(225,150),(325,50),10)
                        draw_ob ='O'
                        board[0][1]=1
                    else:
                        pygame.draw.circle(window, (0,255,0), (275,100), 50)
                        draw_ob ='x'
                        board[0][1]=2
                    second_open=False                    
                
                
                if third.collidepoint(pos) and third_open:
                    if draw_ob == 'x':
                        third_box_x1=pygame.draw.line(window,(255,0,0),(400,50),(500,150),10)
                        third_box_x2=pygame.draw.line(window,(255,0,0),(400,150),(500,50),10)
                        draw_ob ='O'
                        board[0][2]=1
                    else:
                        pygame.draw.circle(window, (0,255,0), (450,100), 50)
                        draw_ob ='x'
                        board[0][2]=2
                    third_open=False                    
                
                
                if fourth.collidepoint(pos) and fourth_open:
                    if draw_ob == 'x':

                        fourth_box_x1=pygame.draw.line(window,(255,0,0),(50,225),(150,325),10)
                        fourth_box_x2=pygame.draw.line(window,(255,0,0),(50,325),(150,225),10)
                        draw_ob ='O'
                        board[1][0]=1
                    else:
                        pygame.draw.circle(window, (0,255,0), (100,275), 50)
                        draw_ob ='x'
                        board[1][0]=2
                    fourth_open=False
                
                
                
                if fifth.collidepoint(pos) and fifth_open:
                    if draw_ob =='x':

                        fifth_box_x1=pygame.draw.line(window,(255,0,0),(225,225),(325,325),10)
                        fifth_box_x2=pygame.draw.line(window,(255,0,0),(225,325),(325,225),10)
                        draw_ob ='O'
                        board[1][1]=1
                    else:
                        pygame.draw.circle(window, (0,255,0), (275,275), 50)
                        draw_ob ='x'
                        board[1][1]=2
                    fifth_open=False                    
                
                
                if sixth.collidepoint(pos) and sixth_open:
                    if draw_ob =='x':

                        sixth_box_x1=pygame.draw.line(window,(255,0,0),(400,225),(500,325),10)
                        sixth_box_x2=pygame.draw.line(window,(255,0,0),(400,325),(500,225),10)
                        draw_ob ='O'
                        board[1][2]=1
                    else:
                        pygame.draw.circle(window, (0,255,0), (450,275), 50)
                        draw_ob ='x'
                        board[1][2]=2
                    sixth_open=False
                
                
                
                if seventh.collidepoint(pos) and seventh_open:
                    if draw_ob =='x':

                        seventh_box_x1=pygame.draw.line(window,(255,0,0),(50,400),(150,500),10)
                        seventh_box_x2=pygame.draw.line(window,(255,0,0),(50,500),(150,400),10)
                        draw_ob ='O'
                        board[2][0]=1
                    else:
                        pygame.draw.circle(window, (0,255,0), (100,450), 50)
                        draw_ob ='x'
                        board[2][0]=2

                    seventh_open=False    
                
                
                
                if eighth.collidepoint(pos) and eight_open:
                    if draw_ob =='x':

                        eighth_box_x1=pygame.draw.line(window,(255,0,0),(225,400),(325,500),10)
                        eighth_box_x2=pygame.draw.line(window,(255,0,0),(225,500),(325,400),10)
                        draw_ob ='O'
                        board[2][1]=1
                    else:
                        pygame.draw.circle(window, (0,255,0), (275,450), 50)
                        draw_ob='x'
                        board[2][1]=2
                    eight_open=False    
                
                
                
                if ninth.collidepoint(pos) and ninth_open:
                    if draw_ob =='x':
                        ninth_box_x1=pygame.draw.line(window,(255,0,0),(400,400),(500,500),10)
                        ninth_box_x2=pygame.draw.line(window,(255,0,0),(400,500),(500,400),10)
                        draw_ob ='O'
                        board[2][2]=1
                    else:
                        pygame.draw.circle(window, (0,255,0), (450,450), 50)                
                        draw_ob ='x'
                        board[2][2]=2
                    ninth_open=False
    
    
    if win_check(1):
        #print('player 1 won')
        won = True
    
    if win_check(2):
        #print('player 2 won')
        won = True
        #print('player 2 won')
    pygame.display.update() #updates the screen when changes are made


print("RESULT:")
if win_check(1):
    print('Player 1 won')
if win_check(1)!=True and win_check(2)!=True:
    print('Draw')

if win_check(2):
    print('Player 2 won')




pygame.quit()  


