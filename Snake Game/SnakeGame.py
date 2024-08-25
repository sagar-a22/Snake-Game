import pygame
import random
import os

pygame.mixer.init()


pygame.init()

White=(255,255,255)
Red=(255,0,0)
Blue=(0,0,255)
Black=(0,0,0)
screen_length=900
screen_breadth=500
GameWindow=pygame.display.set_mode((screen_length,screen_breadth))
pygame.display.set_caption("Snake game")

bgimg= pygame.image.load("assets/snake.jpg")
bgimg= pygame.transform.scale(bgimg,(screen_length,screen_breadth)).convert_alpha()

font=pygame.font.SysFont(None,55) 
def screen_text(text,color,x,y):
    text_screen= font.render(text,True,color)
    GameWindow.blit(text_screen,[x,y])

clock= pygame.time.Clock()


def plot_snk(GameWindow,color,snk_list,snake_length,snake_breadth):
    for x,y in snk_list:
        pygame.draw.rect(GameWindow,color,[x,y,snake_length,snake_breadth])


def Welcome():

    exit_game=False
    while not exit_game:
        GameWindow.fill((233,210,229))
        screen_text("Welcome!",Black,300, 150) 
        screen_text("Press spacebar to Play!",Black, 190, 250) 

        for event in pygame.event.get():
           if event.type==pygame.QUIT:
                exit_game=True

           if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                   GameLoop()

        pygame.display.update()
        clock.tick(60)    


def GameLoop():
    exit_game=False
    game_over=False
    snake_x=40
    snake_y=50
    velocity_x=0
    velocity_y=0
    food_x= random.randint(20,900/2)
    food_y= random.randint(20,500/2)
    score=0
    snake_length=20
    snake_breadth=20
    fps=30
    snk_list=[]
    snk_length=1   
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        highscore= f.read()
    while not exit_game :
        if game_over:
             
            with open("highscore.txt","w") as f:
               f.write(str(highscore)) 
            GameWindow.fill((233,210,229))
            screen_text("Game Over!",Black,280, 200)
            screen_text("Press Enter To Play Again",Black,140, 300)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True    
               
                if event.type==pygame.KEYDOWN:
                    if event.key== pygame.K_RETURN:
                         GameLoop() 
 
    
                        
        else:    
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True    

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x = velocity_x + 10
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x = velocity_x - 10
                        velocity_y=0

                    if event.key== pygame.K_UP:
                        velocity_y = velocity_y - 10
                        velocity_x=0

                    if event.key==pygame.K_DOWN:
                        velocity_y = velocity_y + 10
                        velocity_x=0  

                    if event.key== pygame.K_a:
                        score+=10             

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x) < 6 and abs(snake_y-food_y)<6:
                pygame.mixer.music.load("assets/Food-eating.mp3")
                pygame.mixer.music.play()
                score+=10
                food_x= random.randint(20,900/2)
                food_y= random.randint(20,500/2)
                snk_length +=5
                if score >int( highscore):
                    highscore = score
            
            GameWindow.fill(White)
            GameWindow.blit(bgimg,(0,0))
            screen_text("Score:"+ str(score)+ "      Highscore:"+ str(highscore),White,5,5)
            plot_snk(GameWindow,Blue,snk_list,snake_length,snake_breadth)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]

            pygame.draw.rect(GameWindow,Red,[food_x,food_y,snake_length,snake_breadth])
            if snake_x<0 or snake_x>900 or snake_y<0 or snake_y>500:
                game_over=True
                pygame.mixer.music.load("assets/Game over.mp3")
                pygame.mixer.music.play()

                
            if head in snk_list[:-1]:
                game_over=True 
                pygame.mixer.music.load("assets/Game over.mp3")
                pygame.mixer.music.play()
   

        pygame.display.update()
        clock.tick(fps)
    pygame.QUIT()
    quit()
Welcome()
