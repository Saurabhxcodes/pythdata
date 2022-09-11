from shutil import move
import pgzrun
HEIGHT =300
WIDTH = 500
p = Actor('ironman',pos=(100,100))
def draw():
    screen.clear()
    p.draw()
    animate('ironman', tween = 'linear', duration = 1, on_finshed= 'none' ,   pos=(100, 100))
        
        
pgzrun.go()
