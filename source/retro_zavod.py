import pygame, sys, random, time
from time import sleep
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

#načíst obrázky
fotoauta = pygame.image.load("auto.png")

trava1 = pygame.image.load("trava.png")
trava2 = pygame.image.load("trava.png")
trava2 = pygame.transform.flip(trava2, 180, 0)

silnice = pygame.image.load("silnicepre.png")

crashfoto = pygame.image.load("crashed.png")
crashexploze = pygame.image.load("crash.png")

#ikona
pygame.display.set_icon(fotoauta)

# # # # # # # # # # # # # # # # 

#auta
sirka = 270 // 4
vyska = 460 // 4
fotoauta = pygame.transform.scale(fotoauta, (sirka, vyska))

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
    if autoX <= 100:
        pozice_crashX = autoX - 50
    if autoX >= 600:
        pozice_crashX = autoX + 10
    crashexploze_mensi = pygame.transform.scale(crashexploze, (sirka_crash, vyska_crash))
    okno.blit(crashexploze_mensi, (pozice_crashX, autoY))
    
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
    autoY= 480
    rychlostX = 0
    rychlostY = 0
    silnice_x1 = 100
    silnice_x2 = 100
    silnice_y1 = 0
    silnice_y2 = -600
    silnice_speed = 8
    silnice_speed_change = 0
    
    while spusteno:
        stisknuto = pygame.key.get_pressed()
        udalosti = pygame.event.get()
        
        #vypnutí aplikace
        
        for udalost in udalosti:
            
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if stisknuto[pygame.K_ESCAPE]:
            pygame.QUIT
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
            autoY = 480

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
           
            

        auto(autoX, autoY)
        
        pygame.display.update()
        hodiny.tick(60)
        
gameloop()
pygame.quit()
quit()

    
    
    
    