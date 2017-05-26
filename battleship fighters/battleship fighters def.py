
from tkinter import *
import time
import random
import math



##CREANDO MENÚ PRINCIPAL


ventana=Tk()#crear la ventana de menu principal
ventana.geometry("1260x690+20+5")#tamaño de menu principal
ventana.title("battleship fighters")#titulo del menu principal(battleship fighters)
imagen=PhotoImage(file="menu.gif")#elegir imagen del menu principal
imagent=Label(ventana,image=imagen,cursor="pirate").place(x=0,y=0)#estableciendo imagen elegid

        #creando menu 1 jugador
def menu_1():
        
        #se modifica el menu principal
    ventana.geometry("1260x690+20+5")#el tamaño de la  ventana se deja igual
    ventana.title("one player")# titulo del menu de 1 jugador(one player)
    imagen=PhotoImage(file="menu2.gif")#elegimos la imagen del menu 1 jugador
    imagent=Label(ventana,image=imagen,cursor="pirate").place(x=0,y=0)#establecemos la imagen escogida
        #se crea la etiqueda de seleccionar nivel
    levelselect= Label(text="Level select:",bg="black",fg="blue",
                           font=("Harrington",25),cursor="pirate").place(x=750,y=370)
        #se crea una spinbox para seleccionar los niveles(1,2,3,4,5)
    spinlevel= Spinbox(ventana, values= ("nivel 1","nivel 2","nivel 3","nivel 4","nivel 5"),
                           fg="blue",bg="black",font=("Harrington",15),width=12,cursor="pirate").place(x=950,y=380)
        #se crea la etiqueta para el nombre del jugador(player's name:)
    plname= Label(text="player's name:",bg="black",fg="blue",font=("Harrington",25),cursor="pirate").place(x=750,y=470)
        #crear campo de texto para ingresar el nombre del jugador
    entryName=StringVar()
    textName= Entry(ventana, textvariable= entryName,bg="black",fg="blue",font=("Harrington",15),cursor="pirate").place(x=990,y=475)
        #crear botón de iniciar partida
    battle=PhotoImage(file="start.gif")#se elige imagen para el botón
    battlebutton= Button(ventana, image=battle, height=80,
                             width=320,bg="black",cursor="pirate").place(x=800,y=560)#se establece la imagen en el botón.
        
   
    ventana.mainloop()

    #creando el menu 2 jugadores
def menu_2():
        # se modifica el menú principal
    ventana.geometry("1260x690+20+5")#igual tamaño de ventana
    ventana.title("player vs player")#titulo del menu (player vs player)
    imagen=PhotoImage(file="menu2.gif")# igual imagen de fondo del menu 1 jugador
    imagent=Label(ventana,image=imagen,cursor="pirate").place(x=0,y=0)#se establece la imagen de fondo
    # igual imagen de fondo del menu 1 jugador
    
        #se crea la etiqueta para el nombre del jugador 1
    plname1= Label(text="player one's name:",bg="black",fg="blue",font=("Harrington",25),cursor="pirate").place(x=750,y=350)
        #se crea el campo de texto para ingresar el nombre del jugador1
    entryName1=StringVar()
    textName1= Entry(ventana, textvariable= entryName1,
                         bg="black",fg="blue",font=("Harrington",15),width=15,cursor="pirate").place(x=1050,y=360)
        #se crea la etiqueta para el nombre del jugador2
    plname2= Label(text="player two's name:",bg="black",fg="blue",font=("Harrington",25),cursor="pirate").place(x=750,y=430)
        #se crea campo de texto para ingresar nombre jugador2
    entryName2=StringVar()
    textName2= Entry(ventana, textvariable= entryName2,bg="black",fg="blue",font=("Harrington",15),width=15,cursor="pirate").place(x=1050,y=440)
    conditionName=Label(ventana,text="*Max. 6 characters",
                        bg="black",fg="white",font=("Harrington",15),width=25,cursor="pirate").place(x=850,y=300)
    ## CREACIÓN NIVEL 1
    
    def versus_mode1():
        ventana.withdraw()#ocultar menu de dos jugadores
        vsmode=Toplevel()# ejecutar nueva ventana para el nivel 1
        vsmode.geometry("1300x670+20+10")
        vsmode.title("VS MODE")#titulo de la ventana
        vsmode.resizable(0,0)
        player1= PhotoImage(file="screen1.GIF")#mapa jugador 1
        p1= PhotoImage(file="ship1s.GIF")#jugador1
        player2= PhotoImage(file="screen2.GIF")#mapa jugador 2
        p2= PhotoImage(file="ship2s.GIF")#jugador 2
        pit2= PhotoImage(file="pirata31.GIF")#personaje jugador2
        pit1=PhotoImage(file="pirata1p.GIF")#personaje jugador1
        enemy1=PhotoImage(file="enemy1.PNG")#enemigo 1
        enemy2=PhotoImage(file="enemy2.PNG")#enemigo 2
        enemy3=PhotoImage(file="enemy3.PNG")#enemigo 3
        explosion= PhotoImage(file= "explosion1.GIF")
        empty=PhotoImage(file= "empty.GIF")
        
        #crear canvas para pantalla jugador 1
        c1= Canvas(vsmode,width=650,height=670,
                  bd=0,highlightthickness=0,cursor="pirate",bg="black")
        player1s= c1.create_image(420,-3585,image= player1)
        p1m= c1.create_image(415,620, image= p1)
        c1.pack()
        c1.place(x=0,y=0)
        pit1set= c1.create_image(90,130,image=pit1)
        #crear canvas para pantala jugador2
        c2= Canvas(vsmode,width=650,height=670,
                  bd=0,highlightthickness=0,cursor="pirate",bg="black")
        player2s= c2.create_image(230,-3585, image= player2)
        p2m= c2.create_image(235,620, image= p2)
        pit2set= c2.create_image(550,130,image=pit2)
        c2.pack()
        c2.place(x=650,y=0)
        
        vsmode.update()
        #etiqueta de nombre jugador2
        plname2= Label(vsmode,text="PLAYER 2:",bg="black",fg="blue",font=("Harrington",25),cursor="pirate").place(x=1115,y=280)
        #etiqueta de nombre jugador 1
        plname1=  Label(vsmode, text= "PLAYER 1:", bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=17,y=280)
        #establecer nombre del jugador 1 establecido
        name1 = Label(vsmode,text= entryName1.get(),bg="black",fg="white",font=("Pristina",25)).place(x=25,y=325)
        #establecer nombre del jugador 2 establecido
        name2 = Label(vsmode,text= entryName2.get(),bg="black",fg="white",font=("Pristina",25)).place(x=1125,y=325)
        #etiquetas de la variable viento(conbustible)
        wind1 = Label(vsmode,text= "WIND:",bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=17,y=380)
        wind2 = Label(vsmode,text= "WIND:",bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=1115,y=380)
        
        
        x=random.randrange(307,553)
        x1= random.randrange(115,345)
        #creacion de los enemigos en los canvas 1 y 2
        enemy1set= c1.create_image(x,-70, image= enemy1)
        enemy2set= c1.create_image(470,-70, image= enemy2)
        enemy3set= c1.create_image(310,-70,image= enemy3)
        enemy1set2= c2.create_image(x1,-70, image= enemy1)
        enemy2set2= c2.create_image(300,-70, image= enemy2)
        enemy3set2= c2.create_image(120,-70,image=enemy3)    
        #creando movimiento de los mapas
        while 1:
            
            em1= c1.move(enemy1set,0,1.5)
            em2= c2.move(enemy1set2,0,1.5)
            em13=c1.move(enemy3set,0,1.5)
            em23=c2.move(enemy3set2,0,1.5)
            
            v=1#velocidad 
            f=95 #frecuencia
            
                    
            coord1p= c1.coords(p1m)#coordenadas del jugador1
            coord1=c1.coords(player1s)#coordenadas del mapa jugador1
            coord2=c2.coords(player2s)#coordenadas del mapa jugador2
            #movimiento del enemigo1 en el canvas 1
            if c1.coords(enemy1set)[1]>900:
                
                c1.move(enemy1set,random.randint(310.0,551.0)-c1.coords(enemy1set)[0],-900)
                
            #movimiento del enemigo2 en el canvas1
            if c1.coords(enemy2set)[1]>900.0:
                
                
                c1.move(enemy2set,320-c1.coords(enemy2set)[0],-900)
             
            y= math.sin(c1.coords(enemy2set)[1]*math.pi/f)*v*3
            c1.move(enemy2set,y,v)
            #movimiento del enemigo3 en el canvas1
            if c1.coords(enemy3set)[1]>900:
                c1.move(enemy3set,130,-900)
            #movimiento del enemigo1 en el canvas2
            if c2.coords(enemy1set2)[1]>900:
                
                c2.move(enemy1set2,random.randint(117.0,342.0)-c2.coords(enemy1set2)[0],-900)
                
            #movimiento del enemigo2 en el canvas2
            if c2.coords(enemy2set2)[1]>900.0:
                
                
                c2.move(enemy2set2,150-c2.coords(enemy2set2)[0],-900)
                
            y= math.sin(c2.coords(enemy2set2)[1]*math.pi/f)*v*3
            c2.move(enemy2set2,y,v)
            #movimiento del enemigo3 en el canvas2
            if c2.coords(enemy3set2)[1]>900:
                c2.move(enemy3set2,100,-900)
            #seguimiento del enemigo3 al jugador2
            if c2.coords(enemy3set2)[0]> c2.coords(p2m)[0]:
                c2.move(enemy3set2,-1,0)
            if c2.coords(enemy3set)[0]< c2.coords(p2m)[0]:
                c2.move(enemy3set,1,0)

            #colision enemigo3 con jugador1
            if (c1.coords(p1m)[0] == c1.coords(enemy3set)[0]) and (c1.coords(p1m)[1] == c1.coords(enemy3set)[1]):
                
                c1.create_image(c1.coords(p1m),image= explosion)
                
                c1.create_image(415,620,image= p1m)

            if (c1.coords(p1m)[0] == c1.coords(enemy1set)[0]) and (c1.coords(p1m)[1] == c1.coords(enemy1set)[1]):
                
                c1.create_image(c1.coords(p1m),image= explosion)
                
                c1.create_image(415,620,image= p1m)
                
                
            #seguimiento del enemigo3 al jugador1
            if c1.coords(enemy3set)[0]> c1.coords(p1m)[0]:
                c1.move(enemy3set,-1,0)
            if c1.coords(enemy3set)[0]< c1.coords(p1m)[0]:
                c1.move(enemy3set,1,0)
            #movimiento del mapa jugador1
            m1=c1.move(player1s,0,1.5)
            
            
            
            #condicion de parada del mapa jugador1
            if coord1[1] >= 4100.0:
                m1= c1.move(player1s,0,-1.5)
            #movimiento del mapa jugador2 
            m2=c2.move(player2s,0,1.5)
            
            #condicion de parada mapa jugador2
            if coord2[1] >= 4100.0:
                m2=c2.move(player2s,0,-1.5)
            
            #colision enemigo3 con jugador2
            if (c2.coords(p2m)[0] == c2.coords(enemy3set2)[0]) and (c2.coords(p2m)[1] == c2.coords(enemy3set2)[1]):
                
                
                c2.create_image(c2.coords(p2m),image= explosion)
                
                c2.create_image(200,620,image= p2m)    
            ventana.update_idletasks()
            #actualizar
            ventana.update()
            #crear movimientos con teclado jugador1
            def mover1(event1):
                
                if event1.keysym == "w":
                    c1.move(p1m,0,-15)
                    

                if event1.keysym == "s":
                    c1.move(p1m,0,15)
                    

                if event1.keysym == "d":
                    c1.move(p1m,15,0)
                    
                    
                        

                if event1.keysym == "a":
                    
                    c1.move(p1m,-15,0)
                    
                    if c1.coords(p1m)[0]<= 283.0:
                        c1.move(p1m,15,0)
                        
            c1.bind_all('<KeyPress-w>',mover1)
            c1.bind_all('<KeyPress-s>',mover1)
            c1.bind_all('<KeyPress-d>',mover1)
            c1.bind_all('<KeyPress-a>',mover1)
            
            
           #movimiento con teclado jugador2
            def mover2(event2):
                
                if event2.keysym == "Up":
                    c2.move(p2m,0,-15)
                    
                    
                        
                if event2.keysym == "Down":
                    c2.move(p2m,0,15)
                    
                if event2.keysym == "Right":
                    c2.move(p2m,15,0)
                    
                    
                    if c2.coords(p2m)[0]>= 367.0:
                        c2.move(p2m,-15,0) 
                      
                    
                if event2.keysym == "Left":
                    c2.move(p2m,-15,0)
                    
                    
                    if c2.coords(p2m)[0]<= 93.0:
                        c2.move(p2m,15,0)
            

            c2.bind_all('<KeyPress-Up>',mover2)
            c2.bind_all('<KeyPress-Down>',mover2)
            c2.bind_all('<KeyPress-Right>',mover2)
            c2.bind_all('<KeyPress-Left>',mover2)
            
                
            time.sleep(0.000000003)
            
    ## CREACIÓN NIVEL 2 
    def versus_mode2():
        
        ventana.withdraw()
        vsmode=Toplevel()
        vsmode.geometry("1300x670+20+10")
        vsmode.title("VS MODE")
        vsmode.resizable(0,0)
        player1= PhotoImage(file="screen21.GIF")
        p1= PhotoImage(file="ship1s.GIF")
        player2= PhotoImage(file="screen21.GIF")
        p2= PhotoImage(file="ship2s.GIF")
        pit2= PhotoImage(file="pirata31.GIF")
        pit1=PhotoImage(file="pirata1p.GIF")
        c1= Canvas(vsmode,width=650,height=670,bg="black",
                  bd=0,highlightthickness=0,cursor="pirate")
        player1s= c1.create_image(420,-5708,image= player1)
        p1m= c1.create_image(415,620, image= p1)
        c1.pack()
        pit1set= c1.create_image(90,130,image=pit1)
        c1.place(x=0,y=0)
        vsmode.update()

        
        c2= Canvas(vsmode,width=650,height=670,bg="black",
                  bd=0,highlightthickness=0,cursor="pirate")
        player2s= c2.create_image(230,-5708, image= player2)
        p2m= c2.create_image(235,620, image= p2)
        pit2set= c2.create_image(550,130,image=pit2)
        c2.pack()
        c2.place(x=650,y=0)
        plname2= Label(vsmode,text="PLAYER 2:",bg="black",fg="blue",font=("Harrington",25),cursor="pirate").place(x=1115,y=280)
        plname1=  Label(vsmode, text= "PLAYER 1:", bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=17,y=280)
        name1 = Label(vsmode,text= entryName1.get(),bg="black",fg="white",font=("Pristina",25)).place(x=25,y=325)
        name2 = Label(vsmode,text= entryName2.get(),bg="black",fg="white",font=("Pristina",25)).place(x=1125,y=325)
        wind1 = Label(vsmode,text= "WIND:",bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=17,y=380)
        wind2 = Label(vsmode,text= "WIND:",bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=1115,y=380)

        def mover1(event1):
            
            if event1.keysym == "w":
                c1.move(p1m,0,-12)

            if event1.keysym == "s":
                c1.move(p1m,0,12)

            if event1.keysym == "d":
                c1.move(p1m,12,0)
                if c1.coords(p1m)[0]>= 557.0:
                    c1.move(p1m,-13,0)

            if event1.keysym == "a":
                c1.move(p1m,-12,0)
                if c1.coords(p1m)[0]<= 283.0:
                    c1.move(p1m,13,0)
                    
        c1.bind_all('<KeyPress-w>',mover1)
        c1.bind_all('<KeyPress-s>',mover1)
        c1.bind_all('<KeyPress-d>',mover1)
        c1.bind_all('<KeyPress-a>',mover1)
        
        
       
        def mover2(event2):
            
            if event2.keysym == "Up":
                c2.move(p2m,0,-12)
                
                    
            if event2.keysym == "Down":
                c2.move(p2m,0,12)
            if event2.keysym == "Right":
                c2.move(p2m,12,0)
                
                if c2.coords(p2m)[0]>= 367.0:
                    c2.move(p2m,-13,0) 
                  
                
            if event2.keysym == "Left":
                c2.move(p2m,-12,0)
                
                if c2.coords(p2m)[0]<= 93.0:
                    c2.move(p2m,13,0)
        

        c2.bind_all('<KeyPress-Up>',mover2)
        c2.bind_all('<KeyPress-Down>',mover2)
        c2.bind_all('<KeyPress-Right>',mover2)
        c2.bind_all('<KeyPress-Left>',mover2)
        
        while 1:
            
            coord1p= c1.coords(p1m)
            coord1=c1.coords(player1s)
            coord2=c2.coords(player2s)
            
            m1=c1.move(player1s,0,2.5)
            
            
            if coord1[1] >= 6100.0:
                m1= c1.move(player1s,0,-2.5)
            
            m2=c2.move(player2s,0,2.5)
            
            
            if coord2[1] >= 6100.0:
                m2=c2.move(player2s,0,-2.5)
            
                
            ventana.update_idletasks()
            ventana.update()
                
            time.sleep(0.000000003)
    def versus_mode3():
        
        ventana.withdraw()
        vsmode=Toplevel()
        vsmode.geometry("1300x670+20+10")
        vsmode.title("VS MODE")
        vsmode.resizable(0,0)
        player1= PhotoImage(file="screen3.GIF")
        p1= PhotoImage(file="ship1s.GIF")
        player2= PhotoImage(file="screen3.GIF")
        p2= PhotoImage(file="ship2s.GIF")
        pit2= PhotoImage(file="pirata31.GIF")
        pit1=PhotoImage(file="pirata1p.GIF")
        
        
        c1= Canvas(vsmode,width=650,height=670,bg="black",
                  bd=0,highlightthickness=0,cursor="pirate")
        player1s= c1.create_image(420,-7128,image= player1)
        p1m= c1.create_image(415,620, image= p1)
        pit1set= c1.create_image(90,130,image=pit1)
        c1.pack()
        c1.place(x=0,y=0)
        vsmode.update()

        
        c2= Canvas(vsmode,width=650,height=670,bg="black",
                  bd=0,highlightthickness=0,cursor="pirate")
        player2s= c2.create_image(230,-7128, image= player2)
        p2m= c2.create_image(235,620, image= p2)
        pit2set= c2.create_image(550,130,image=pit2)
        c2.pack()
        c2.place(x=650,y=0)
        plname2= Label(vsmode,text="PLAYER 2:",bg="black",fg="blue",font=("Harrington",25),cursor="pirate").place(x=1115,y=280)
        plname1=  Label(vsmode, text= "PLAYER 1:", bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=17,y=280)
        name1 = Label(vsmode,text= entryName1.get(),bg="black",fg="white",font=("Pristina",25)).place(x=25,y=325)
        name2 = Label(vsmode,text= entryName2.get(),bg="black",fg="white",font=("Pristina",25)).place(x=1125,y=325)
        wind1 = Label(vsmode,text= "WIND:",bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=17,y=380)
        wind2 = Label(vsmode,text= "WIND:",bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=1115,y=380)

        def mover1(event1):
            
            if event1.keysym == "w":
                c1.move(p1m,0,-14)

            if event1.keysym == "s":
                c1.move(p1m,0,14)

            if event1.keysym == "d":
                c1.move(p1m,14,0)
                if c1.coords(p1m)[0]>= 557.0:
                    c1.move(p1m,-15,0)

            if event1.keysym == "a":
                c1.move(p1m,-14,0)
                if c1.coords(p1m)[0]<= 283.0:
                    c1.move(p1m,15,0)
                    
        c1.bind_all('<KeyPress-w>',mover1)
        c1.bind_all('<KeyPress-s>',mover1)
        c1.bind_all('<KeyPress-d>',mover1)
        c1.bind_all('<KeyPress-a>',mover1)
        
        def mover2(event2):
            
            if event2.keysym == "Up":
                c2.move(p2m,0,-14)
                        
            if event2.keysym == "Down":
                c2.move(p2m,0,14)
            if event2.keysym == "Right":
                c2.move(p2m,14,0)
                if c2.coords(p2m)[0]>= 367.0:
                    c2.move(p2m,-15,0)
                
                
                      
            if event2.keysym == "Left":
                c2.move(p2m,-14,0)
                
                if c2.coords(p2m)[0]<= 93.0:
                    c2.move(p2m,15,0)
        
        c2.bind_all('<KeyPress-Up>',mover2)
        c2.bind_all('<KeyPress-Down>',mover2)
        c2.bind_all('<KeyPress-Right>',mover2)
        c2.bind_all('<KeyPress-Left>',mover2)
        
        while 1:
            
            coord1p= c1.coords(p1m)
            coord1=c1.coords(player1s)
            coord2=c2.coords(player2s)
            
            m1=c1.move(player1s,0,3.5)
            
            if coord1[1] >= 7600.0:
                m1= c1.move(player1s,0,-3.5)
            
            m2=c2.move(player2s,0,3.5)
            
            if coord2[1] >= 7600.0:
                m2=c2.move(player2s,0,-3.5)
            
            ventana.update_idletasks()
            ventana.update()
                
            time.sleep(0.000000003)


    def versus_mode4():
        
        ventana.withdraw()
        vsmode=Toplevel()
        vsmode.geometry("1300x670+20+10")
        vsmode.title("VS MODE")
        vsmode.resizable(0,0)
        player1= PhotoImage(file="screen4.GIF")
        p1= PhotoImage(file="ship1s.GIF")
        player2= PhotoImage(file="screen4.GIF")
        p2= PhotoImage(file="ship2s.GIF")
        pit2= PhotoImage(file="pirata31.GIF")
        pit1=PhotoImage(file="pirata1p.GIF")
        
        
        c1= Canvas(vsmode,width=650,height=670,bg="black",
                  bd=0,highlightthickness=0,cursor="pirate")
        player1s= c1.create_image(420,-9253,image= player1)
        p1m= c1.create_image(415,620, image= p1)
        pit1set= c1.create_image(90,130,image=pit1)
        c1.pack()
        c1.place(x=0,y=0)
        vsmode.update()

        
        c2= Canvas(vsmode,width=650,height=670,bg="black",
                  bd=0,highlightthickness=0,cursor="pirate")
        player2s= c2.create_image(230,-9253, image= player2)
        p2m= c2.create_image(235,620, image= p2)
        pit2set= c2.create_image(550,130,image=pit2)
        c2.pack()
        c2.place(x=650,y=0)
        plname2= Label(vsmode,text="PLAYER 2:",bg="black",fg="blue",font=("Harrington",25),cursor="pirate").place(x=1115,y=280)
        plname1=  Label(vsmode, text= "PLAYER 1:", bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=17,y=280)
        name1 = Label(vsmode,text= entryName1.get(),bg="black",fg="white",font=("Pristina",25)).place(x=25,y=325)
        name2 = Label(vsmode,text= entryName2.get(),bg="black",fg="white",font=("Pristina",25)).place(x=1125,y=325)
        wind1 = Label(vsmode,text= "WIND:",bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=17,y=380)
        wind2 = Label(vsmode,text= "WIND:",bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=1115,y=380)

        def mover1(event1):
            
            if event1.keysym == "w":
                c1.move(p1m,0,-16)

            if event1.keysym == "s":
                c1.move(p1m,0,16)

            if event1.keysym == "d":
                c1.move(p1m,16,0)
                if c1.coords(p1m)[0]>= 558.0:
                    c1.move(p1m,-17,0)

            if event1.keysym == "a":
                c1.move(p1m,-16,0)
                if c1.coords(p1m)[0]<= 283.0:
                    c1.move(p1m,17,0)
                    
        c1.bind_all('<KeyPress-w>',mover1)
        c1.bind_all('<KeyPress-s>',mover1)
        c1.bind_all('<KeyPress-d>',mover1)
        c1.bind_all('<KeyPress-a>',mover1)
        
        def mover2(event2):
            
            if event2.keysym == "Up":
                c2.move(p2m,0,-16)
                        
            if event2.keysym == "Down":
                c2.move(p2m,0,16)
            if event2.keysym == "Right":
                c2.move(p2m,16,0)
                if c2.coords(p2m)[0]>= 368.0:
                    c2.move(p2m,-17,0)
                
                
                      
            if event2.keysym == "Left":
                c2.move(p2m,-16,0)
                
                if c2.coords(p2m)[0]<= 93.0:
                    c2.move(p2m,17,0)
        
        c2.bind_all('<KeyPress-Up>',mover2)
        c2.bind_all('<KeyPress-Down>',mover2)
        c2.bind_all('<KeyPress-Right>',mover2)
        c2.bind_all('<KeyPress-Left>',mover2)
        
        while 1:
            
            coord1p= c1.coords(p1m)
            coord1=c1.coords(player1s)
            coord2=c2.coords(player2s)
            
            m1=c1.move(player1s,0,4)
            
            if coord1[1] >= 9700.0:
                m1= c1.move(player1s,0,-4)
            
            m2=c2.move(player2s,0,4)
            
            if coord2[1] >= 9700.0:
                m2=c2.move(player2s,0,-4)
            
            ventana.update_idletasks()
            ventana.update()
                
            time.sleep(0.0000003)

    def versus_mode5():
        
        ventana.withdraw()
        vsmode=Toplevel()
        vsmode.geometry("1300x670+20+10")
        vsmode.title("VS MODE")
        vsmode.resizable(0,0)
        player1= PhotoImage(file="screen5.GIF")
        p1= PhotoImage(file="ship1s.GIF")
        player2= PhotoImage(file="screen5.GIF")
        p2= PhotoImage(file="ship2s.GIF")
        pit2= PhotoImage(file="pirata31.GIF")
        pit1=PhotoImage(file="pirata1p.GIF")
        
        
        c1= Canvas(vsmode,width=650,height=670,bg="black",
                  bd=0,highlightthickness=0,cursor="pirate")
        player1s= c1.create_image(420,-11093,image= player1)
        p1m= c1.create_image(415,620, image= p1)
        pit1set= c1.create_image(90,130,image=pit1)
        c1.pack()
        c1.place(x=0,y=0)
        vsmode.update()

        
        c2= Canvas(vsmode,width=650,height=670,bg="black",
                  bd=0,highlightthickness=0,cursor="pirate")
        player2s= c2.create_image(230,-11093, image= player2)
        p2m= c2.create_image(235,620, image= p2)
        pit2set= c2.create_image(550,130,image=pit2)
        c2.pack()
        c2.place(x=650,y=0)
        plname2= Label(vsmode,text="PLAYER 2:",bg="black",fg="blue",font=("Harrington",25),cursor="pirate").place(x=1115,y=280)
        plname1=  Label(vsmode, text= "PLAYER 1:", bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=17,y=280)
        name1 = Label(vsmode,text= entryName1.get(),bg="black",fg="white",font=("Pristina",25)).place(x=25,y=325)
        name2 = Label(vsmode,text= entryName2.get(),bg="black",fg="white",font=("Pristina",25)).place(x=1125,y=325)
        wind1 = Label(vsmode,text= "WIND:",bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=17,y=380)
        wind2 = Label(vsmode,text= "WIND:",bg= "black", fg="blue",font=("Harrington",25),cursor="pirate").place(x=1115,y=380)

        def mover1(event1):
            
            if event1.keysym == "w":
                c1.move(p1m,0,-18)

            if event1.keysym == "s":
                c1.move(p1m,0,18)

            if event1.keysym == "d":
                c1.move(p1m,18,0)
                if c1.coords(p1m)[0]>= 557.0:
                    c1.move(p1m,-19,0)

            if event1.keysym == "a":
                c1.move(p1m,-18,0)
                if c1.coords(p1m)[0]<= 283.0:
                    c1.move(p1m,19,0)
                    
        c1.bind_all('<KeyPress-w>',mover1)
        c1.bind_all('<KeyPress-s>',mover1)
        c1.bind_all('<KeyPress-d>',mover1)
        c1.bind_all('<KeyPress-a>',mover1)
        
        
        def mover2(event2):
            
            if event2.keysym == "Up":
                c2.move(p2m,0,-18)
                        
            if event2.keysym == "Down":
                c2.move(p2m,0,18)
            if event2.keysym == "Right":
                c2.move(p2m,18,0)
                if c2.coords(p2m)[0]>= 368.0:
                    c2.move(p2m,-19,0)
                
                
                      
            if event2.keysym == "Left":
                c2.move(p2m,-18,0)
                
                if c2.coords(p2m)[0]<= 93.0:
                    c2.move(p2m,19,0)
        
        c2.bind_all('<KeyPress-Up>',mover2)
        c2.bind_all('<KeyPress-Down>',mover2)
        c2.bind_all('<KeyPress-Right>',mover2)
        c2.bind_all('<KeyPress-Left>',mover2)
        
        while 1:
            
            coord1p= c1.coords(p1m)
            coord1=c1.coords(player1s)
            coord2=c2.coords(player2s)
            
            m1=c1.move(player1s,0,5.5)
            
            if coord1[1] >= 11600.0:
                m1= c1.move(player1s,0,-5.5)
            
            m2=c2.move(player2s,0,5.5)
            
            if coord2[1] >= 11600.0:
                m2=c2.move(player2s,0,-5.5)
            
            ventana.update_idletasks()
            ventana.update()
                
            time.sleep(0.0000003)
        
    #battle=PhotoImage(file="start.gif")#igual imagen a la del menu 1 jugador
    lvl1button= Button(ventana,text="Level 1", 
                             width=9,bg="black",fg="blue",font=("Harrington",15),cursor="pirate",command=versus_mode1).place(x=770,y=500)#se establece la imagen en el botón.

    lvl2wobutton= Button(ventana,text="Level 2", 
                             width=9,bg="black",fg="blue",font=("Harrington",15),cursor="pirate",command=versus_mode2).place(x=920,y=500)

    lvl3button= Button(ventana,text="Level 3", 
                             width=9,bg="black",fg="blue",font=("Harrington",15),cursor="pirate",command=versus_mode3).place(x=1070,y=500)

    lvl4button= Button(ventana,text="Level 4", 
                             width=9,bg="black",fg="blue",font=("Harrington",15),cursor="pirate",command=versus_mode4).place(x=850,y=560)

    lvl5button= Button(ventana,text="Level 5", 
                             width=9,bg="black",fg="blue",font=("Harrington",15),cursor="pirate",command=versus_mode5).place(x=1000,y=560)
    ventana.mainloop()
    
  
    #creando los botones del menu principal
    #boton 1 solo jugador con comando en función ventana1()
boton1player=Button(ventana,text="Single Player",fg="blue",bg="black",font=("Harrington",25),width=15,cursor="pirate",command= menu_1).place(x=500,y=400)
#boton 2 jugadores con comando en función ventana2()
boton2players=Button(ventana,text=" Vs Mode",fg="blue",bg="black",font=("Harrington",25),width=15,cursor="pirate",command=menu_2).place(x=500,y=500)
ventana.mainloop()

