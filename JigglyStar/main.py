import pygame, sys
from pygame.locals import QUIT

start = '''
menu = None
play_rec = pygame.Rect((325, 165, 370, 110))
info_rec = pygame.Rect((325, 280, 370, 110))
quit_rec = pygame.Rect((325, 400, 370, 110))


def load():
    global menu
    menu = pygame.image.load("help.png")
    menu = pygame.transform.scale(menu, (420, 420))


def draw_menu(window):
    global menu
    window.blit(menu, (300, 110))


pygame.init()
window = pygame.display.set_mode((1000, 640))
pygame.display.set_caption('menuzinho')
load()

while True:
    draw_menu(window)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if play_rec.collidepoint(event.pos):
                    exec(easy)
                elif info_rec.collidepoint(event.pos):
                    exec(instruc)
                elif quit_rec.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
    pygame.display.update()
'''

easy = '''

import pygame, sys
from pygame.locals import QUIT

derrota = None
vitoria = None
in_menu = True
playing = True
tileset = None
fundo = None
curr_frame_walk = 0
curr_time = 0
star = None
curr_frame_c = 0
curr_time_c = 0
coin = []
curr_frame_s = 0
curr_time_s = 0
time_control = 0
curr_frame_j = 0
jump_time = 1
fps = 60
colider_c = None
tile_size_game = 80
pos_x = 100
jump_duration = 2
jumping = False
left = False
jumpr_frames = []
jumpl_frames = []
mapa_joguinho = []
clock = pygame.time.Clock()
y = 220
vel_y = 17
star = None
curr_frame_s = 0
curr_time_s = 0
nidoran = None
nidoranD = None
sp = True
spj = True
curr_frameN = 0
curr_timeN = 0
sentidoX = 0.1
pos_xN =0 
win = False
collider_player_s = None
collider_s = None
collider_c = None
collided = False
vex = 0
vey = 0
old_x = 0
old_y = 0
walking = False
heart = None
heart_size = 40
lifes = 5
dead = False
rst = None
curr_time_j = 0
button_width = 180
button_height = 60
button_y = 300
button_x = 410
button_rst_surface = None
button_rst_rect = None
button_start_surface = None
button_start_rect = None
colisão_marcada = False
points = 0
scen = 0
curr_time_life = 0


with open('mapaFacil.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        mapa_joguinho.append(row)

dicionario = {
  "L": (0, tile_size_game, tile_size_game, tile_size_game),
  "Q":  (2*tile_size_game, 2*tile_size_game, tile_size_game, tile_size_game),
  "M": (3* tile_size_game, 2*tile_size_game, tile_size_game, tile_size_game),
}


def load():
    global fundo, jigglypuff_r, jigglypuff_l, jigglypuff_jr, jumpr_frames, jigglypuff_jl, jumpl_frames, star, nidoran, nidoranD, coin, lilfont, heart, rst, button_width, button_height, button_y, button_x, button_rst_surface, button_rst_rect, button_start_surface, button_start_rect, derrota, vitoria

    for i in range(4):
      coin.append(pygame.image.load("gold/" + str(i+1) + ".png"))

    fundo = pygame.image.load("unnamed.jpg")
    fundo = pygame.transform.scale(fundo, (400, 400))
    jigglypuff_r = pygame.image.load("jigglypuff_r.png")
    jigglypuff_l = pygame.image.load("jigglypuff_l.png")
    jigglypuff_jr = pygame.image.load("jigglypuff_jr.png")
    jigglypuff_jl = pygame.image.load("jigglypuff_jl.png")
    star = pygame.image.load("star.png")
    star = pygame.transform.scale(star, (600, 600))
    nidoran = pygame.image.load("nidoran.png")
    nidoranD = pygame.image.load("nidoranD.png")
    lilfont = pygame.font.Font("slkscr.ttf",20)
    vitoria = pygame.image.load("vitoria.jpg")
    vitoria = pygame.transform.scale(vitoria, (1000, 640))
    derrota = pygame.image.load("telaDerrota.jpg")
    derrota = pygame.transform.scale(derrota, (1000, 640))
    heart = pygame.image.load("heart.png")
    heart = pygame.transform.scale(heart, (90,30))
    rst = pygame.image.load("restart.png")
    rst = pygame.transform.scale(rst, (180,60))
    button_rst_surface = pygame.Surface((button_width, button_height))
    button_rst_surface.fill("black")
    button_rst_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    button_start_surface = pygame.Surface((button_width, button_height))
    button_start_surface.fill("black")
    button_start_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    for i in range(6):
        frame = jigglypuff_jr.subsurface((i * 56, 0), (56, 80))
        jumpr_frames.append(frame)

    for i in range(6):
        frame = jigglypuff_jl.subsurface((i * 56, 0), (56, 80))
        jumpl_frames.append(frame)
    jumpl_frames.reverse()

  
def draw_map(window):
    global collider_s, vex, vey, pos_x, y, collider_plx, collider_ply, old_x, old_y, jumping, spj, walking, curr_frame_j, heart_size, collider_c, curr_frame_c, collider_i, collider_player_s, points, lifes, scen, curr_time_life

    collider_player_s = pygame.Rect(pos_x,y,58,65)
    if pos_x > 500:
        pos_x = 500
        scen -= vex
    elif pos_x < 100:
        pos_x = 100
        scen -= vex
        
    window.fill((132, 234, 245))
    for i in range(lifes):
      x = i*heart_size
      window.blit(heart, (x,0), (0,0,30,30))
  
      for i, linha in enumerate(mapa_joguinho):
        for j, char in enumerate(linha):
            if char == "S":
                window.blit(star, (j * tile_size_game + scen, i * tile_size_game),
                            (75 * curr_frame_s, 360, 75, 75))
                collider_s = pygame.Rect(j*tile_size_game + scen, i*tile_size_game,tile_size_game,tile_size_game)
                
            elif char == "I":
              if sp:
                window.blit(nidoranD, (j * tile_size_game + pos_xN, i * tile_size_game+47), (36 * curr_frameN, 1, 37, 33))
                collider_i = pygame.Rect(j*tile_size_game + pos_xN, i*tile_size_game+47,37, 33)
                if collider_player_s.colliderect(collider_i):
                    if curr_time_life > 500:
                        lifes -= 1
                        curr_time_life = 0
                    else:
                        curr_time_life += 10
                  
              else:
                window.blit(nidoran, (j * tile_size_game + pos_xN, i * tile_size_game+47), (35 * curr_frameN, 60, 34, 32))
                collider_i = pygame.Rect(j*tile_size_game + pos_xN, i*tile_size_game+47,34,32)
                if collider_player_s.colliderect(collider_i):
                    if curr_time_life > 500:
                        lifes -= 1
                        curr_time_life = 0
                    else:
                        curr_time_life += 10
            elif char in dicionario:
                window.blit(fundo, (j * tile_size_game + scen, i * tile_size_game), dicionario[char])
            collider_scen = pygame.Rect(j*tile_size_game + scen, i*tile_size_game, tile_size_game, tile_size_game)
            collider_plx = pygame.Rect(pos_x + vex, y+ 10, 58, 55)
            collider_ply = pygame.Rect(pos_x, y + 10 + vey, 58, 55)
            
            if char != "X" and char != "S" and char != "L" and char != "I":
                if char == "C":
                    window.blit(coin[curr_frame_c],  (j * tile_size_game + scen, i * tile_size_game))
                    collider_c = pygame.Rect(j*tile_size_game + scen, i*tile_size_game,32,32)
                    if collider_player_s.colliderect(collider_c):
                        points += 10
                        mapa_joguinho[i][j] = "X"
                             
                elif collider_plx.colliderect(collider_scen):
                    collided = True
                    pos_x = old_x
                    vex = 0
                elif collider_ply.colliderect(collider_scen):
                    collided = True
                    y = old_y
                    vey = 0
                    jumping = False
                else:
                    collided = False
            
                text = lilfont.render("LEVEL ONE: EASY", True, "black")
                window.blit(text, (200,5))
                
                text = lilfont.render("score: " + str(points), True, "black")
                window.blit(text, (0,50))
                resto = 50 - points
                if resto > 0:
                    text = lilfont.render("score needed for next level: " + str(resto), True, "black")
                else:
                    text = lilfont.render("catch the star", True, "black")
                window.blit(text, (0,75))
                     
    if walking and not jumping:
        if spj:
            window.blit(jigglypuff_r, (pos_x, y),(58 * curr_frame_walk, 0, 58, 65))
        else:
            window.blit(jigglypuff_l, (pos_x, y),(58 * curr_frame_walk, 0, 58, 65))
    else:
        if jumping:
            if left:
                window.blit(jumpl_frames[curr_frame_j], (pos_x, y))
            else:
                window.blit(jumpr_frames[curr_frame_j], (pos_x, y))
        else:
            if left:
                window.blit(jumpl_frames[3], (pos_x, y))
            else: 
                window.blit(jumpr_frames[3], (pos_x, y))
    
def update(dt):
    global curr_time,curr_time_c, curr_frame_c, pos_x, curr_frame_walk, curr_frame_s, curr_time_s, curr_frameN, curr_timeN, sp, sentidoX, pos_xN, curr_frameN,curr_frameN, curr_timeN, sentidoX, curr_frameN, curr_timeN, sentidoX, old_x, old_y, vex, vey, y, spj, walking, jumping, curr_frame_j, curr_time_j, lifes

    curr_time_c = curr_time_c + dt
    if curr_time_c > 100:
        curr_frame_c += 1
        curr_time_c = 0
        if curr_frame_c > 3: 
          curr_frame_c = 0

    old_x = pos_x
    old_y = y

    y += vey
    pos_x += vex
    vey += 1*dt/100
    curr_time_s = curr_time_s + dt

    if curr_time_s > 100:
        curr_frame_s += 1
        curr_time_s = 0
        if curr_frame_s > 2:
            curr_frame_s = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        walking = True
        spj = True
        vex = 0.1*dt
        if pos_x > 2000:
            pos_x = 2000
        curr_time = curr_time + dt
        if curr_time > 150:
            curr_frame_walk += 1
            curr_time = 0
            if curr_frame_walk > 7:
                curr_frame_walk = 0

    elif keys[pygame.K_LEFT]:
        walking = True
        spj = False
        vex = -0.1 * dt
        if pos_x < 0:
            pos_x = 0
        curr_time = curr_time + dt
        if curr_time > 150:
            curr_frame_walk -= 1
            curr_time = 0
            if curr_frame_walk < 0:
                curr_frame_walk = 7

    else:
        vex = 0
        walking = False
    if keys[pygame.K_UP] and not jumping:
        vey = -7.5
        jumping = True

    curr_timeN = curr_timeN + dt
    if curr_timeN > 100:
        curr_frameN += 1
        curr_timeN = 0
        if curr_frameN > 3:
            curr_frameN = 0
            

    pos_xN += sentidoX * dt
    if pos_xN - scen >= (203):
        sp = False
        sentidoX = -0.1

    if pos_xN - scen <= 0:
        sp = True
        sentidoX = 0.1

    if jumping:
        curr_time_j = curr_time_j + dt
        if curr_time_j > 600:
            curr_frame_j += 1
            curr_time_j = 0
            if curr_frame_j > 3:
                curr_frame_j = 0
    else:
        curr_frame_j = 0
        curr_time_j = 0

pygame.init()
window = pygame.display.set_mode((1000, 640))
pygame.display.set_caption('LEVEL ONE: EASY MODE')
load()

while playing: 
    while not dead:
        if not win:
            draw_map(window)
            clock.tick(60)
            dt = clock.get_time()
            update(dt)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        left = True
                    elif event.key == pygame.K_RIGHT:
                        left = False
            if collider_player_s.colliderect(collider_s):
                if points >= 50:
                    win = True
                
        else:
            exec(medium)

        if lifes <= 0 or y > 580:
            dead = True
        pygame.display.update()
        
    while dead:
        window.fill("white")
        window.blit(derrota, (-8, -10))
        window.blit(rst, button_rst_rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if button_rst_rect.collidepoint(event.pos):
                    lifes = 5
                    dead = False
                    pos_x = 100
                    y = 220
                    points = 0
                    scen = 0
                    mapa_joguinho = []
                    with open('mapaFacil.txt', 'r') as file:
                        for line in file:
                            row = list(line.strip())
                            mapa_joguinho.append(row)
            

        pygame.display.update()

'''

medium = '''
import pygame, sys
from pygame.locals import QUIT

derrota = None
vitoria = None
in_menu = True
playing = True
tileset = None
fundo = None
curr_frame_walk = 0
curr_time = 0
star = None
curr_frame_c = 0
curr_time_c = 0
coin = []
curr_frame_s = 0
curr_time_s = 0
time_control = 0
curr_frame_j = 0
jump_time = 1
fps = 60
colider_c = None
tile_size_game = 80
pos_x = 100
jump_duration = 2
jumping = False
left = False
jumpr_frames = []
jumpl_frames = []
mapa_joguinho = []
clock = pygame.time.Clock()
y = 220
vel_y = 17
star = None
curr_frame_s = 0
curr_time_s = 0
nidoran = None
nidoranD = None
sp = True
spj = True
curr_frameN = 0
curr_timeN = 0
sentidoX = 0.1
pos_xN =0 
win = False
collider_player_s = None
collider_s = None
collider_c = None
collided = False
vex = 0
vey = 0
old_x = 0
old_y = 0
walking = False
heart = None
heart_size = 40
lifes = 4
dead = False
rst = None
curr_time_j = 0
button_width = 180
button_height = 60
button_y = 300
button_x = 410
button_rst_surface = None
button_rst_rect = None
button_start_surface = None
button_start_rect = None
colisão_marcada = False
points = 0
scen = 0
curr_time_life = 0


with open('mapaMedio.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        mapa_joguinho.append(row)

dicionario = {
  "L": (0, tile_size_game, tile_size_game, tile_size_game),
  "G":  (0, 4*tile_size_game, tile_size_game, tile_size_game),
  "E": (4* tile_size_game, 0, tile_size_game, tile_size_game),
}


def load():
    global fundo, jigglypuff_r, jigglypuff_l, jigglypuff_jr, jumpr_frames, jigglypuff_jl, jumpl_frames, star, nidoran, nidoranD, coin, lilfont, heart, rst, button_width, button_height, button_y, button_x, button_rst_surface, button_rst_rect, button_start_surface, button_start_rect, derrota, vitoria

    for i in range(4):
      coin.append(pygame.image.load("gold/" + str(i+1) + ".png"))

    fundo = pygame.image.load("unnamed.jpg")
    fundo = pygame.transform.scale(fundo, (400, 400))
    jigglypuff_r = pygame.image.load("jigglypuff_r.png")
    jigglypuff_l = pygame.image.load("jigglypuff_l.png")
    jigglypuff_jr = pygame.image.load("jigglypuff_jr.png")
    jigglypuff_jl = pygame.image.load("jigglypuff_jl.png")
    star = pygame.image.load("star.png")
    star = pygame.transform.scale(star, (600, 600))
    nidoran = pygame.image.load("nidoran.png")
    nidoranD = pygame.image.load("nidoranD.png")
    lilfont = pygame.font.Font("slkscr.ttf",20)
    vitoria = pygame.image.load("vitoria.jpg")
    vitoria = pygame.transform.scale(vitoria, (1000, 640))
    derrota = pygame.image.load("telaDerrota.jpg")
    derrota = pygame.transform.scale(derrota, (1000, 640))
    heart = pygame.image.load("heart.png")
    heart = pygame.transform.scale(heart, (90,30))
    rst = pygame.image.load("restart.png")
    rst = pygame.transform.scale(rst, (180,60))
    button_rst_surface = pygame.Surface((button_width, button_height))
    button_rst_surface.fill("black")
    button_rst_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    button_start_surface = pygame.Surface((button_width, button_height))
    button_start_surface.fill("black")
    button_start_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    for i in range(6):
        frame = jigglypuff_jr.subsurface((i * 56, 0), (56, 80))
        jumpr_frames.append(frame)

    for i in range(6):
        frame = jigglypuff_jl.subsurface((i * 56, 0), (56, 80))
        jumpl_frames.append(frame)
    jumpl_frames.reverse()

  
def draw_map(window):
    global collider_s, vex, vey, pos_x, y, collider_plx, collider_ply, old_x, old_y, jumping, spj, walking, curr_frame_j, heart_size, collider_c, curr_frame_c, collider_i, collider_player_s, points, lifes, scen, curr_time_life

    collider_player_s = pygame.Rect(pos_x,y,58,65)
    if pos_x > 500:
        pos_x = 500
        scen -= vex
    elif pos_x < 100:
        pos_x = 100
        scen -= vex
        
    window.fill((132, 234, 245))
    for i in range(lifes):
      x = i*heart_size
      window.blit(heart, (x,0), (0,0,30,30))
  
      for i, linha in enumerate(mapa_joguinho):
        for j, char in enumerate(linha):
            if char == "S":
                window.blit(star, (j * tile_size_game + scen, i * tile_size_game),
                            (75 * curr_frame_s, 360, 75, 75))
                collider_s = pygame.Rect(j*tile_size_game + scen, i*tile_size_game,tile_size_game,tile_size_game)
            elif char == "I":
              if sp:
                window.blit(nidoranD, (j * tile_size_game + pos_xN, i * tile_size_game+47), (36 * curr_frameN, 1, 37, 33))
                collider_i = pygame.Rect(j*tile_size_game + pos_xN, i*tile_size_game+47,37, 33)
                if collider_player_s.colliderect(collider_i):
                    if curr_time_life > 500:
                        lifes -= 1
                        curr_time_life = 0
                    else:
                        curr_time_life += 10
                  
              else:
                window.blit(nidoran, (j * tile_size_game + pos_xN, i * tile_size_game+47), (35 * curr_frameN, 60, 34, 32))
                collider_i = pygame.Rect(j*tile_size_game + pos_xN, i*tile_size_game+47,34,32)
                if collider_player_s.colliderect(collider_i):
                    if curr_time_life > 500:
                        lifes -= 1
                        curr_time_life = 0
                    else:
                        curr_time_life += 10
            elif char in dicionario:
                window.blit(fundo, (j * tile_size_game + scen, i * tile_size_game), dicionario[char])
            collider_scen = pygame.Rect(j*tile_size_game + scen, i*tile_size_game, tile_size_game, tile_size_game)
            collider_plx = pygame.Rect(pos_x + vex, y+ 10, 58, 55)
            collider_ply = pygame.Rect(pos_x, y + 10 + vey, 58, 55)
            
            if char != "X" and char != "S" and char != "L" and char != "I":
                if char == "C":
                    window.blit(coin[curr_frame_c],  (j * tile_size_game + scen, i * tile_size_game))
                    collider_c = pygame.Rect(j*tile_size_game + scen, i*tile_size_game,32,32)
                    if collider_player_s.colliderect(collider_c):
                        points += 10
                        mapa_joguinho[i][j] = "X"
                             
                elif collider_plx.colliderect(collider_scen):
                    collided = True
                    pos_x = old_x
                    vex = 0
                elif collider_ply.colliderect(collider_scen):
                    collided = True
                    y = old_y
                    vey = 0
                    jumping = False
                else:
                    collided = False

                text = lilfont.render("LEVEL TWO: MEDIUM", True, "black")
                window.blit(text, (200,5))
                
                text = lilfont.render("score: " + str(points), True, "black")
                window.blit(text, (0,50))
                resto = 50 - points
                if resto > 0:
                    text = lilfont.render("score needed for next level: " + str(resto), True, "black")
                else:
                    text = lilfont.render("catch the star", True, "black")
                window.blit(text, (0,75))
                     
    if walking and not jumping:
        if spj:
            window.blit(jigglypuff_r, (pos_x, y),(58 * curr_frame_walk, 0, 58, 65))
        else:
            window.blit(jigglypuff_l, (pos_x, y),(58 * curr_frame_walk, 0, 58, 65))
    else:
        if jumping:
            if left:
                window.blit(jumpl_frames[curr_frame_j], (pos_x, y))
            else:
                window.blit(jumpr_frames[curr_frame_j], (pos_x, y))
        else:
            if left:
                window.blit(jumpl_frames[3], (pos_x, y))
            else: 
                window.blit(jumpr_frames[3], (pos_x, y))
    
def update(dt):
    global curr_time,curr_time_c, curr_frame_c, pos_x, curr_frame_walk, curr_frame_s, curr_time_s, curr_frameN, curr_timeN, sp, sentidoX, pos_xN, curr_frameN,curr_frameN, curr_timeN, sentidoX, curr_frameN, curr_timeN, sentidoX, old_x, old_y, vex, vey, y, spj, walking, jumping, curr_frame_j, curr_time_j, lifes

    curr_time_c = curr_time_c + dt
    if curr_time_c > 100:
        curr_frame_c += 1
        curr_time_c = 0
        if curr_frame_c > 3: 
          curr_frame_c = 0

    old_x = pos_x
    old_y = y

    y += vey
    pos_x += vex
    vey += 1*dt/100
    curr_time_s = curr_time_s + dt

    if curr_time_s > 100:
        curr_frame_s += 1
        curr_time_s = 0
        if curr_frame_s > 2:
            curr_frame_s = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        walking = True
        spj = True
        vex = 0.1*dt
        if pos_x > 2000:
            pos_x = 2000
        curr_time = curr_time + dt
        if curr_time > 150:
            curr_frame_walk += 1
            curr_time = 0
            if curr_frame_walk > 7:
                curr_frame_walk = 0

    elif keys[pygame.K_LEFT]:
        walking = True
        spj = False
        vex = -0.1 * dt
        if pos_x < 0:
            pos_x = 0
        curr_time = curr_time + dt
        if curr_time > 150:
            curr_frame_walk -= 1
            curr_time = 0
            if curr_frame_walk < 0:
                curr_frame_walk = 7

    else:
        vex = 0
        walking = False
    if keys[pygame.K_UP] and not jumping:
        vey = -7.5
        jumping = True

    curr_timeN = curr_timeN + dt
    if curr_timeN > 100:
        curr_frameN += 1
        curr_timeN = 0
        if curr_frameN > 3:
            curr_frameN = 0
            

    pos_xN += sentidoX * dt
    if pos_xN - scen >= (203):
        sp = False
        sentidoX = -0.1

    if pos_xN - scen <= 0:
        sp = True
        sentidoX = 0.1

    if jumping:
        curr_time_j = curr_time_j + dt
        if curr_time_j > 600:
            curr_frame_j += 1
            curr_time_j = 0
            if curr_frame_j > 3:
                curr_frame_j = 0
    else:
        curr_frame_j = 0
        curr_time_j = 0

pygame.init()
window = pygame.display.set_mode((1000, 640))
pygame.display.set_caption('LEVEL TWO: MEDIUM')
load()

while playing: 
    while not dead:
        if not win:
            draw_map(window)
            clock.tick(60)
            dt = clock.get_time()
            update(dt)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        left = True
                    elif event.key == pygame.K_RIGHT:
                        left = False
            if collider_player_s.colliderect(collider_s):
                if points >= 50:
                    win = True
                
        else:
            exec(hard)

        if lifes <= 0 or y > 580:
            dead = True
        pygame.display.update()
        
    while dead:
        window.fill("white")
        window.blit(derrota, (-8, -10))
        window.blit(rst, button_rst_rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if button_rst_rect.collidepoint(event.pos):
                    lifes = 4
                    dead = False
                    pos_x = 100
                    y = 220
                    points = 0
                    scen = 0
                    mapa_joguinho = []
                    with open('mapaMedio.txt', 'r') as file:
                        for line in file:
                            row = list(line.strip())
                            mapa_joguinho.append(row)
            
        pygame.display.update() 

'''
hard = '''
import pygame, sys
from pygame.locals import QUIT

derrota = None
vitoria = None
in_menu = True
playing = True
tileset = None
fundo = None
curr_frame_walk = 0
curr_time = 0
star = None
curr_frame_c = 0
curr_time_c = 0
coin = []
curr_frame_s = 0
curr_time_s = 0
time_control = 0
curr_frame_j = 0
jump_time = 1
fps = 60
colider_c = None
tile_size_game = 80
pos_x = 100
jump_duration = 2
jumping = False
left = False
jumpr_frames = []
jumpl_frames = []
mapa_joguinho = []
clock = pygame.time.Clock()
y = 220
vel_y = 17
star = None
curr_frame_s = 0
curr_time_s = 0
nidoran = None
nidoranD = None
sp = True
spj = True
curr_frameN = 0
curr_timeN = 0
sentidoX = 0.1
pos_xN =0 
win = False
collider_player_s = None
collider_s = None
collider_c = None
collided = False
vex = 0
vey = 0
old_x = 0
old_y = 0
walking = False
heart = None
heart_size = 40
lifes = 3
dead = False
rst = None
curr_time_j = 0
button_width = 180
button_height = 60
button_y = 300
button_x = 410
button_rst_surface = None
button_rst_rect = None
button_start_surface = None
button_start_rect = None
colisão_marcada = False
points = 0
scen = 0
curr_time_life = 0


with open('mapa.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        mapa_joguinho.append(row)

dicionario = {
    "T": (0, 2 * tile_size_game, tile_size_game, tile_size_game),
    "L": (0, tile_size_game, tile_size_game, tile_size_game),
    "P": (1 * tile_size_game, 1 * tile_size_game, tile_size_game, tile_size_game),
}


def load():
    global fundo, jigglypuff_r, jigglypuff_l, jigglypuff_jr, jumpr_frames, jigglypuff_jl, jumpl_frames, star, nidoran, nidoranD, coin, lilfont, heart, rst, button_width, button_height, button_y, button_x, button_rst_surface, button_rst_rect, button_start_surface, button_start_rect, derrota, vitoria

    for i in range(4):
      coin.append(pygame.image.load("gold/" + str(i+1) + ".png"))

    fundo = pygame.image.load("unnamed.jpg")
    fundo = pygame.transform.scale(fundo, (400, 400))
    jigglypuff_r = pygame.image.load("jigglypuff_r.png")
    jigglypuff_l = pygame.image.load("jigglypuff_l.png")
    jigglypuff_jr = pygame.image.load("jigglypuff_jr.png")
    jigglypuff_jl = pygame.image.load("jigglypuff_jl.png")
    star = pygame.image.load("star.png")
    star = pygame.transform.scale(star, (600, 600))
    nidoran = pygame.image.load("nidoran.png")
    nidoranD = pygame.image.load("nidoranD.png")
    lilfont = pygame.font.Font("slkscr.ttf",20)
    vitoria = pygame.image.load("vitoria.jpg")
    vitoria = pygame.transform.scale(vitoria, (1000, 640))
    derrota = pygame.image.load("telaDerrota.jpg")
    derrota = pygame.transform.scale(derrota, (1000, 640))
    heart = pygame.image.load("heart.png")
    heart = pygame.transform.scale(heart, (90,30))
    rst = pygame.image.load("restart.png")
    rst = pygame.transform.scale(rst, (180,60))
    button_rst_surface = pygame.Surface((button_width, button_height))
    button_rst_surface.fill("black")
    button_rst_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    button_start_surface = pygame.Surface((button_width, button_height))
    button_start_surface.fill("black")
    button_start_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    for i in range(6):
        frame = jigglypuff_jr.subsurface((i * 56, 0), (56, 80))
        jumpr_frames.append(frame)

    for i in range(6):
        frame = jigglypuff_jl.subsurface((i * 56, 0), (56, 80))
        jumpl_frames.append(frame)
    jumpl_frames.reverse()

  
def draw_map(window):
    global collider_s, vex, vey, pos_x, y, collider_plx, collider_ply, old_x, old_y, jumping, spj, walking, curr_frame_j, heart_size, collider_c, curr_frame_c, collider_i, collider_player_s, points, lifes, scen, curr_time_life

    collider_player_s = pygame.Rect(pos_x,y,58,65)
    if pos_x > 500:
        pos_x = 500
        scen -= vex
    elif pos_x < 100:
        pos_x = 100
        scen -= vex
        
    window.fill((132, 234, 245))
    for i in range(lifes):
      x = i*heart_size
      window.blit(heart, (x,0), (0,0,30,30))
  
      for i, linha in enumerate(mapa_joguinho):
        for j, char in enumerate(linha):
            if char == "S":
                window.blit(star, (j * tile_size_game + scen, i * tile_size_game),
                            (75 * curr_frame_s, 360, 75, 75))
                collider_s = pygame.Rect(j*tile_size_game + scen, i*tile_size_game,tile_size_game,tile_size_game)
                
            elif char == "I":
              if sp:
                window.blit(nidoranD, (j * tile_size_game + pos_xN, i * tile_size_game+47), (36 * curr_frameN, 1, 37, 33))
                collider_i = pygame.Rect(j*tile_size_game + pos_xN, i*tile_size_game+47,37, 33)
                if collider_player_s.colliderect(collider_i):
                    if curr_time_life > 500:
                        lifes -= 1
                        curr_time_life = 0
                    else:
                        curr_time_life += 10
                  
              else:
                window.blit(nidoran, (j * tile_size_game + pos_xN, i * tile_size_game+47), (35 * curr_frameN, 60, 34, 32))
                collider_i = pygame.Rect(j*tile_size_game + pos_xN, i*tile_size_game+47,34,32)
                if collider_player_s.colliderect(collider_i):
                    if curr_time_life > 500:
                        lifes -= 1
                        curr_time_life = 0
                    else:
                        curr_time_life += 10
            elif char in dicionario:
                window.blit(fundo, (j * tile_size_game + scen, i * tile_size_game), dicionario[char])
            collider_scen = pygame.Rect(j*tile_size_game + scen, i*tile_size_game, tile_size_game, tile_size_game)
            collider_plx = pygame.Rect(pos_x + vex, y+ 10, 58, 55)
            collider_ply = pygame.Rect(pos_x, y + 10 + vey, 58, 55)
            
            if char != "X" and char != "S" and char != "L" and char != "I":
                if char == "C":
                    window.blit(coin[curr_frame_c],  (j * tile_size_game + scen, i * tile_size_game))
                    collider_c = pygame.Rect(j*tile_size_game + scen, i*tile_size_game,32,32)
                    if collider_player_s.colliderect(collider_c):
                        points += 10
                        mapa_joguinho[i][j] = "X"
                             
                elif collider_plx.colliderect(collider_scen):
                    collided = True
                    pos_x = old_x
                    vex = 0
                elif collider_ply.colliderect(collider_scen):
                    collided = True
                    y = old_y
                    vey = 0
                    jumping = False
                else:
                    collided = False

                text = lilfont.render("LEVEL THREE: HARDCORE", True, "black")
                window.blit(text, (200,5))

                text = lilfont.render("score: " + str(points), True, "black")
                window.blit(text, (0,50))
                resto = 50 - points
                if resto > 0:
                    text = lilfont.render("score needed for next level: " + str(resto), True, "black")
                else:
                    text = lilfont.render("catch the star", True, "black")
                window.blit(text, (0,75))
                     
    if walking and not jumping:
        if spj:
            window.blit(jigglypuff_r, (pos_x, y),(58 * curr_frame_walk, 0, 58, 65))
        else:
            window.blit(jigglypuff_l, (pos_x, y),(58 * curr_frame_walk, 0, 58, 65))
    else:
        if jumping:
            if left:
                window.blit(jumpl_frames[curr_frame_j], (pos_x, y))
            else:
                window.blit(jumpr_frames[curr_frame_j], (pos_x, y))
        else:
            if left:
                window.blit(jumpl_frames[3], (pos_x, y))
            else: 
                window.blit(jumpr_frames[3], (pos_x, y))
    
def update(dt):
    global curr_time,curr_time_c, curr_frame_c, pos_x, curr_frame_walk, curr_frame_s, curr_time_s, curr_frameN, curr_timeN, sp, sentidoX, pos_xN, curr_frameN,curr_frameN, curr_timeN, sentidoX, curr_frameN, curr_timeN, sentidoX, old_x, old_y, vex, vey, y, spj, walking, jumping, curr_frame_j, curr_time_j, lifes

    curr_time_c = curr_time_c + dt
    if curr_time_c > 100:
        curr_frame_c += 1
        curr_time_c = 0
        if curr_frame_c > 3: 
          curr_frame_c = 0

    old_x = pos_x
    old_y = y

    y += vey
    pos_x += vex
    vey += 1*dt/100
    curr_time_s = curr_time_s + dt

    if curr_time_s > 100:
        curr_frame_s += 1
        curr_time_s = 0
        if curr_frame_s > 2:
            curr_frame_s = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        walking = True
        spj = True
        vex = 0.1*dt
        if pos_x > 2000:
            pos_x = 2000
        curr_time = curr_time + dt
        if curr_time > 150:
            curr_frame_walk += 1
            curr_time = 0
            if curr_frame_walk > 7:
                curr_frame_walk = 0

    elif keys[pygame.K_LEFT]:
        walking = True
        spj = False
        vex = -0.1 * dt
        if pos_x < 0:
            pos_x = 0
        curr_time = curr_time + dt
        if curr_time > 150:
            curr_frame_walk -= 1
            curr_time = 0
            if curr_frame_walk < 0:
                curr_frame_walk = 7

    else:
        vex = 0
        walking = False
    if keys[pygame.K_UP] and not jumping:
        vey = -7.5
        jumping = True

    curr_timeN = curr_timeN + dt
    if curr_timeN > 100:
        curr_frameN += 1
        curr_timeN = 0
        if curr_frameN > 3:
            curr_frameN = 0
            

    pos_xN += sentidoX * dt
    if pos_xN - scen >= (203):
        sp = False
        sentidoX = -0.1

    if pos_xN - scen <= 0:
        sp = True
        sentidoX = 0.1

    if jumping:
        curr_time_j = curr_time_j + dt
        if curr_time_j > 600:
            curr_frame_j += 1
            curr_time_j = 0
            if curr_frame_j > 3:
                curr_frame_j = 0
    else:
        curr_frame_j = 0
        curr_time_j = 0

pygame.init()
window = pygame.display.set_mode((1000, 640))
pygame.display.set_caption('LEVEL THREE: HARDCORE')
load()

while playing: 
    while not dead:
        if not win:
            draw_map(window)
            clock.tick(60)
            dt = clock.get_time()
            update(dt)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        left = True
                    elif event.key == pygame.K_RIGHT:
                        left = False
            if collider_player_s.colliderect(collider_s):
                if points >= 50:
                    win = True
                
        else:
            window.blit(vitoria, (0, 0))
            button_rect = pygame.Rect(button_x, button_y+250, button_width, button_height)
            window.blit(rst, button_rect)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        exec(start)

        if lifes <= 0 or y > 580:
            dead = True
        pygame.display.update()
        
    while dead:
        window.fill("white")
        window.blit(derrota, (-8, -10))
        window.blit(rst, button_rst_rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if button_rst_rect.collidepoint(event.pos):
                    lifes = 3
                    dead = False
                    pos_x = 100
                    y = 220
                    points = 0
                    scen = 0
                    mapa_joguinho = []
                    with open('mapa.txt', 'r') as file:
                        for line in file:
                            row = list(line.strip())
                            mapa_joguinho.append(row)
            

        pygame.display.update()      

'''
instruc = '''

import pygame, sys
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((1000, 640))
pygame.display.set_caption('help')

inst = pygame.image.load("inst.jpg")
inst = pygame.transform.scale(inst, (1000, 640))

while True:
    window.blit(inst, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    exec(easy)
            elif event.key == pygame.K_m:
                    exec(start)
    pygame.display.update()
    

'''

menu = None
play_rec = pygame.Rect((325, 165, 370, 110))
info_rec = pygame.Rect((325, 280, 370, 110))
quit_rec = pygame.Rect((325, 400, 370, 110))


def load():
    global menu
    menu = pygame.image.load("help.png")
    menu = pygame.transform.scale(menu, (420, 420))


def draw_menu(window):
    global menu
    window.blit(menu, (300, 110))


pygame.init()
window = pygame.display.set_mode((1000, 640))
pygame.display.set_caption('menuzinho')
load()

while True:
    draw_menu(window)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if play_rec.collidepoint(event.pos):
                    exec(easy)
                elif info_rec.collidepoint(event.pos):
                    exec(instruc)
                elif quit_rec.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
    pygame.display.update()