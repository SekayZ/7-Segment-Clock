#RACHID Kayssé
#Horloge 7 segments

from Tkinter import *

from datetime import* 


#Création des fenêtres
Win=Tk()
can=Canvas(width=610,height=200)
can.pack()

can.create_rectangle(0,0,610,610,fill="white",outline="white")
can.create_rectangle(10,20,190,180,width=2,fill="black")
can.create_rectangle(220,20,400,180,width=2,fill="black")
can.create_rectangle(430,20,600,180,width=2,fill="black")


can.create_rectangle(195,70,215,90,width=2,fill="red")
can.create_rectangle(195,110,215,130,width=2,fill="red")

can.create_rectangle(405,70,425,90,width=2,fill="red")
can.create_rectangle(405,110,425,130,width=2,fill="red")

#Coordonnées des segments 
chiffre={0:[1,2,3,4,5,6], 1:[2,3], 2:[1,2,7,5,4], 3:[1,2,3,4,7], 4:[6,7,2,3], 5:[1,6,7,3,4], 6:[1,6,5,4,3,7], 7:[1,2,3], 8:[1,2,3,4,5,6,7], 9:[1,2,3,4,6,7]}

lignea={1:[30,50,80,50],2:[85,55,85,95],3:[85,105,85,145],4:[30,150,80,150],5:[25,105,25,145],6:[25,55,25,95],7:[30,100,80,100]}
ligneb={1:[120,50,170,50],2:[175,55,175,95],3:[175,105,175,145],4:[120,150,170,150],5:[115,105,115,145],6:[115,55,115,95],7:[120,100,170,100]}
a=0
b=0

lignec={1:[240,50,290,50],2:[295,55,295,95],3:[295,105,295,145],4:[240,150,290,150],5:[235,105,235,145],6:[235,55,235,95],7:[240,100,290,100]}
ligned={1:[330,50,380,50],2:[385,55,385,95],3:[385,105,385,145],4:[330,150,380,150],5:[325,105,325,145],6:[325,55,325,95],7:[330,100,380,100]}
c=0
d=0

lignee={1:[450,50,500,50],2:[505,55,505,95],3:[505,105,505,145],4:[450,150,500,150],5:[445,105,445,145],6:[445,55,445,95],7:[450,100,500,100]}
lignef={1:[540,50,590,50],2:[595,55,595,95],3:[595,105,595,145],4:[540,150,590,150],5:[535,105,535,145],6:[535,55,535,95],7:[540,100,590,100]}
e=0
f=0

#Récupération du temps et création des segments gris
while 1:
    a=0
    b=0
    hour=datetime.now().hour
    can.create_line(30,50,80,50,width=5,fill="#1C1C1C")
    can.create_line(30,100,80,100,width=5,fill="#1C1C1C")
    can.create_line(30,150,80,150,width=5,fill="#1C1C1C")
    can.create_line(120,50,170,50,width=5,fill="#1C1C1C")
    can.create_line(120,100,170,100,width=5,fill="#1C1C1C")
    can.create_line(120,150,170,150,width=5,fill="#1C1C1C")

    can.create_line(25,55,25,95,width=5,fill="#1C1C1C")
    can.create_line(115,55,115,95,width=5,fill="#1C1C1C")
    can.create_line(85,55,85,95,width=5,fill="#1C1C1C")
    can.create_line(175,55,175,95,width=5,fill="#1C1C1C")
    can.create_line(25,105,25,145,width=5,fill="#1C1C1C")
    can.create_line(115,105,115,145,width=5,fill="#1C1C1C")
    can.create_line(85,105,85,145,width=5,fill="#1C1C1C")
    can.create_line(175,105,175,145,width=5,fill="#1C1C1C")

    c=0
    d=0
    minute=datetime.now().minute
    can.create_line(240,50,290,50,width=5,fill="#1C1C1C")
    can.create_line(240,100,290,100,width=5,fill="#1C1C1C")
    can.create_line(240,150,290,150,width=5,fill="#1C1C1C")
    can.create_line(330,50,380,50,width=5,fill="#1C1C1C")
    can.create_line(330,100,380,100,width=5,fill="#1C1C1C")
    can.create_line(330,150,380,150,width=5,fill="#1C1C1C")

    can.create_line(235,55,235,95,width=5,fill="#1C1C1C")
    can.create_line(325,55,325,95,width=5,fill="#1C1C1C")
    can.create_line(295,55,295,95,width=5,fill="#1C1C1C")
    can.create_line(385,55,385,95,width=5,fill="#1C1C1C")
    can.create_line(235,105,235,145,width=5,fill="#1C1C1C")
    can.create_line(325,105,325,145,width=5,fill="#1C1C1C")
    can.create_line(295,105,295,145,width=5,fill="#1C1C1C")
    can.create_line(385,105,385,145,width=5,fill="#1C1C1C")

    e=0
    f=0
    seconde=datetime.now().second
    can.create_line(450,50,500,50,width=5,fill="#1C1C1C")
    can.create_line(450,100,500,100,width=5,fill="#1C1C1C")
    can.create_line(450,150,500,150,width=5,fill="#1C1C1C")
    can.create_line(540,50,590,50,width=5,fill="#1C1C1C")
    can.create_line(540,100,590,100,width=5,fill="#1C1C1C")
    can.create_line(540,150,590,150,width=5,fill="#1C1C1C")

    can.create_line(445,55,445,95,width=5,fill="#1C1C1C")
    can.create_line(535,55,535,95,width=5,fill="#1C1C1C")
    can.create_line(505,55,505,95,width=5,fill="#1C1C1C")
    can.create_line(595,55,595,95,width=5,fill="#1C1C1C")
    can.create_line(445,105,445,145,width=5,fill="#1C1C1C")
    can.create_line(535,105,535,145,width=5,fill="#1C1C1C")
    can.create_line(505,105,505,145,width=5,fill="#1C1C1C")
    can.create_line(595,105,595,145,width=5,fill="#1C1C1C")
    

 
    

#Affichage du temps
    while(hour>=10):
        hour=hour-10
        a=a+1
    b=hour
    sgtb=list(chiffre [b])
    sgta=list(chiffre [a])

    for i in sgtb:
        can.create_line(ligneb[i],width=5,fill="red")
    for j in sgta:
        can.create_line(lignea[j],width=5,fill="red")


    while(minute>=10):
        minute=minute-10
        c=c+1
    d=minute

    sgtd=list(chiffre [d])
    sgtc=list(chiffre [c])
    for k in sgtd:
        can.create_line(ligned[k],width=5,fill="red")
    for l in sgtc:
        can.create_line(lignec[l],width=5,fill="red")
    


    while(seconde>=10):
        seconde=seconde-10
        e=e+1
    f=seconde
    sgtf=list(chiffre [f])
    sgte=list(chiffre [e])

    for m in sgtf:
        can.create_line(lignef[m],width=5,fill="red")
    for n in sgte:
        can.create_line(lignee[n],width=5,fill="red")

    Win.update()


    


    
    
     

    

    








    



