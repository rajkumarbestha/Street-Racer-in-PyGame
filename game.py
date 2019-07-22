# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 08:36:54 2019

@author: Rajkumar
"""

import pygame
import time
import random
from utils.colours import gray, black, red, green, blue, bright_red, bright_green, bright_blue

# Load pygame resources.
pygame.init()

# Set width and height of the game display
display_width = 800
display_height = 600
gamedisplay = pygame.display.set_mode((display_width, display_height))

# Window Title.
pygame.display.set_caption("Street Racer")

clock = pygame.time.Clock()

# Load Images.
car_img = pygame.image.load('assets/images/car1.png')
grass_img = pygame.image.load('assets/images/grass.jpg')
yellow_strip = pygame.image.load('assets/images/yellow_strip.jpg')
white_strip = pygame.image.load('assets/images/white_strip.jpg')
crash_img = pygame.image.load('assets/images/crash.png')
start_img = pygame.image.load('assets/images/background.jpg')
instruct_img = pygame.image.load('assets/images/instruct.jpg')
pygame.mixer.music.load("assets/music/Hurry_Up.mp3")


def start_game():
    """
    The Game Intro starts here.
    """
    
    intro=True
    pygame.mixer.music.play(-1)
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                #sys.exit()
        gamedisplay.blit(start_img,(0,0))
        gamedisplay.blit(instruct_img,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',70)
        TextSurf,TextRect=text_objects("STREET RACER",largetext)
        TextRect.center=(400,140)
        gamedisplay.blit(TextSurf,TextRect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("QUIT",550,520,100,50,red,bright_red,"quit")
        button("INSTRUCTIONS",300,520,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)

def show_rules():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                #sys.exit()
        gamedisplay.blit(instruct_img,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',70)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("This is a Car Game in which you need to dodge the coming Cars",smalltext)
        textRect.center=((400),(200))
        TextSurf,TextRect=text_objects("INSTRUCTIONS",largetext)
        TextRect.center=((400),(130))
        gamedisplay.blit(TextSurf,TextRect)
        gamedisplay.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        stextRect.center=((150),(350))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(400))
        atextSurf,atextRect=text_objects("A : ACCELERATOR",smalltext)
        atextRect.center=((150),(450))
        rtextSurf,rtextRect=text_objects("B : BRAKE ",smalltext)
        rtextRect.center=((150),(500))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((360),(250))
        gamedisplay.blit(sTextSurf,sTextRect)
        gamedisplay.blit(stextSurf,stextRect)
        gamedisplay.blit(hTextSurf,hTextRect)
        gamedisplay.blit(atextSurf,atextRect)
        gamedisplay.blit(rtextSurf,rtextRect)
        button("BACK",650,500,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def set_race_track():
    gamedisplay.blit(grass_img, (0,0))
    gamedisplay.blit(grass_img, (display_width-100,0))
    for strip in range(0,10):
        gamedisplay.blit(yellow_strip, (display_width*0.49,75 * strip))
        gamedisplay.blit(white_strip, (120,75 * strip))
        gamedisplay.blit(white_strip, (display_width - 122,75 * strip))
        
def car(x, y):
    gamedisplay.blit(car_img, (x,y))

def text_objects(text, font, color = black):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                game()
            elif action=="quit":
                pygame.quit()
                quit()
                #sys.exit()
            elif action=="intro":
                show_rules()
            elif action=="menu":
                start_game()
    else:
        pygame.draw.rect(gamedisplay,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplay.blit(textsurf,textrect)
    
def set_score(passed, score, obs_speed):
    font = pygame.font.SysFont(None,25)
    passes = font.render("Passed: "+str(passed),True, black)
    scored = font.render("Score: "+str(score),True, blue)
    speed = font.render("Speed: "+str(obs_speed*5)+'Km/Hr',True, red)
    gamedisplay.blit(passes,(5,50))
    gamedisplay.blit(speed, (5,70))
    gamedisplay.blit(scored,(5,30))

def message_display(text,size,x,y):
	 font = pygame.font.Font("freesansbold.ttf",size)
	 text_surface , text_rectangle = text_objects(text,font)
	 text_rectangle.center =(x,y)
	 gamedisplay.blit(text_surface,text_rectangle)
    
def crash(x,y):
    gamedisplay.blit(crash_img,(x-10,y))
    message_display("You Crashed!",80,display_width/2,display_height/2)
    message_display("Restarting!",40,display_width/2,(display_height/2)+100)
    pygame.display.update()
    time.sleep(3)
    start_game()

def set_obstacles(obstacle_start_x, obstacle_start_y, obs):
    obstacle_img = pygame.image.load('assets/images/car'+str(obs)+'.jpg')
    gamedisplay.blit(obstacle_img, (obstacle_start_x, obstacle_start_y))


def game():
    """
    The Actual Game starts here.
    """
    
    x = (display_width*0.49)
    y = (display_height*0.8)
    x_change = 0
    car_width = 50
    obstacle_speed = 10
    obs = 1
    obstacle_start_x = random.randrange(140, display_width-140)
    obstacle_start_y = -750
    obstacle_width = 50
    obstacle_height = 111
    cars_passed = 0
    level = 0
    score = 0
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_a:
                    obstacle_speed+=2
                if event.key == pygame.K_b:
                    obstacle_speed-=2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x+=x_change  
        gamedisplay.fill((110,110,110))
        set_race_track()
        obstacle_start_y-=(obstacle_speed/4)
        set_obstacles(obstacle_start_x, obstacle_start_y, obs)
        obstacle_start_y+=obstacle_speed
        car(x,y)
        set_score(cars_passed, score, obstacle_speed)
        if x > display_width - 135 or x < 100:
            crash(x, y)
        if obstacle_start_y > display_height:
            obstacle_start_y = 0 - obstacle_height
            obstacle_start_x = random.randrange(160, (display_width-160))
            obs = random.randrange(1,7)
            cars_passed+=1
            score=cars_passed*10
            if int(cars_passed)%10 == 0:
                level+=1
                obstacle_speed+=2
                message_display("Level "+str(level),40,display_width/2,(display_height/2)+100)
                pygame.display.update()
                time.sleep(1)
        if y < obstacle_start_y + obstacle_height:
            if x > obstacle_start_x and x < obstacle_start_x + obstacle_width or x+car_width > obstacle_start_x \
                and x+car_width < obstacle_start_x + obstacle_width:
                    crash(x,y)
        pygame.display.update()
        clock.tick(55)

if __name__ == "__main__":
    start_game()
    pygame.quit()
    quit()