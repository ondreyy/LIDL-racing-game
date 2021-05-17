import pygame, sys, random, time
pygame.init()

#název
pygame.display.set_caption("RƎTRO racing")

#okno
sirka_okna = 800
vyska_okna = 600
okno = pygame.display.set_mode((sirka_okna, vyska_okna))

okno.fill((0,0,0))

#čas
hodiny = pygame.time.Clock()

#soundtrack
pygame.mixer.music.load("soundtrack.mp3")
pygame.mixer.music.set_volume(0.4)

#načíst obrázky
fotoauta = pygame.image.load("auto.png") #RED
fotoauta2 = pygame.image.load("auto2.png") #GREEN
fotoauta3 = pygame.image.load("auto3.png") #BLUE
fotoauta4 = pygame.image.load("auto4.png") #YELLOW
fotoauta5 = pygame.image.load("auto5.png") #BLACK
fotoauta6 = pygame.image.load("auto6.png") #WHITE

menufoto = pygame.image.load("RetroRacingMENU.png")

trava1 = pygame.image.load("trava.png")
trava2 = pygame.image.load("trava.png")
trava2 = pygame.transform.flip(trava2, 180, 0)

silnice = pygame.image.load("silnicepre.png")

crashfoto = pygame.image.load("crashed.png")
crashexploze = pygame.image.load("crash.png")

play = pygame.image.load("playbutton.png")
options = pygame.image.load("optionsbutton.png")
quit = pygame.image.load("quitbutton.png")

play2 = pygame.image.load("playbutton2.png")
options2 = pygame.image.load("optionsbutton2.png")
quit2 = pygame.image.load("quitbutton2.png")


#ikona
pygame.display.set_icon(fotoauta)

# # # # # # # # # # # # # # # # 

#auta
sirka = 270 // 4
vyska = 460 // 4
fotoauta = pygame.transform.scale(fotoauta, (sirka, vyska))
fotoauta2 = pygame.transform.scale(fotoauta2, (sirka, vyska))
fotoauta3 = pygame.transform.scale(fotoauta3, (sirka, vyska))
fotoauta4 = pygame.transform.scale(fotoauta4, (sirka, vyska))
fotoauta5 = pygame.transform.scale(fotoauta5, (sirka, vyska))
fotoauta6 = pygame.transform.scale(fotoauta6, (sirka, vyska))

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
        okno.blit(quit, (550, 490))
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        
        if mouse[0] > 555 and mouse[0] < 670 and mouse[1] > 395 and mouse[1] < 435:
            okno.blit(play2, (550, 390))
            if click == (True, False, False):
                gameloop()
            
        if mouse[0] > 513 and mouse[0] < 711 and mouse[1] > 443 and mouse[1] < 483:
            okno.blit(options2, (510, 440))
           # if click == (True, False, False):
           # DODĚLAT OPTIONS !!! # Fullscreen etc. #
            
        if mouse[0] > 553 and mouse[0] < 662 and mouse[1] > 493 and mouse[1] < 533:
            okno.blit(quit2, (550, 490))
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
    okno.blit(prekazka, (prekx,preky))
    
#pozadí
def pozadi():
    okno.blit(silnice, (100, 0))
    okno.blit(trava1, (0,0))
    okno.blit(trava2, (700,0))

#auto
def auto(autoX, autoY):
    okno.blit(fotoauta, (autoX, autoY))

#crash text
#def text_objekt(text,font):
#    textRender = font.render(text,True,255)
#    return textRender,textRender.get_rect()
#
#def zobrazeni_textu(text,size,autoX,autoY):
#    font = pygame.font.Font("8-bit wonder.ttf",size)
#    text_surface, text_rectangle = text_objekt(text,font)
#    text_rectangle.center =(autoX,autoY)
#    okno.blit(text_surface, text_rectangle)



#def crash(autoX, autoY):
#    okno.blit(crashfoto, (crash_rect.center))
#    zobrazeni_textu("CRASHED", 64, sirka_okna/2, vyska_okna/2)
#    pygame.display.update()
#    time.sleep(2)
#    gameloop()
   
def crash(autoX, autoY):
    
    #exploze
    sirka_crash = 722 // 6
    vyska_crash = 702 // 6
    pozice_crashX = autoX
    
    crashexploze_mensi = pygame.transform.scale(crashexploze, (sirka_crash, vyska_crash))
    okno.blit(crashexploze_mensi, (pozice_crashX, autoY))    
  
    #překážka č.1
    prekazka_startx = random.randrange(400,700-sirka)
    prekazka_starty = -600
    prek_sirka = 50
    prek_vyska = 100
    prek_speed = 10
 
    if autoX >= prekazka_startx and autoX <= prekazka_startx+prek_sirka:
        pozice_crashX = autoX - 50
        
    if autoX+sirka >= prekazka_startx and autoX+sirka <= prekazka_startx+prek_sirka:
        pozice_crashX = autoX + 10
        
    #překážka č.2
    prekazka_startx = random.randrange(100,300)
    prekazka_starty = -600
    prek_sirka = 50
    prek_vyska = 100
    prek_speed = 10
    
    if autoX >= prekazka_startx and autoX <= prekazka_startx+prek_sirka:
        pozice_crashX = autoX - 50
        
    if autoX+sirka >= prekazka_startx and autoX+sirka <= prekazka_startx+prek_sirka:
        pozice_crashX = autoX + 10
         
    
#    if autoX <= 100:
#        pozice_crashX = autoX - 50
#    if autoX >= 600:
#        pozice_crashX = autoX + 10
    
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
    autoX = 440
    autoY= 460
    rychlostX = 0
    rychlostY = 0
    silnice_x1 = 100
    silnice_x2 = 100
    silnice_y1 = 0
    silnice_y2 = -600
    silnice_speed = 8
    silnice_speed_change = 0
    #pygame.mixer.music.play(-1)
    pocet = 0
    
    #překážka č.1
    prekazka_startx = random.randrange(400,700-sirka)
    prekazka_starty = -600
    prek_sirka = 50
    prek_vyska = 100
    prek_speed = 10
    
    #překážka č.2
    prekazka_startx = random.randrange(100,300)
    prekazka_starty = -600
    prek_sirka = 50
    prek_vyska = 100
    prek_speed = 10
    
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
                    rychlostX = 8
                if udalost.key == pygame.K_LEFT:
                    rychlostX = -8
            
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
            
            
        if stisknuto[pygame.K_SPACE]:
            autoX = 440
            autoY = 460

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
           
        auto(autoX, autoY)
        prekazky(prekazka_startx,prekazka_starty,fotoauta3)
        prekazky(prekazka_startx,prekazka_starty,fotoauta3)
        
        highscore(pocet)              
        pocet+=1
        prekazka_starty += prek_speed

        if prekazka_starty > sirka_okna:
            prekazka_startx = random.randrange(400,700-sirka)
            prekazka_starty = -200
        
        if prekazka_starty > sirka_okna:
            prekazka_startx = random.randrange(100,300)
            prekazka_starty = -200
        
        pygame.display.update()
        hodiny.tick(60)
        
mainmenu()        
gameloop()
pygame.quit()
quit()

    
    
    
    
