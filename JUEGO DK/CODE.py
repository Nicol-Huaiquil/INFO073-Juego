#!/usr/bin/env python
# -*- coding: utf-8 -*-
#☻ ♦ ◄ ► ▼ ▲

import curses
import keyboard
import time
import random
#Estefano Espinoza & Nicol Huaiquil
def portada():
    screen = curses.initscr()
    curses.start_color()
                                    #Texto              fondo
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_BLACK)
     
    booleano=True
    while booleano:
        #N°s aleatorios para los colores
        n=random.randint(5,6)
        x=random.randint(1,5)
                                #Texto que se ve en la portada
        screen.addstr(8,38, " D   O   N   K   E   Y    K   O   N   G ", curses.color_pair(x))
        screen.addstr(11,47, " El rescate del tesoro", curses.color_pair(x))
        print()
        screen.addstr(16,45, "pulsa 'ENTER' para comenzar", curses.color_pair(n))
        screen.addstr(26,33,"Desarrollado por Estefano Espinoza & Nicol Huaiquil",curses.color_pair(4)) 
        time.sleep(0.2)
        screen.refresh()
        try:       
            if keyboard.is_pressed('enter'):
                #Limpia todo en pantalla
                screen.clear()
                return(True)
            
            if keyboard.is_pressed('esc'):
                return(False)
        except:
            pass
        
def tablero():
    
    screen = curses.initscr()
    curses.start_color()
                                #colorTexto       #colorFondo               
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)  
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLUE)

                # Largo eje y
    for i in range(3,23):
        screen.addstr(i,2,"                    ", curses.color_pair(1))
                #largo de eje x
        screen.addstr(i,22,"                    ", curses.color_pair(2))
        screen.refresh()
        
                 #y , x
    screen.addstr(18,48,"Como jugar:",curses.color_pair(5))
    screen.addstr(20,48," Movimiento ",curses.color_pair(5))
    screen.addstr(22,54,"▲",curses.color_pair(6))
    screen.addstr(23,52,"◄ ▼ ►",curses.color_pair(6))
    
    screen.refresh()
    
    #--------up---------Crea el tablero------------------- 

    #origenDeFlechas
    x=1
    y=3
    screen = curses.initscr()
    screen.addstr(y,x,"◄", curses.color_pair(3)) 

    x=42 
    y=22
    screen = curses.initscr()
    screen.addstr(y,x,"►", curses.color_pair(4))

    screen.refresh()
    
def bombas():

    #origen de cursor para colocar bombas
    x=2
    y=3
    screen = curses.initscr()
    curses.start_color()
                                    #texto              fondo
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_BLACK)
    
                # y , x  Texto que aparece en pantalla lado derecho cuando se colocan las bombas
    screen.addstr(11,48,"FASE 1:",curses.color_pair(2))
    screen.addstr(12,48,"Debes ubicar bombas (",curses.color_pair(2))
    screen.addstr(12,69,"♦",curses.color_pair(4))
    screen.addstr(12,70,") para evitar que tu enemigo llegue a tu tesoro",curses.color_pair(2))
    screen.addstr(20,70," Poner bombas ",curses.color_pair(2))
    screen.addstr(23,72," ESPACIO ",curses.color_pair(3))
    screen.addstr(3,45,"Bombas Restantes:", curses.color_pair(2))
    screen.addstr(4,45,"♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦", curses.color_pair(4))
    screen.addstr(y,x," ", curses.color_pair(3))
    screen.refresh()
    
    #para borrar desde atrás el texto con bombas de pantalla lado derecho
    borrador=83
    #Lista para coordenadas de bombas
    BombasJugadorXY=[]
    
    #cantidad de bombas a colocar 
    Bom=20
    contador=0
    booleano=True
   
    while(contador<Bom):
        #Para que al presionar "espacio" se coloquen bombas
        if keyboard.is_pressed('space'):
            #para que cuando sea 20 deje de colocar bombas
            contador=contador+1
            #condiciones para no colocar bombas a los lados de esta, ni encima
            if(((x,y) not in BombasJugadorXY) and ((x+1,y+1) not in BombasJugadorXY) and ((x-1,y-1) not in BombasJugadorXY) and ((x,y+1) not in BombasJugadorXY) and ((x+1,y-1) not in BombasJugadorXY) and ((x-1,y+1) not in BombasJugadorXY) and ((x-1,y) not in BombasJugadorXY) and ((x+1,y) not in BombasJugadorXY) and ((x,y-1) not in BombasJugadorXY)):
                             #"borrador" coodenada que disminuye para borrar las bombas en pantalla lado derecho
                screen.addstr(4,borrador," ", curses.color_pair(7))
                borrador=borrador-2
                #imprime bomba
                screen.addstr(y,x,"♦", curses.color_pair(1))
                screen.refresh()
                time.sleep(0.2)
                #agrega coordenadas de bombas a una lista
                BombasJugadorXY.append((x,y))
                
            else:
                contador=contador-1
                screen.addstr(8,48,"Error, no puedes colocar una bomba ni sobre ni junto a otra!", curses.color_pair(5))
                screen.refresh()
                time.sleep(1)
                #Para que desaparezca el mensaje de #Error..."
                screen.addstr(8,48,"                                                              ", curses.color_pair(7))
                screen.refresh()
                time.sleep(0.5)
              
        #para mover cursor hacia  A R R I B A      
        if keyboard.is_pressed('up'):
            #para que coordenada cambie cuando cursor suba
            y=y-1
            #Limite para no colocar bombas en la parte superior fuera del tablero
            if (y==2): 
                y=y+1
            #Para no dejar rastro
            screen.addstr(y,x,"", curses.color_pair(6)) 
            time.sleep(0.2) 
            screen.refresh()
            
            
        #para mover cursor hacia  A B A J O   
        if keyboard.is_pressed('down'):
            #para que coordenada cambie cuando cursor baje
            y=y+1
            #Limite para no colocar bombas en la parte inferior fuera del tablero
            if (y==23):
                y=y-1
            #Para no dejar rastro
            screen.addstr(y,x,"", curses.color_pair(6))
            time.sleep(0.2)
            screen.refresh()
            
            
        #Para mover cursor hacia la  I Z Q U I E R D A        
        if keyboard.is_pressed('left'):
            #para que coordenada cambie cuando cursor vaya hacia la izquierda
            x=x-1
            #Limite para no colocar bombas en la parte izquierda fuera del tablero
            if (x==1):
                x=x+1
            #Para no dejar rastro
            screen.addstr(y,x,"", curses.color_pair(6)) 
            time.sleep(0.2)
            screen.refresh()
            
            
        #Para mover cursor hacia   D E R E C H A      
        if keyboard.is_pressed('right'):
            #para que coordenada cambie cuando cursor vaya a derecha 
            x=x+1
            #Limite para no colocar bombas en lado enemigo
            if (x==22):
                x=x-1
            #Para no dejar rastro
            screen.addstr(y,x,"", curses.color_pair(6))
            time.sleep(0.2)
            screen.refresh()   
        
        if keyboard.is_pressed('esc'):
            contBom=Bom
            booleano=False
            
    #retorna lista de coordenadas de las bombas
    return(BombasJugadorXY)        
    booleano=False
                       

def bomBot():
    screen=curses.initscr()
    curses.start_color()
    
                                    #texto              fondo
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLACK)
    
    #texto que se muestra en tablero lado derecho
    screen.addstr(3,45,"Ubicando Bombas Enemigas:", curses.color_pair(2))
    screen.addstr(4,45,"♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦", curses.color_pair(3))

    #para coordenadas aleatorias de bombas enemigas
    x=random.randint(22,40)
    y=random.randint(3,22)
    #para imprimir la primera bomba enemiga
    screen.addstr(y,x,"♦", curses.color_pair(1))
    screen.refresh()
    time.sleep(0.1)
    
    #Lista para coordenadas de bombas
    BombasEnemigoXY=[]
    #para borrar desde atrás el texto con bombas enemigas de pantalla lado derecho
    borrador=83
    #agrega coordenadas de bombas
    BombasEnemigoXY.append((x,y))
    contador=0
    contador=contador+1
    '''BombAdd=False'''
    while(contador < 20):
        #para coordenadas aleatorias de bombas enemigas
        x=random.randint(22,40)
        y=random.randint(3,22)
        BombAdd=True
        while(BombAdd==True):
            #condiciones para no colocar bombas en el mismo lugar ni a los alrededores
            if(((x,y) not in BombasEnemigoXY) and ((x+1,y+1) not in BombasEnemigoXY) and ((x-1,y-1) not in BombasEnemigoXY) and ((x,y+1) not in BombasEnemigoXY) and ((x+1,y) not in BombasEnemigoXY) and ((x+1,y-1) not in BombasEnemigoXY) and ((x-1,y+1) not in BombasEnemigoXY) and ((x-1,y) not in BombasEnemigoXY) and ((x,y-1) not in BombasEnemigoXY)):
                #"borrador" coodenada que disminuye para borrar las bombas enemigas de pantalla lado derecho
                screen.addstr(4,borrador," ", curses.color_pair(4))
                borrador = borrador - 2
                #imprime bombas enemigas
                screen.addstr(y,x,"♦", curses.color_pair(1))
                screen.refresh()
                time.sleep(0.1)
                #para que cuando llegue a 20 deje de colocar bombas
                contador=contador+1
                #coordenadas de bombas
                BombasEnemigoXY.append((x,y))
                BombAdd=True
                #para coordenadas aleatorias de bombas
                x=random.randint(22,40)
                y=random.randint(3,22)    

            else:
                BombAdd=False
    #Para borrar texto del lado derecho de la pantalla que indica las bombas restantes           
    screen.addstr(3,45,"                                    ", curses.color_pair(4))
    screen.addstr(4,45,"                                    ", curses.color_pair(4))
    screen.refresh()
    #retorna lista de coordenadas de las bombas
    return(BombasEnemigoXY)

#recibe las lista con coordenadas de bombas enemigas y de usuario
def carita(ListaCB):
    
    screen = curses.initscr()
    curses.start_color()
                                   #Texto             #fondo
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(6,curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(7,curses.COLOR_WHITE, curses.COLOR_WHITE)
    #Para borrar bombas enemigas
    for i in range(3,23):
        screen.addstr(i,22,"                    ", curses.color_pair(7))
        
                    # y , x  TEXTO de pantalla lado derecho que aparece cuando termina la etapa de colocar bombas
    screen.addstr(3,48,"FASE 2:",curses.color_pair(5))
    screen.addstr(4,48,"Tu personaje:",curses.color_pair(5))
    screen.addstr(4,62," ☻ ",curses.color_pair(1))
    screen.addstr(4,65," Tu enemigo: ",curses.color_pair(5))
    screen.addstr(4,78," ☻ ",curses.color_pair(3))
    screen.addstr(7,48,"-Debes llegar al tesoro de tu enemigo",curses.color_pair(5))
    screen.addstr(7,85," ►",curses.color_pair(1))
    screen.addstr(9,48,"-Evita las bombas que ubicó tu enemigo",curses.color_pair(5))
    screen.addstr(9,86,"♦",curses.color_pair(3))
    screen.addstr(11,48,"       ",curses.color_pair(2))
    screen.addstr(11,48,"-Si tu personaje o tu enemigo chocan con tus bombas",curses.color_pair(5))
    screen.addstr(11,100,"♦",curses.color_pair(4))
    screen.addstr(11,102,"o las suyas",curses.color_pair(5))
    screen.addstr(11,114,"♦",curses.color_pair(3))
                        #texto negro que se coloca para borrar parte del texto de funcion bombas
    screen.addstr(12,48,"                      ",curses.color_pair(2))
    screen.addstr(12,70,"                                               ",curses.color_pair(2))
    screen.addstr(12,69," ",curses.color_pair(4))
    screen.addstr(12,48,"comenzaran desde donde comenzaron.",curses.color_pair(5))
    screen.addstr(14,48,"-Puedes chocar con tu enemigo para que ambos vuelvan a comenzar",curses.color_pair(5))
    screen.addstr(16,48,"-Quien llegue primero",curses.color_pair(5))
    screen.addstr(16,70,"¡G A N A!",curses.color_pair(4))
                       #texto negro que se coloca para borrar parte del texto de funcion bombas
    screen.addstr(20,70,"              ",curses.color_pair(2))
    screen.addstr(23,72,"         ",curses.color_pair(2))
    screen.addstr(20,68,"Salir",curses.color_pair(5))
    screen.addstr(23,68," ESC ",curses.color_pair(6))

    #Coordenadas de inicio de caritas
    x=2 
    y=3
    
    w=22 
    d=41
    
    #MovimientoAleatorioCPU
    n=random.randint(1,8)

    #ImprimeCaritas
    screen.addstr(y,x,"☻", curses.color_pair(1)) 
    screen.addstr(w,d,"☻", curses.color_pair(3)) 
    screen.refresh()

    booleano=True
    while booleano:
        try:
            #para mover carita hacia A R R I B A 
            if keyboard.is_pressed('up'):    
                #condicion para choque de caritas y retornen
                if(y+1==w) and (x==d):
                    #Para que no quede marcado donde mueren
                    screen.addstr(y,x," ", curses.color_pair(2))
                    x=2 
                    y=3
                    screen.addstr(y,x,"☻", curses.color_pair(1))
                    #Para que no quede marcado donde mueren
                    screen.addstr(w,d," ", curses.color_pair(3))
                    w=22
                    d=41
                    screen.addstr(w,d,"☻", curses.color_pair(3))
                    continue
                
                #para no dejar rastro de caritas
                screen.addstr(y,x," ",curses.color_pair(2))
                #para que coordenada cambie cuando la carita suba
                y=y-1
                #Limite para que no se escape hacia arriba
                if (y==2):
                    y=y+1
                screen.addstr(y,x,"☻", curses.color_pair(1))
                time.sleep(0.2)
                #funcion que realiza movimiendo de CPU
                w,d = MovRandomCara(n,w,d)
                screen.refresh()
                #numero random que define direccion cpu
                n=random.randint(1,8)
                
            #para mover carita hacia A B A J O    
            if keyboard.is_pressed('down'):
                
                #condicion para choque de caritas y retornen
                if(y-1==w) and (x==d):
                    #Para que no quede marcado donde mueren
                    screen.addstr(y,x," ", curses.color_pair(2))
                    x=2 
                    y=3
                    screen.addstr(y,x,"☻", curses.color_pair(1))
                    #Para que no quede marcado donde mueren
                    screen.addstr(w,d," ", curses.color_pair(3))
                    w=22
                    d=41
                    screen.addstr(w,d,"☻", curses.color_pair(3))
                    continue
                #para no dejar rastro de caritas
                screen.addstr(y,x," ",curses.color_pair(2))
                #para que coordenada cambie cuando la carita baje
                y=y+1
                #Limite para que no se escape hacia abajo
                if (y==23):
                    y=y-1
                screen.addstr(y,x,"☻", curses.color_pair(1)) 
                time.sleep(0.2)
                #funcion que realiza movimiendo de CPU
                w,d = MovRandomCara(n,w,d)
                screen.refresh()
                #numero random que define direccion cpu
                n=random.randint(1,8)    

            #para mover carita hacia la  I Z Q U I E R D A
            if keyboard.is_pressed('left'):
                #condicion para choque de caritas y retornen
                if(x-1==d) and (y==w):
                    #Para que no quede marcado donde mueren
                    screen.addstr(y,x," ", curses.color_pair(2))
                    x=2 
                    y=3
                    screen.addstr(y,x,"☻", curses.color_pair(1))
                    #Para que no quede marcado donde mueren
                    screen.addstr(w,d," ", curses.color_pair(3))
                    w=22
                    d=41
                    screen.addstr(w,d,"☻", curses.color_pair(3))
                    continue
                #para no dejar rastro de caritas
                screen.addstr(y,x," ",curses.color_pair(2))
                #para que coordenada cambie cuando vaya a la izquierda
                x=x-1
                #Limite para que no se escape hacia la izquierda
                if (x==1):
                    x=x+1
                screen.addstr(y,x,"☻", curses.color_pair(1)) 
                time.sleep(0.2)
                #funcion que realiza movimiendo de CPU
                w,d = MovRandomCara(n,w,d)
                screen.refresh()
                #numero random que define direccion cpu
                n=random.randint(1,8)

            #para mover carita hacia la  D E R E C H A    
            if keyboard.is_pressed('right'):
                #condicion para choque de caritas y retornen
                if(x+1==d) and (y==w):
                    #Para que no quede marcado donde mueren
                    screen.addstr(y,x," ", curses.color_pair(2))
                    x=2 
                    y=3
                    screen.addstr(y,x,"☻", curses.color_pair(1))
                    #Para que no quede marcado donde mueren
                    screen.addstr(w,d," ", curses.color_pair(3))
                    w=22
                    d=41
                    screen.addstr(w,d,"☻", curses.color_pair(3))
                    continue
                #para no dejar rastro de caritas
                screen.addstr(y,x," ",curses.color_pair(2))
                #para que coordenada cambie cuando vaya a derecha
                x=x+1
                #Limite para que no se escape hacia la derecha
                if (x==42):
                    x=x-1
                screen.addstr(y,x,"☻", curses.color_pair(1)) 
                time.sleep(0.2)
                #funcion que realiza movimiendo de CPU
                w,d = MovRandomCara(n,w,d)
                screen.refresh()
                #numero random que define direccion cpu
                n=random.randint(1,8)
                
            #condicion para que vuelvan las caritas a origen cuando choquen
            if((y==w) and (x==d)):
                #Para que no quede marcado donde mueren
                screen.addstr(y,x," ", curses.color_pair(2))
                x=2 
                y=3
                screen.addstr(y,x,"☻", curses.color_pair(1))
                screen.addstr(y,x," ", curses.color_pair(2))
                w=22
                d=41
                screen.addstr(w,d,"☻", curses.color_pair(3))
            #condicion para que cuando las coordenadas del jugador
            #sean iguales a alguna de las bombas del tablero, el jugador vuelva a inicio 
            if ((x,y) in ListaCB):
                #Para que no quede marcado donde mueren
                screen.addstr(y,x," ", curses.color_pair(2))
                #para que no se borre la bomba del tablero
                screen.addstr(y,x,"♦", curses.color_pair(4))
                x=2 
                y=3
                screen.addstr(y,x,"☻", curses.color_pair(1))
                
            #condicion para que cuando las coordenadas de CPU
            #sean iguales a alguna de las bombas del tablero, el CPU vuelva a inicio 
            if((d,w) in ListaCB):
                screen.addstr(w,d," ", curses.color_pair(2))
                #para que no se borre la bomba del tablero
                screen.addstr(w,d,"♦", curses.color_pair(4))
                w=22
                d=41
                screen.addstr(w,d,"☻", curses.color_pair(3))
                  
            #condicion para que al llegar a la meta salga mensaje de "ganaste"   
            if (x==41) and (y==22):
                screen.clear()
                screen.addstr(14,48,"G A N A S T E!! :D", curses.color_pair(4))
                screen.refresh()
                time.sleep(4)
                return(False)

            #condicion para que al llegar a la meta salga mensaje de "perdiste"     
            if (w==3) and (d==2):
                screen.clear()
                screen.addstr(14,47,"P E R D I S T E  >:C", curses.color_pair(3))
                screen.refresh()
                time.sleep(4)
                return(False)

            if keyboard.is_pressed('esc'):
                booleano=False
                
        except:
            pass
    
def MovRandomCara(n,w,d):
    screen = curses.initscr()

    #para que cuando salgan esos valores vaya hacia arriba
    if (n==4) or (n==5) or (n==7):
        #para no dejar rastro de caritas
        screen.addstr(w,d," ", curses.color_pair(2))
        #para que coordenada cambie cuando suba
        w=w-1
        #Limite para que no se escape hacia arriba
        if(w==2):
            w=w+1
        
        screen.addstr(w,d,"☻", curses.color_pair(3))
        time.sleep(0.1)

    #para que cuando salgan esos valores vaya hacia abajo    
    if (n==2):
        #para no dejar rastro de caritas
        screen.addstr(w,d," ", curses.color_pair(2))
        #para que coordenada cambie cuando baje
        w=w+1
        #Limite para que no se escape hacia abajo
        if(w==23):
            w=w-1
        
        screen.addstr(w,d,"☻", curses.color_pair(3))
        time.sleep(0.1)

    #para que cuando salgan esos valores vaya hacia la izquierda
    if (n==3) or (n==6) or (n==8):
        #para no dejar rastro de caritas
        screen.addstr(w,d," ", curses.color_pair(2))
        #para que coordenada cambie cuando vaya a izquierda
        d=d-1
        #Limite para que no se escape hacia izquierda
        if(d==1):
            d=d+1
        
        screen.addstr(w,d,"☻", curses.color_pair(3))
        time.sleep(0.1)

    #para que cuando salgan esos valores vaya hacia la derecha
    if (n==1):
        #para no dejar rastro de caritas
        screen.addstr(w,d," ", curses.color_pair(2))
        #para que coordenada cambie cuando vaya a derecha
        d=d+1
        #Limite para que no se escape hacia la derecha
        if(d==42):
            d=d-1
            
        screen.addstr(w,d,"☻", curses.color_pair(3))
        time.sleep(0.1)
            
    screen.refresh()
    return(w,d)
  
#PROGRAMA PRINCIPAL

booleano=portada()
while booleano:
    try:
        tablero()
        #Lista de Usuario
        ListaU=bombas()
        #Lista CPU
        ListaC=bomBot()
        #Lista Coordenadas bombas
        ListaCB=ListaU+ListaC
        
        booleano=carita(ListaCB)
 
        if keyboard.is_pressed('esc'):
            booleano=False
    except:
        pass
    
