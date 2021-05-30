import pygame, sys, random, time, os
pygame.init()
os.listdir()

#název
pygame.display.set_caption("RƎTRO RACING")

#okno
sirka_okna = 800
vyska_okna = 600
okno = pygame.display.set_mode((sirka_okna, vyska_okna))


okno.fill((0,0,0))
fullscreen = False

#čas
hodiny = pygame.time.Clock()

#soundtrack
pygame.mixer.music.load("soundtrack.mp3")
pygame.mixer.music.set_volume(0.4)

#načíst obrázky
fotoauta = pygame.image.load("obrazky/auto.png") #RED
fotoauta2 = pygame.image.load("obrazky/auto2.png") #GREEN
fotoauta3 = pygame.image.load("obrazky/auto3.png") #BLUE
fotoauta4 = pygame.image.load("obrazky/auto4.png") #YELLOW
fotoauta5 = pygame.image.load("obrazky/auto5.png") #BLACK
fotoauta6 = pygame.image.load("obrazky/auto6.png") #WHITE

#menu obrázky
menufoto = pygame.image.load("menu/RetroRacingMENU.png") #HLAVNÍ MENU

pausefoto = pygame.image.load("menu/PauseMenu.png") #PAUSE MENU
pausetext = pygame.image.load("obrazky/Pause.png")
pausetext2 = pygame.image.load("obrazky/Pause2.png")

optionsfoto = pygame.image.load("menu/OptionsMenu.png") #OPTIONS MENU
sound = pygame.image.load("menu/sound.png")
sound2 = pygame.image.load("menu/sound2.png")
zvukfoto = pygame.image.load("menu/zvuk.png")
nezvukfoto = pygame.image.load("menu/nezvuk.png")
fullscreenfoto = pygame.image.load("menu/fullscreen.png")
fullscreenfoto2 = pygame.image.load("menu/fullscreen2.png")
back = pygame.image.load("menu/back_button.png")
back2 = pygame.image.load("menu/back_button2.png")

play = pygame.image.load("menu/playbutton.png")
options = pygame.image.load("menu/optionsbutton.png")
quit1 = pygame.image.load("menu/quitbutton.png")
continue1 = pygame.image.load("menu/continue.png")
restart = pygame.image.load("menu/restart.png")

play2 = pygame.image.load("menu/playbutton2.png")
options2 = pygame.image.load("menu/optionsbutton2.png")
quit2 = pygame.image.load("menu/quitbutton2.png")
continue2 = pygame.image.load("menu/continue2.png")
restart2 = pygame.image.load("menu/restart2.png")

#ostatní
trava1 = pygame.image.load("obrazky/trava.png")
trava2 = pygame.image.load("obrazky/trava.png")
trava2 = pygame.transform.flip(trava2, 180, 0)

silnice = pygame.image.load("obrazky/silnicepre.png")

ndy = pygame.image.load("menu/notdoneyet.png")

#crash
crashfoto = pygame.image.load("obrazky/crashed.png")
crashexploze = pygame.image.load("obrazky/crash.png")

#ikona
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


# # # # # # # # # # # # # # # # 

#auta
sirka = 300 // 4
vyska = 450 // 4
fotoauta = pygame.transform.scale(fotoauta, (sirka, vyska))
fotoauta2 = pygame.transform.scale(fotoauta2, (sirka, vyska))
fotoauta3 = pygame.transform.scale(fotoauta3, (sirka, vyska))
fotoauta4 = pygame.transform.scale(fotoauta4, (sirka, vyska))
fotoauta5 = pygame.transform.scale(fotoauta5, (sirka, vyska))
fotoauta6 = pygame.transform.scale(fotoauta6, (sirka, vyska))

pausetext_mensi = pygame.transform.scale(pausetext, (62, 57))
pausetext2_mensi = pygame.transform.scale(pausetext2, (62, 57))
zvukfoto_mensi = pygame.transform.scale(zvukfoto, (35, 45))
nezvukfoto_mensi = pygame.transform.scale(nezvukfoto, (35, 45))

fotoauta2flip = pygame.transform.flip(fotoauta2, False, True)
fotoauta3flip = pygame.transform.flip(fotoauta3, False, True)
fotoauta4flip = pygame.transform.flip(fotoauta4, False, True)
fotoauta5flip = pygame.transform.flip(fotoauta5, False, True)
fotoauta6flip = pygame.transform.flip(fotoauta6, False, True)

#MENU
def mainmenu():
    menu = True
    
    zvoleno = "start"

    while menu:
        udalosti = pygame.event.get()
        for udalost in udalosti:
            if udalost.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if udalost.type==pygame.KEYDOWN:
                if udalost.key==pygame.K_UP:
                    zvoleno="start"
                elif udalost.key==pygame.K_DOWN:
                    zvoleno="quit"
                if udalost.key==pygame.K_RETURN:
                    if zvoleno=="start":
                        print("Start")
                    if zvoleno=="quit":
                        pygame.quit()
                        quit()
        
        okno.blit(menufoto, (0,0))
        
        okno.blit(play, (550, 390))
        okno.blit(options, (510, 440))
        okno.blit(quit1, (550, 490))
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        
        if mouse[0] > 555 and mouse[0] < 670 and mouse[1] > 395 and mouse[1] < 435:
            okno.blit(play2, (550, 390))
            if click == (True, False, False):
                gameloop()
            
        if mouse[0] > 513 and mouse[0] < 711 and mouse[1] > 443 and mouse[1] < 483:
            okno.blit(options2, (510, 440))
            if click == (True, False, False):
                optionsmenu()
            
        if mouse[0] > 553 and mouse[0] < 662 and mouse[1] > 493 and mouse[1] < 533:
            okno.blit(quit2, (550, 490))
            if click == (True, False, False):
                pygame.quit()
                sys.exit()
        
        
        pygame.display.update()
  
def fullscreen():
    fullscreen = False
    fullscreen = not fullscreen
    if fullscreen:
        pygame.display.set_mode((sirka_okna, vyska_okna), pygame.FULLSCREEN)
    else:
        pygame.display.set_mode((sirka_okna, vyska_okna))


def optionsmenu():
    options = True
    
    while options:
        udalosti = pygame.event.get()
        for udalost in udalosti:
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if udalost.type == pygame.KEYDOWN:
                if udalost.key == pygame.K_ESCAPE:
                    options = False
            
        okno.blit(optionsfoto, (0,0))
        #okno.blit(sound, (123, 249))
        #okno.blit(fullscreenfoto, (105,298))
        #okno.blit(zvukfoto_mensi, (228,238))
        #okno.blit(nezvukfoto_mensi, (268, 238))
        okno.blit(back, (20,460))
        okno.blit(ndy, (38, 220))
            
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
                
        if mouse[0] > 26 and mouse[0] < 95 and mouse[1] > 469 and mouse[1] < 550:
            okno.blit(back2, (20,460))
            if click == (True, False, False):
                options = False 
            
            
        pygame.display.update()
        

def nezvuk():
    pygame.mixer.music.pause()
    
    crash_zvuk = pygame.mixer.Sound("crashzvuk.mp3")
    crash_zvuk.set_volume(0)

        
def zvuk():
    pygame.mixer.music.unpause()
    

def paused():
    pause = True
         
    while pause:
        udalosti = pygame.event.get()
        for udalost in udalosti:
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if udalost.type == pygame.KEYDOWN:
                if udalost.key == pygame.K_ESCAPE:
                    pause = False
                         
                         
                         
        okno.blit(pausefoto, (0, 0))
        okno.blit(continue1, (519, 392))
        okno.blit(restart, (533, 438))
        okno.blit(options, (533, 480))
        okno.blit(quit1, (580, 525))
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
             
        if mouse[0] > 519 and mouse[0] < 744 and mouse[1] > 392 and mouse[1] < 430:
            okno.blit(continue2, (519, 392))
            if click == (True, False, False):
                pause = False
            
        if mouse[0] > 533 and mouse[0] < 728 and mouse[1] > 443 and mouse[1] < 479:
            okno.blit(restart2, (533, 438))
            if click == (True, False, False):
                gameloop()
                
        if mouse[0] > 533 and mouse[0] < 728 and mouse[1] > 481 and mouse[1] < 518:
            okno.blit(options2, (533, 480))
            if click == (True, False, False):
                optionsmenu()      
            
        if mouse[0] > 580 and mouse[0] < 690 and mouse[1] > 525 and mouse[1] < 563:
            okno.blit(quit2, (580, 525))
            if click == (True, False, False):
                pygame.quit()
                sys.exit()
            
            
                      
        pygame.display.update()

    
def highscore(pocet):
    font = pygame.font.Font("VCR_OSD_MONO.ttf",35)
    text = font.render("Score:"+str(pocet),True,255)
    okno.blit(text,(30,30))
    pocet = 0
    
def prekazky(prekx,preky,prekazka):
    okno.blit(prekazka, (prekx,preky))
    
    
def prekazky2(prek2x, prek2y, prekazka2):
    okno.blit(prekazka2, (prek2x, prek2y))
    
def prekazky3(prek3x, prek3y, prekazka3):
    okno.blit(prekazka3, (prek3x, prek3y))
    
def prekazky32(prek32x, prek32y, prekazka32):
    okno.blit(prekazka32, (prek32x, prek32y))
    
def prekazky4(prek4x, prek4y, prekazka4):
    okno.blit(prekazka4, (prek4x, prek4y))

    
#pozadí
def pozadi():
    okno.blit(silnice, (100, 0))
    okno.blit(trava1, (0,0))
    okno.blit(trava2, (700,0))

#auto
def auto(autoX, autoY):
    okno.blit(fotoauta, (autoX, autoY))

   
def crash(autoX, autoY):
    
    #exploze
    sirka_crash = 722 // 6
    vyska_crash = 702 // 6
    pozice_crashX = autoX
    
    crashexploze_mensi = pygame.transform.scale(crashexploze, (sirka_crash, vyska_crash))
    okno.blit(crashexploze_mensi, (pozice_crashX, autoY))
  
    #překážky
    prek_sirka = 50
    prek_vyska = 100
    prek_speed = 7
    prek2_speed = 10
    
    #překážka č.1
    prekazka_startx = random.randrange(400,460)
    prekazka_starty = random.randrange(-214, -540, -447)
 
    if autoX >= prekazka_startx and autoX <= prekazka_startx+prek_sirka:
        pozice_crashX = autoX - 50
        
    if autoX+sirka >= prekazka_startx and autoX+sirka <= prekazka_startx+prek_sirka:
        pozice_crashX = autoX + 10
        
    #překážka č.2
    prekazka2_startx = random.randrange(100,160)
    prekazka2_starty = random.randrange(-300, -400, -400)
    
    if autoX >= prekazka2_startx and autoX <= prekazka2_startx+prek_sirka:
        pozice_crashX = autoX - 50
        
    if autoX+sirka >= prekazka2_startx and autoX+sirka <= prekazka2_startx+prek_sirka:
        pozice_crashX = autoX + 10
        
    #překážka č.3
    prekazka3_startx = random.randrange(240,300)
    prekazka3_starty = random.randrange(-377,-447, -484)
    
    if autoX >= prekazka3_startx and autoX <= prekazka3_startx+prek_sirka:
        pozice_crashX = autoX - 50
        
    if autoX+sirka >= prekazka3_startx and autoX+sirka <= prekazka3_startx+prek_sirka:
        pozice_crashX = autoX + 10
        
    #překážka č.4
    prekazka4_startx = random.randrange(540,600)
    prekazka4_starty = random.randrange(-1000,-1200, -400)
    
    if autoX >= prekazka4_startx and autoX <= prekazka4_startx+prek_sirka:
        pozice_crashX = autoX - 50
        
    if autoX+sirka >= prekazka4_startx and autoX+sirka <= prekazka4_startx+prek_sirka:
        pozice_crashX = autoX + 10
        
    #překážka č.3.2
    prekazka32_startx = random.randrange(240,300)
    prekazka32_starty = random.randrange(-637,-973, -1357)
    
    if autoX >= prekazka32_startx and autoX <= prekazka32_startx+prek_sirka:
        pozice_crashX = autoX - 50
        
    if autoX+sirka >= prekazka32_startx and autoX+sirka <= prekazka32_startx+prek_sirka:
        pozice_crashX = autoX + 10
        
    
    #zvuk nárazu
    crash_zvuk = pygame.mixer.Sound("crashzvuk.mp3")
    crash_zvuk.play()
    
    #text: CRASHED
    sirka_crashed = 120 * 3
    vyska_crashed = 30 * 3
    crashfoto_vetsi = pygame.transform.scale(crashfoto, (sirka_crashed, vyska_crashed))
    crash_rect = crashfoto_vetsi.get_rect()
    crash_rect.center = okno.get_rect().center
    okno.blit(crashfoto_vetsi, crash_rect)
    pygame.display.flip()
    pygame.display.update()
    time.sleep(2)
    gameloop()



#game loop
def gameloop():
    spusteno = True
    pause = False
    autoX = 435
    autoY= 460
    rychlostX = 0
    rychlostY = 0
    silnice_x1 = 100
    silnice_x2 = 100
    silnice_y1 = 0
    silnice_y2 = -600
    silnice_speed = 8
    silnice_speed_change = 0
    pygame.mixer.music.play(-1)
    pocet = 0
    fullscreen = False
    
    #překážka č.1
    prekazka_startx = random.randrange(400,460)
    prekazka_starty = random.randrange(-214, -540, -447)
    prek_sirka = 50
    prek_vyska = 100
    prek_speed = 7
    prek2_speed = 10
    
    #překážka č.2
    prekazka2_startx = random.randrange(100,160)
    prekazka2_starty = random.randrange(-300,-400, -400)
    
    #překážka č.3
    prekazka3_startx = random.randrange(240,300)
    prekazka3_starty = random.randrange(-377,-447, -484)
    
    #překážka č.3.2
    prekazka32_startx = random.randrange(240,300)
    prekazka32_starty = random.randrange(-637,-973, -1357)
    
    #překážka č.4
    prekazka4_startx = random.randrange(540,600)
    prekazka4_starty = random.randrange(-1000,-1200, -400)
    
    while spusteno:
        stisknuto = pygame.key.get_pressed()
        udalosti = pygame.event.get()
        
        #vypnutí aplikace
        
        for udalost in udalosti:
            
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #ovládání auta
            if udalost.type == pygame.KEYDOWN:
                if udalost.key == pygame.K_RIGHT:
                    rychlostX = 6
                if udalost.key == pygame.K_LEFT:
                    rychlostX = -6
                    
                    
                if udalost.key == pygame.K_ESCAPE:
                    paused()
                    
                if udalost.key == pygame.K_SPACE:
                    gameloop()
                    
                    
            if udalost.type == pygame.KEYDOWN:     
                if udalost.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        pygame.display.set_mode((sirka_okna, vyska_okna), pygame.FULLSCREEN)
                    else:
                        
                        pygame.display.set_mode((sirka_okna, vyska_okna))
                        
            
        #    if udalost.key == pygame.K_UP:
        #         rychlostY = -5
        #    if udalost.key == pygame.K_DOWN:
        #         rychlostY = 5
                 
            if udalost.type == pygame.KEYUP:
                if udalost.key == pygame.K_LEFT or udalost.key == pygame.K_RIGHT:
                    rychlostX = 0
                 
        #if udalost.type == pygame.KEYUP:
        #    if udalost.key == pygame.K_UP or udalost.key == pygame.K_DOWN:
        #        rychlostY = 0
                
        autoX += rychlostX
        #autoY += rychlostY
            

        pozadi()

        okno.blit(silnice,(silnice_x1,silnice_y1))
        okno.blit(silnice, (silnice_x2,silnice_y2))
        
        silnice_y1 += silnice_speed
        silnice_y2 += silnice_speed

        if silnice_y1 >= vyska_okna:
            silnice_y1 = -600

        if silnice_y2 >= vyska_okna:
            silnice_y2 = -600
          
        if autoX > 700-sirka:
            crash(autoX, autoY)
            
        if autoX < 100:
            crash(autoX, autoY)
           
        if autoY < prekazka_starty + prek_vyska:
            if autoX >= prekazka_startx and autoX <= prekazka_startx+prek_sirka:
                crash(autoX-25,autoY-vyska/2)
                if autoX+sirka >= prekazka_startx and autoX+sirka <= prekazka_startx+prek_sirka:
                    crash(autoX,autoY-vyska/2)
        
        if autoY < prekazka2_starty + prek_vyska:
            if autoX >= prekazka2_startx and autoX <= prekazka2_startx+prek_sirka:
                crash(autoX-25,autoY-vyska/2)
                if autoX+sirka >= prekazka2_startx and autoX+sirka <= prekazka2_startx+prek_sirka:
                    crash(autoX,autoY-vyska/2)
            
        if autoY < prekazka3_starty + prek_vyska:
            if autoX >= prekazka3_startx and autoX <= prekazka3_startx+prek_sirka:
                crash(autoX-25,autoY-vyska/2)
                if autoX+sirka >= prekazka3_startx and autoX+sirka <= prekazka3_startx+prek_sirka:
                    crash(autoX,autoY-vyska/2)
                    
        if autoY < prekazka32_starty + prek_vyska:
            if autoX >= prekazka32_startx and autoX <= prekazka32_startx+prek_sirka:
                crash(autoX-25,autoY-vyska/2)
                if autoX+sirka >= prekazka32_startx and autoX+sirka <= prekazka32_startx+prek_sirka:
                    crash(autoX,autoY-vyska/2) 
                    
        if autoY < prekazka4_starty + prek_vyska:
            if autoX >= prekazka4_startx and autoX <= prekazka4_startx+prek_sirka:
                crash(autoX-25,autoY-vyska/2)
                if autoX+sirka >= prekazka4_startx and autoX+sirka <= prekazka4_startx+prek_sirka:
                    crash(autoX,autoY-vyska/2)
                    
           
        auto(autoX, autoY)
        
        prekazky(prekazka_startx,prekazka_starty,fotoauta2)
        prekazky2(prekazka2_startx,prekazka2_starty,fotoauta3flip)
        prekazky3(prekazka3_startx,prekazka3_starty,fotoauta4flip)
        prekazky4(prekazka4_startx, prekazka4_starty,fotoauta5)
        prekazky32(prekazka32_startx,prekazka32_starty,fotoauta6flip)
        
        highscore(pocet)              
        pocet+=1
        prekazka_starty += prek_speed
        prekazka2_starty += prek2_speed
        prekazka3_starty += prek2_speed
        prekazka32_starty += prek2_speed
        prekazka4_starty += prek_speed

        if prekazka_starty > sirka_okna:
            prekazka_startx = random.randrange(400,460)
            prekazka_starty = random.randrange(-200,-600, -400)
        
        
        if prekazka2_starty > sirka_okna:
            prekazka2_startx = random.randrange(100,160)
            prekazka2_starty = random.randrange(-300,-400, -400)
        
        if prekazka3_starty > sirka_okna:
            prekazka3_startx = random.randrange(240,300)
            prekazka3_starty = random.randrange(-377,-447, -484)
        
        if prekazka32_starty > sirka_okna:
            prekazka32_startx = random.randrange(240,300)
            prekazka32_starty = random.randrange(-637,-973, -1357)
            
        if prekazka4_starty > sirka_okna:   
            prekazka4_startx = random.randrange(540,600)
            prekazka4_starty = random.randrange(-1000,-1200, -400)
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if mouse[0] > 725 and mouse[0] < 775 and mouse[1] > 15 and mouse[1] < 60:
            okno.blit(pausetext2_mensi, (720, 10))
            if click == (True, False, False):
                paused()
        else:
            okno.blit(pausetext_mensi, (720, 10))
            
    
        pygame.display.update()
        hodiny.tick(60)

         

mainmenu()
gameloop()
paused()
pygame.quit()
quit()

    
    
    
    
