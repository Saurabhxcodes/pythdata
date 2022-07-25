from turtle import *


speed('slowest')
pencolor('red')
bgcolor('black')
pensize(10)
side = 12
size =200

begin_fill()
fillcolor('green')
for i in range(side):
    fd(size)
    lt(360/size)
    rt(100)


end_fill()
mainloop()