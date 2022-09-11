import pgzrun
HEIGHT =300
WIDTH = 500
p = Actor('ironman',pos=(100,100))
def draw():
    screen.clear()
    screen.draw.text("welcome to the pgzrun",(10,10),color='red',fontsize=50)
    screen.draw.text('created by me',(10,460),color='white')
    p.draw()
pgzrun.go()
