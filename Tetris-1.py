# Tetris by: Johnson Lee
#
# This program is a game called Tetris that was first sold in 1984
# The goal of this game is to try and get the highest score 
# As you play try and not stack the blockor else the game ends
#
#Ideas were taken from
#https://gist.github.com/silvasur/565419
#https://www.youtube.com/watch?v=NuhuzJAibNI

# Last modified: Jan. 25, 2017

import pygame,sys,random,easygui
from os import path 
pygame.init()
pygame.mixer.init()
pygame.key.set_repeat(1, 100)
size = width, height = 807, 640
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tetris')
font = pygame.font.SysFont("Arial",36)
black = [0, 0, 0]
white = [255,255,255]
grey=[211,211,211]
red=[255,0,0]
x=200
y=0
timer = 0
clear=0
drop_timer=0
tetrissscounter = 0
file='Tetris_Music.mp3'
### walls ###
bottom = pygame.Rect(0,560,420,20)
left= pygame.Rect(0,0,40,640)
rightside = pygame.image.load("rightside.png")
leftside = pygame.image.load("leftside.png")
bottomside = pygame.image.load("bottomside.png")
### generating shapes ###
shape=random.randint(0,6)
shape2=random.randint(0,6)


def game_start():
    easygui.msgbox('Welcome to Tetris')
    easygui.msgbox('To move the pieces left or right use the left/right arrow keys')
    easygui.msgbox('To move the pieces down faster press down arrow')
    easygui.msgbox('To rotate the pieces press the up arrow')
    easygui.msgbox('The scores are calculated by number of rows cleared')
    easygui.msgbox('1 line=100 points')
    easygui.msgbox('2 lines=200 points')
    easygui.msgbox('3 lines= 400 points')
    easygui.msgbox('4 lines=800 points')
    easygui.msgbox('If the blocks go up to high the game is over')
    easygui.msgbox('Have Fun')
    
game_start()

class Borderblocks():
    def __init__(self,shape,image):
        self.shape = shape
        self.image = image

class Piece():
    def __init__(self,rect,colour):
        self.rect=rect
        self.colour=colour
def clear_line():
    global clear
    pieces.remove(p)
    clear+=1
    print(clear)
def new_pieces():
    global current_shape, current_shape_x,current_shape_y, shape, dispshape, shape2, dispshape_x, dispshape_y
    shape=shape2
    shape2 = random.randint(0,6)
    current_shape=tetris_shapes [shape]
    current_shape_x=200
    current_shape_y=0
    dispshape = tetris_shapes [shape2]
    dispshape_x=650
    dispshape_y=55

def add_pieces(pieces,current_shape,x,y):
    for r in current_shape:
        y+=20
        x=current_shape_x
        for c in r:
            x+=20
            if c!=0:
                pieces.append(Piece(pygame.Rect(x,y,20,20),c))

def hit_pieces():
    x=current_shape_x
    y=current_shape_y
    for r in current_shape:
        y+=20
        x=current_shape_x
        for c in r:
            x+=20
            if c!=0:
                for p in pieces:
                    if p.rect.colliderect(pygame.Rect(x,y,20,20)):
                        return True
    return False
def hit_border():
    x=current_shape_x
    y=current_shape_y
    for r in current_shape:
        y+=20
        x=current_shape_x
        for c in r:
            x+=20
            if c!=0:
                for b in border:
                    if b.colliderect(pygame.Rect(x,y,20,20)):
                        return True
    return False
### Tetris pieces using arrays ###
tetris_shapes = [
[[1, 1, 1],
 [0, 1, 0]],

[[0, 2, 2],
 [2, 2, 0]],

[[3, 3, 0],
 [0, 3, 3]],

[[4, 0, 0],
 [4, 4, 4]],

[[0, 0, 5],
 [5, 5, 5]],

[[6, 6, 6, 6 ]],

[[7, 7],
 [7, 7]]
]
### Tetris colours using arrays ###
colours=[   [0,0,0],        # black
            [102,0,204],    # purple
            [0,255,0],      # green
            [255,0,0],      # red
            [0,0,255],      # blue
            [255,128,0],    # orange
            [0,255,255],    # sky blue
            [255,255,0],    # yellow
        ]

###randomly generating which piece and their settings ###
new_pieces()
current_shape=tetris_shapes[shape]
current_shape_x=200
current_shape_y=0
gravity=True
border=[]
pieces=[]
ps=[]
### setting borders ###
leftborder = Borderblocks(pygame.Rect(-1,0,60,640),leftside)
bottomborder = Borderblocks(pygame.Rect(-1,579,640,55),bottomside)
rightborder = Borderblocks(pygame.Rect(404,0,403,640),rightside)
borderblocks = (leftborder,bottomborder,rightborder)
score=0
################### MUSIC ###################	
while pygame.mixer.music.get_busy(): pygame.time.Clock().tick(10)
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)


while True:
    gravity=True
    last_shape_x=current_shape_x
    last_shape_y=current_shape_y
### setting reaction for clicks ###
    a=False
    w=False
    s=False
    d=False
### counter for tetris row ###
    tetriscounter = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys=pygame.key.get_pressed()
################### UP KEY PRESS ###################
### rotation of shape ###
        if keys[pygame.K_UP]:
            w=True
            if a==False and s==False and w==True and d==False:
                current_shape=[list(i) for i in zip(*current_shape[::-1])]
                if hit_pieces():
                    current_shape=[list(i) for i in zip(*current_shape[::-1])]
                    current_shape=[list(i) for i in zip(*current_shape[::-1])]
                    current_shape=[list(i) for i in zip(*current_shape[::-1])]
            else:
                pass
################### DOWN KEY PRESS ###################
### Moving Down ###
        if keys[pygame.K_DOWN]:
            s=True
            if a==False and s==True and w==False and d==False:
                current_shape_y+= 20
            else:
                pass
            if hit_pieces():
                  current_shape_y-= 20  
            else:
                score+=1
                gravity=False   
################### LEFT KEY PRESS ###################
### Moving Left ###
        if keys[pygame.K_LEFT]:
            a=True
            if a==True and s==False and w==False and d==False:
                current_shape_x-= 20
            else:
                pass
### if pieces collide ###
            if hit_pieces():
                current_shape_x+= 20
################### RIGHT KEY PRESS ###################
### Moving Right ###
        if keys[pygame.K_RIGHT]:
            d=True
            if a==False and s==False and w==False and d==True:
                current_shape_x=current_shape_x+20
            else:
                pass
### if pieces collide ###
            if hit_pieces():
                current_shape_x-= 20
################### GRAVITY ###################         
### dropping pieces ###
    if gravity ==True and drop_timer>40:
        current_shape_y+= 20
        drop_timer=0
    drop_timer+=1          
################### COLLISION CHECKER ###################
### checking collision with bottom or pieces and adding pieces ###
    if bottom.colliderect(x,y,20,20) :
        add_pieces(pieces,current_shape,last_shape_x,last_shape_y)
        new_pieces()

    if hit_border()==True or hit_pieces()==True:
        add_pieces(pieces,current_shape,last_shape_x,last_shape_y)
        new_pieces()
### right border collision ###
    x = current_shape_x
    y = current_shape_y
    hit_left = pygame.Rect(x,y,20,20)
    if hit_left.colliderect(left) :
        current_shape_x = 40
### Check right edged by checking each piece in shape ###
    for r in current_shape:
        xoffset=0
        for c in r:
            xoffset+=20
            if current_shape_x+xoffset>380:
                current_shape_x = 380-xoffset
################### ROW CLEAR CHECKER ###################
    for row in range(580,0,-20):
        ps=[]
        for p in pieces:
            if p.rect.y==row:
                ps.append(p)
        if len(ps)==17:
            for p in ps:
                clear_line()
            for p in pieces:
                if p.rect.y<row:
                    p.rect.y+=20
            tetrissscounter +=1
### Different score for different amout of row cleared each time ###
            if tetrissscounter == 4:
                score+=800
                tetrissscounter=0
            if tetrissscounter == 3:
                score+=400
                tetrissscounter=0
            if tetrissscounter == 2:
                score+=200
                tetrissscounter=0
            if tetrissscounter == 1:
                score+=100
                tetrissscounter=0
################### GAME OVER CHECKER ###################
    for p in pieces:
        if p.rect.top==20:
            Lose=easygui.buttonbox("Good Try.Do you want to play again","Lose",choices=("Yes","No"))
            if Lose=="Yes":
                new_pieces()
                current_shape=tetris_shapes[shape]
                current_shape_x=200
                current_shape_y=0
                gravity=True
                border=[]
                pieces=[]
                ps=[]
                leftborder = Borderblocks(pygame.Rect(-1,0,60,640),leftside)
                bottomborder = Borderblocks(pygame.Rect(-1,579,640,55),bottomside)
                rightborder = Borderblocks(pygame.Rect(404,0,403,640),rightside)
                borderblocks = (leftborder,bottomborder,rightborder)
                score=0
                x=200
                y=0
                timer = 0
                clear=0
                drop_timer=0
            if Lose=="No":
                pygame.quit()
                sys.exit()
        
   

#draw
    screen.fill(black)
    for b in borderblocks:
        screen.blit(b.image,b.shape)
    x=current_shape_x
    y=current_shape_y
    for r in current_shape:
        y+=20
        x=current_shape_x
        for c in r:
            x+=20
            pygame.draw.rect(screen,colours[c],pygame.Rect(x,y,20,20))

    x8=dispshape_x
    y8=dispshape_y
    for r in dispshape:
        y8+=20
        x8=dispshape_x
        for c in r:
            x8 +=20
            pygame.draw.rect(screen,colours[c],pygame.Rect(x8,y8,20,20))
#drawing pieces
    for p in pieces:
        pygame.draw.rect(screen,colours[p.colour],p.rect)
#drawing bottom border
    for b in border:
        pygame.draw.rect(screen,white,b)
#white grid
    for i in range(60,420,20):
        pygame.draw.line(screen,grey,[i,0],[i,580])
    for i in range(0,600,20):
        pygame.draw.line(screen,grey,[60,i],[400,i])
        
    Score = font.render("SCORE: "+str(score),1,white)
    Next = font.render("Next Piece: ",1,white)
    screen.blit(Score, (550,180))
    screen.blit(Next, (520,70))    
    pygame.display.flip()
    pygame.display.update()
    pygame.time.wait(1)
    
    
