#Rayyan Hasan Goraya
#June 14th 2024
#Final Summative

import os  # Importing the operating system module
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 0)  # Setting the position of the window

import random  # Importing the random module

from pygame import *  # Importing the pygame module
init()  # Initializing pygame

from pygame import mixer  # Importing the mixer submodule from pygame for sound mixing
mixer.init()  # Initializing the mixer

#Loading the Sounds
splash=mixer.Sound("splash.wav")  
touch=mixer.Sound("touch.wav")
end=mixer.Sound("end.wav")
click=mixer.Sound("click.wav")
swim=mixer.Sound("swim.wav")
bomb=mixer.Sound("bomb.wav")

#playing the splash sound in the beginning of the game
splash.play()

screen = display.set_mode((600,700))  # Creating a screen with dimensions 600x600
 
# Defining states for the game
STATE_MENU = 0
STATE_GAME = 1
STATE_HELP = 2
STATE_QUIT = 3

# Loading and scaling images for the menu
titleIMG=image.load("title.png")
titleIMG=transform.scale(titleIMG,(500,120))
menuIMG=image.load("menu.png")
menuIMG=transform.scale(menuIMG,(600,700))
startIMG=image.load("start.png")
startIMG=transform.scale(startIMG,(200,75))
infoIMG=image.load("info.png")
infoIMG=transform.scale(infoIMG,(200,75))
quitIMG=image.load("quit.png")
quitIMG=transform.scale(quitIMG,(200,75))
backIMG=image.load("back.png")
backIMG=transform.scale(backIMG,(75,50))

# Loading and scaling images for the background of the Game
backgroundIMG=image.load("background.jpg")
backgroundIMG=transform.scale(backgroundIMG,(600,700))
fishIMG=image.load("fish.png")
fishIMG=transform.scale(fishIMG,(50,50))
fish1IMG=image.load("fish1.png")
fish1IMG=transform.scale(fish1IMG,(50,50))
fishLineIMG=image.load("fishLine.png")
fishLineIMG=transform.scale(fishLineIMG,(600,50))

#The Random x,y for the 3 bombs
bomb1X=random.randint(50,500)
bomb1Y=random.randint(50,250)
bomb2X=random.randint(50,500)
bomb2Y=random.randint(50,250)
bomb3X=random.randint(50,500)
bomb3Y=random.randint(50,250)

#Loading the bomb
bombIMG=image.load("bomb.png")
bombIMG=transform.scale(bombIMG,(30,30))

# Loading and scaling the plastic images
bottleIMG=image.load("bottle.png")
bottleIMG=transform.scale(bottleIMG,(12,35))
jugIMG=image.load("jug.png")
jugIMG=transform.scale(jugIMG,(35,35))
cokeIMG=image.load("coke.png")
cokeIMG=transform.scale(cokeIMG,(15,25))
spriteIMG=image.load("sprite.png")
spriteIMG=transform.scale(spriteIMG,(15,25))
coffeeIMG=image.load("coffee.png")
coffeeIMG=transform.scale(coffeeIMG,(14,20))

# Creating a list of plastic images and selecting one randomly
garbage=[bottleIMG,jugIMG,cokeIMG,spriteIMG,coffeeIMG]
garbageRAND=random.choice(garbage)
garbageX=random.randint(50,525)
garbageY=-100

# Initial position of the player
playerX=300
playerY=300

# Loading and scaling animations for the player character
player1IMG=image.load("player1.png")
player1IMG=transform.scale(player1IMG,(60,90))
player2IMG=image.load("player2.png")
player2IMG=transform.scale(player2IMG,(90,60))
player3IMG=image.load("player3.png")
player3IMG=transform.scale(player3IMG,(90,60))
playerIMG=player1IMG

# Loading the net image
netIMG=image.load("net.png")
netIMG=transform.scale(netIMG,(60,50))

# Initial score
score=0

#Loading and Scaling Images for Help Page
keyIMG=image.load("keys.png")
keyIMG=transform.scale(keyIMG,(200,100))

#Fonts
font1=font.SysFont("Arial", 20)
myFont = font.SysFont("Times New Roman",30) 

#For player movement
PRESS_RIGHT = False
PRESS_LEFT = False
PRESS_UP = False
PRESS_DOWN = False

# Function to draw the menu screen
def drawMenu(mx, my, button,currentState):
    global rect4
    screen.fill("cadetblue")
    
    # Defining rectangles for menu buttons
    rect1=Rect(200,250,200,75) # Start
    rect2=Rect(200,350,200,75) # Help 
    rect3=Rect(200,450,200,75) # Quit
    rect4=Rect(5,5,75,50) # Back
    
    # Drawing menu elements
    screen.blit(menuIMG,(0,0,600,700))  # Background for the menu  
    screen.blit(titleIMG,(50,100,200,50))
    screen.blit(startIMG,rect1) # Start
    screen.blit(infoIMG, rect2) # Help
    screen.blit(quitIMG, rect3) # Quit
    
    # Checking if the buttons are being pressed and performing actions accordingly
    if rect1.collidepoint(mx,my) and button==1: 
        garbageY=-100
        currentState=STATE_GAME
        click.play()
        
    elif rect2.collidepoint(mx,my) and button==1:
        currentState=STATE_HELP
        click.play()
        
    elif rect3.collidepoint(mx,my) and button==1:
        currentState=STATE_QUIT
        click.play()
        
    return currentState

# Function to draw the game screen
def drawGame(mx, my, button,currentState):
    global garbageY,garbageX, playerX, playerY, playerIMG, garbageRAND, garbage,score, bomb1X, bomb1Y, bomb2X, bomb2Y,bomb3X,bomb3Y
    screen.fill("cadetblue")
    screen.blit(backgroundIMG,(0,0,600,700))
    screen.blit(fishIMG,(450,445,50,50))
    screen.blit(fish1IMG,(200,500,50,50))
    screen.blit(fishLineIMG,(0,390))
    screen.blit(garbageRAND,(garbageX,garbageY))
    screen.blit(bombIMG,(bomb1X,bomb1Y))
    screen.blit(bombIMG,(bomb2X,bomb2Y))
    screen.blit(bombIMG,(bomb3X,bomb3Y))
    
    #Defining rectangles for collision detection
    netRect=Rect(playerX-50,playerY+20,60,50)
    garbageRect=Rect(garbageX,garbageY,10,10)
    bombRect1=Rect(bomb1X,bomb1Y,30,30)
    bombRect2=Rect(bomb2X,bomb2Y,30,30)
    bombRect3=Rect(bomb3X,bomb3Y,30,30)    
    playerRect=Rect(playerX,playerY,50,50)
    
    #Drawing the Player
    screen.blit(playerIMG,(playerX,playerY))
    screen.blit(netIMG,(playerX-50,playerY+20))
    
    bomb1X+=(0.1*(score+1))
    bomb2X+=(0.1*(score+1))
    bomb3X+=(0.1*(score+1))
    
    if bomb1X>600:
        bomb1X=-300   
    if bomb1X<0:
        bomb1X+=(0.1*(score+1))
    if bomb2X>600:
        bomb2X=-300   
    if bomb2X<0:
        bomb2X+=(0.1*(score+1))    
    if bomb3X>600:
        bomb3X=-300   
    if bomb3X<0:
        bomb3X+=(0.1*(score+1))       
    
    #Making the garbage increase in speed as the score increases
    garbageY+=(0.1*(score+1))
    
    #Displaying the score in the bottom right corner
    draw.rect(screen,"cadetblue",(475,650,125,40))
    scoreText=font1.render("SCORE: "+str(score), True,"black")
    screen.blit(scoreText,(500,655))      
        
    # Handling player movement
    if PRESS_RIGHT == True:
        playerIMG=player3IMG #Changing the Image of the player
        playerX += 1
    if PRESS_LEFT == True:
        playerIMG=player2IMG  #Changing the Image of the player
        playerX -= 1
    if PRESS_UP == True:
        playerIMG=player1IMG  #Changing the Image of the player
        playerY -= 1
    if PRESS_DOWN == True:
        playerIMG=player1IMG  #Changing the Image of the player
        playerY += 1
    #When no button is being pressed
    if PRESS_DOWN==False and PRESS_UP==False and PRESS_RIGHT==False and PRESS_LEFT==False:
        playerIMG=player1IMG #Changing the image of player
        
    # Preventing the player from escaping the game area
    if playerX>541:
        playerX=540
    if playerX<-1:
        playerX=0
    if playerY<-1:
        playerY=0
    if playerY>321:
        playerY=320
    
    # when the plastic is dropping down into the ocean 
    if garbageY>0 and garbageY<0.1*(score+1):
        splash.play()
        
    # when the garbage is below the line of fish. this is basically the end game
    if garbageY+30>=400:
        if garbageY+30>400 and garbageY<405:
            end.play()        
        garbageY=1000
        draw.rect(screen,"cadetblue",(0,0,600,700))
        text1=font1.render("Good Try, But the fish are dead and the ocean has been polluted", True,"white")
        text2=font1.render("and has caused global warming, restart by pressing the back button", True,"white")
        pointsText=font1.render("You got "+str(score)+" points!",True,"white")
        screen.blit(text1,(75,70))  
        screen.blit(text2,(75,100))
        screen.blit(pointsText,(75,130)) 
    
    #if the plastic touches the net
    if netRect.colliderect(garbageRect):
        garbageRAND=random.choice(garbage) #randomizing the image for the plastic
        garbageX=random.randint(50,525)
        garbageY=-100
        score+=1
        touch.play()
       
    if bombRect1.colliderect(playerRect) or bombRect2.colliderect(playerRect) or bombRect3.colliderect(playerRect):
        bomb.play()
        garbageY=1000 #so that the code for the end game also displays
        #randomizing the positions of the bombs for when the user wants to retry
        bomb1X=random.randint(50,500)
        bomb1Y=random.randint(50,250)
        bomb2X=random.randint(50,500)
        bomb2Y=random.randint(50,250)  
        bomb3X=random.randint(50,500)
        bomb3Y=random.randint(50,250)         
    
    #to prevent the bombs from collding with each other
    if bombRect1.colliderect(bombRect2) or bombRect2.colliderect(bombRect3) or bombRect1.colliderect(bombRect3):
        bomb1X=random.randint(50,500)
        bomb1Y=random.randint(50,250)
        bomb2X=random.randint(50,500)
        bomb2Y=random.randint(50,250)  
        bomb3X=random.randint(50,500)
        bomb3Y=random.randint(50,250)         

    #Drawing the back button and going back to menu when clicked
    screen.blit(backIMG, rect4)
    if rect4.collidepoint(mx,my) and button==1:
        bomb1X=random.randint(50,500)
        bomb1Y=random.randint(50,250)
        bomb2X=random.randint(50,500)
        bomb2Y=random.randint(50,250)  
        bomb3X=random.randint(50,500)
        bomb3Y=random.randint(50,250)                 
        garbageY=-100
        score=0
        playerY=300
        playerX=300
        playerIMG=player1IMG        
        currentState=STATE_MENU
        click.play()
        
    return currentState
    
# Function to draw the help screen
def drawHelp(mx, my, button,currentState):
    screen.fill("cadetblue")
    info1=font1.render("Clean up the ocean from the plastic because plastic pollution emits", True,"black")
    info2=font1.render("greenhouse gases: methane and CO2, which causes global warming.", True, "black")
    info3=font1.render("Help clean up the ocean of the plastic and also protect the marine life!", True, "black")
    info4=font1.render("Use the arrow keys or W, A, S, and D to move the scuba diver to catch", True, "black")
    info5=font1.render("the plastic in the ocean. Don't let the plastic go below the line of fish", True, "black")
    info6=font1.render("because the marine life will die and the ocean will be polluted by plastic", True, "black")
    info7=font1.render("which will cause global warming. Don't let the player touch the bombs!!", True, "black")
    screen.blit(info1,(50,70))
    screen.blit(info2,(50,100))
    screen.blit(info3,(50,130))
    screen.blit(info4,(50,160))
    screen.blit(info5,(50,190))
    screen.blit(info6,(50,220))
    screen.blit(info7,(50,250))
    screen.blit(keyIMG,(200,300))
    
    #Drawing the back button and going back to menu when clicked
    screen.blit(backIMG, rect4)
    if rect4.collidepoint(mx,my) and button==1:
        currentState=STATE_MENU 
        click.play()
        
    return currentState
    
# Initial state of the game
currentState = STATE_MENU

#defining the mouseX and mouseY
mx = 0
my = 0  

running = True

# Game Loop
while running:
    #reseting the button to 0
    button = 0
    
    # Event handling
    for e in event.get():
        if e.type == QUIT:
            running = False
            
        if e.type == MOUSEBUTTONDOWN:
            #connecting my varaibles, mx, and my to the position of my mouse
            mx, my = e.pos                             
            button = e.button
            
        #making the player movement thing true when the w,a,s,d or arrow keys are pressed down. 
        if e.type == KEYDOWN:
            if e.key == K_RIGHT or e.key==K_d:
                PRESS_RIGHT = True
                swim.play()
            if e.key == K_LEFT or e.key==K_a:
                PRESS_LEFT = True 
                swim.play()
            if e.key == K_UP or e.key==K_w:
                PRESS_UP = True
                swim.play()
            if e.key == K_DOWN or e.key==K_s:
                PRESS_DOWN = True
                swim.play()
                
        #making the player movement thing true when the w,a,s,d or arrow keys aren't pressed. 
        elif e.type == KEYUP:
            if e.key == K_RIGHT or e.key==K_d:
                PRESS_RIGHT = False
            if e.key == K_LEFT or e.key==K_a:
                PRESS_LEFT = False 
            if e.key == K_UP or e.key==K_w:
                PRESS_UP = False
            if e.key == K_DOWN or e.key==K_s:
                PRESS_DOWN = False           
        if e.type == MOUSEMOTION:
            mx, my = e.pos
    
    # Handling different game states and calling the functions accord to which state the game is in.
    if currentState == STATE_MENU:     
        currentState = drawMenu(mx, my, button,currentState)
    elif currentState == STATE_GAME:          
        currentState = drawGame(mx, my, button, currentState)  
    elif currentState == STATE_HELP:
        currentState = drawHelp(mx, my, button, currentState)  
    elif currentState == STATE_QUIT:
        running=False
      
    display.update()  # Updating the display  
quit()  # Exiting the game